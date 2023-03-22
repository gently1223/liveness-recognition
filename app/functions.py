from imutils import paths
import pickle
import cv2
import os
from sklearn.preprocessing import Normalizer
import tensorflow as tf
import imutils
import numpy as np
from architecture import * 
import mtcnn
import pickle 
import numpy as np 
from scipy.spatial.distance import cosine
from train_v2 import normalize,l2_normalizer
from tensorflow.keras.models import load_model
from detect import load_pickle 

confidence_t=0.99
recognition_t=0.5
required_size = (160,160)

def get_face(img, box):
    x1, y1, width, height = box
    x1, y1 = abs(x1), abs(y1)
    x2, y2 = x1 + width, y1 + height
    face = img[y1:y2, x1:x2]
    return face, (x1, y1), (x2, y2)

def get_encode(face_encoder, face, size):
    face = normalize(face)
    face = cv2.resize(face, size)
    encode = face_encoder.predict(np.expand_dims(face, axis=0))[0]
    return encode


def load_pickle(path):
    with open(path, 'rb') as f:
        encoding_dict = pickle.load(f)
    return encoding_dict

def detect(img ,detector,encoder,encoding_dict):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = detector.detect_faces(img_rgb)
    for res in results:
        if res['confidence'] < confidence_t:
            continue
        face, pt_1, pt_2 = get_face(img_rgb, res['box'])
        encode = get_encode(encoder, face, required_size)
        encode = l2_normalizer.transform(encode.reshape(1, -1))[0]
        name = 'unknown'

        distance = float("inf")
        for db_name, db_encode in encoding_dict.items():
            dist = cosine(db_encode, encode)
            if dist < recognition_t and dist < distance:
                name = db_name
                distance = dist
    return name

global imgIndex
imgIndex = 0

def livenessRecognize(frame):
    """This function takes a video as input and returns 
    1 when the face is live and is registered in the
    database and returns 0 when not"""
    required_shape = (160,160)
    face_encoder = InceptionResNetV2()
    path_m = "facenet_keras_weights.h5"
    face_encoder.load_weights(path_m)
    encodings_path = 'my_encodings.pkl'
    face_detector = mtcnn.MTCNN()
    encoding_dict = load_pickle(encodings_path)

    """This function takes a video as input and returns 
    1 when the face is live and is registered in the
    database and returns 0 when not"""
    res = 0
    print('[INFO] loading face detector...')
    proto_path = 'face_detector/deploy.prototxt'
    model_path = 'face_detector/res10_300x300_ssd_iter_140000.caffemodel'
    detector_net = cv2.dnn.readNetFromCaffe(proto_path, model_path)

    liveness_model = tf.keras.models.load_model('liveness.model')
    le = pickle.loads(open('label_encoder.pickle', 'rb').read())

    frame = imutils.resize(frame, width=600)
    
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300,300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
    
    # pass the blob through the network 
    # and obtain the detections and predictions
    detector_net.setInput(blob)
    detections = detector_net.forward()
    
    # iterate over the detections
    for i in range(0, detections.shape[2]):
        # extract the confidence (i.e. probability) associated with the prediction
        confidence = detections[0, 0, i, 2]
        
        # filter out weak detections
        if confidence > 0.9:
            # compute the (x,y) coordinates of the bounding box
            # for the face and extract the face ROI
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype('int')
            
            # ensure that the bounding box does not fall outside of the frame
            startX = max(0, startX)
            startY = max(0, startY)
            endX = min(w, endX)
            endY = min(h, endY)
            
            # extract the face ROI and then preprocess it
            # in the same manner as our training data
            face = frame[startY:endY, startX:endX]
            # cv2.imwrite(str(imgIdx) + '.jpg', face)
            # some error occur here if my face is out of frame and comeback in the frame
            try:
                face = cv2.resize(face, (32,32))
            except:
                break
            face = face.astype('float') / 255.0 
            face = tf.keras.preprocessing.image.img_to_array(face)

            face = np.expand_dims(face, axis=0)
            preds = liveness_model.predict(face)[0]
            j = np.argmax(preds)
            label = le.classes_[j] # get label of predicted class
            livenessLabel = label

            # __________________Face Recognition Part_______________________
            name = detect(frame , face_detector , face_encoder , encoding_dict)
            print('livenesslabel and name', livenessLabel, name)
            if livenessLabel == 'real' and name != 'unknown':
                return 1
            else:
                return 0
                            
 

def encodeFaces():
    ######pathsandvairables#########
    face_data = 'dataset/'
    required_shape = (160,160)
    face_encoder = InceptionResNetV2()
    path = "facenet_keras_weights.h5"
    face_encoder.load_weights(path)
    face_detector = mtcnn.MTCNN()
    encodes = []
    encoding_dict = dict()
    l2_normalizer = Normalizer('l2')
    ###############################


    def normalize(img):
        mean, std = img.mean(), img.std()
        return (img - mean) / std


    for face_names in os.listdir(face_data):
        person_dir = os.path.join(face_data,face_names)

        for image_name in os.listdir(person_dir):
            image_path = os.path.join(person_dir,image_name)

            img_BGR = cv2.imread(image_path)
            img_RGB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2RGB)

            x = face_detector.detect_faces(img_RGB)
            x1, y1, width, height = x[0]['box']
            x1, y1 = abs(x1) , abs(y1)
            x2, y2 = x1+width , y1+height
            face = img_RGB[y1:y2 , x1:x2]
            
            face = normalize(face)
            face = cv2.resize(face, required_shape)
            face_d = np.expand_dims(face, axis=0)
            encode = face_encoder.predict(face_d)[0]
            encodes.append(encode)

        if encodes:
            encode = np.sum(encodes, axis=0 )
            encode = l2_normalizer.transform(np.expand_dims(encode, axis=0))[0]
            encoding_dict[face_names] = encode
        
    path = 'my_encodings.pkl'
    with open(path, 'wb') as file:
        pickle.dump(encoding_dict, file)