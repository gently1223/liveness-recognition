import base64
import json
import numpy as np
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .functions import encodeFaces
from .functions import livenessRecognize
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import os
import cv2

global count
count = 0

def fnLogin(request):
    if request.method == 'POST':
        m_request = json.loads(request.body.decode('utf-8'))
        frame_ = m_request['image']
        frame_ = str(frame_)
        data = frame_.replace('data:image/jpeg;base64,', '')
        print(len(data))
        data = data.replace(' ', '+')
        decoded = base64.b64decode(data)
        try:
            buffer = np.fromstring(decoded, np.float32)
            image_array = cv2.imdecode(buffer, cv2.IMREAD_COLOR)
            res = livenessRecognize(image_array)
            # print("RESULT is ", res, type(res))
            if res == 1:
                global count
                count += 1
                if count > 5:
                    print(count)
                    count = 0
                    return HttpResponse(1)
            else:
                return HttpResponse(0)    
        except:
            print('Error')
            return HttpResponse(0)
    return HttpResponse(0)
    
def fnSignup(request):
    if request.method == 'POST':
        m_request = json.loads(request.body.decode('utf-8'))
        frame_ = m_request['image']
        frame_ = str(frame_)
        data = frame_.replace('data:image/jpeg;base64,', '')
        data = data.replace(' ', '+')
        imgdata = base64.b64decode(data)
        userId = np.random.rand()
        userId = userId * 999999999
        userId = str(int(userId))
        
        os.mkdir('dataset/' + userId)
        filename = 'dataset/' + userId + '/' + userId + '.jpg'
        with open(filename, 'wb') as f:
            print(filename)
            f.write(imgdata)

        encodeFaces()

    return HttpResponse(1)