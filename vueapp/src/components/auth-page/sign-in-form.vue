<template>
  <div class="form-container sign-in-container mt-12">
    <v-form
      action="#"
      :class="{
        'px-2 mt-12': $vuetify.breakpoint.smAndDown,
        'px-8': $vuetify.breakpoint.mdAndUp,
      }"
    >
      <h1 class="pb-12 font-weight-bold">Sign in</h1>

      <div id="app" class="web-camera-container">
        <div class="camera-button">
          <button 
            type="button" 
            class="button is-rounded"
            :class="{ 'is-primary' : !isCameraOpen, 'is-danger' : isCameraOpen}" @click="toggleCamera">
            <span v-if="!isCameraOpen">Open Camera</span>
            <span v-else>Close Camera</span>
          </button>
        </div>

        <div v-show="isCameraOpen && isLoading" class="camera-loading">
          <ul class="loader-circle">
            <li></li>
            <li></li>
            <li></li>
          </ul>
        </div>

        <div v-if="isCameraOpen" v-show="!isLoading" class="camera-box" :class="{ 'flash' : isShotPhoto }">
          <div class="camera-shutter" :class="{'flash' : isShotPhoto}"></div>

          <video v-show="!isPhotoTaken" id="camera" ref="camera" :width="450" :height="337.5" autoplay></video>

          <canvas v-show="isPhotoTaken" id="canvas" ref="canvas" :width="450" :height="337.5"></canvas>

        </div>

      </div>
    </v-form>
  </div>
</template>
<script>
import axios from 'axios'

export default {
  data: () => {
    return {
      isCameraOpen: false,
      isPhotoTaken: false,
      isShotPhoto: false,
      isLoading: false,
      link: '#'
    };
  },
  methods: {
    toggleCamera() {
      if(this.isCameraOpen) {
        this.isCameraOpen = false;
        this.isPhotoTaken = false;
        this.isShotPhoto = false;
        this.stopCameraStream();
      } else {
        this.isCameraOpen = true;
        this.createCameraElement();
      }
    },
    createCameraElement() {
      this.isLoading = true;

      const constraints = (window.constraints = {
        audio: false,
        video: true
      });

      navigator.mediaDevices
        .getUserMedia(constraints)
        .then(stream => {
          this.isLoading = false;
          this.$refs.camera.srcObject = stream;
        })
        .catch(error => {
          this.isLoading = false;
          alert("May the browser didn't support or there is some errors.");
        });

      // TODO: 
      if (navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({
          audio: false,
          video: true
        })
        .then(function(stream) {
          const canvas = document.getElementById('canvas');
          const video = document.getElementById('camera');
          var context = canvas.getContext('2d');
          video.srcObject = stream;
          var timeLeft = 45;
          var timerId = setInterval(countdown, 1000);

          function countdown() {
            if (timeLeft == 0) {
              clearTimeout(timerId);
              alert("Sign In Failed, try again.")
            } else {
              timeLeft--;
              
              let width = video.width;
              let height = video.height;
              context.drawImage(video, 0, 0, width, height);
              var data = canvas.toDataURL('image/jpeg', 0.5);
              context.clearRect(0, 0, width, height);
              // TODO: Axios function
              let payload = {'image': data}

              axios.post('http://127.0.0.1:8000/signin/', payload)
              .then(function (response) {
                if(response.data == 1) {
                  console.log("kkkkkkkkkkkkkkkkk")
                  console.log("Success", response)
                  clearTimeout(timerId);
                  alert("Sign In Success")
                }
                console.log(response.data);
              })
              .catch(function (error) {
                console.log(error)
              })
            }
          }
        })
      }


    },
    stopCameraStream() {
      let tracks = this.$refs.camera.srcObject.getTracks();
      tracks.forEach(track => {
        track.stop();
      });
    },
  },
};
</script>
<style scoped>
.sign-in-container {
  left: 0;
  width: 50%;
  z-index: 2;
}

.container.right-panel-active .sign-in-container {
  transform: translateX(100%);
}

.container.right-panel-active .overlay-container {
  transform: translateX(-100%);
}
.forgot-password-sm {
  font-size: 12px;
}
.forgot-password-md {
  font-size: 15px;
}

.web-camera-container {
  padding: 2rem;
  display: flex;
  margin: 5px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.camera-button {
  margin-bottom: 2rem;
}

.camera-box.camera-shutter {
  opacity: 0;
  width: 450px;
  height: 337.5px;
  background-color: #fff;
  position: absolute;
}

@keyframes flash {
   0%, 100% {
      opacity: 1;
   }
}
.camera-shoot button {
  height: 60px;
  width: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 100%;
}
.camera-shoot button img {
  height: 35px;
  object-fit: cover;
}
.camera-loading {
  overflow: hidden;
  height: 100%;
  position: absolute;
  width: 100%;
  min-height: 150px;
  margin: 3rem 0 0 -1.2rem;
}
.camera-loading ul {
  height: 100%;
  position: absolute;
  width: 100%;
  z-index: 999999;
  margin: 0;
}
.camera-loading.loader-circle {
  display: block;
  height: 14px;
  margin: 0 auto;
  top: 50%;
  left: 100%;
  transform: translateY(-50%);
  transform: translateX(-50%);
  position: absolute;
  width: 100%;
  padding: 0;
}
.image-circle li {
  display: block;
  float: left;
  width: 10px;
  height: 10px;
  line-height: 10px;
  padding: 0;
  position: relative;
  margin: 0 0 0 4px;
  background: #999;
  animation: preload 1s infinite;
  top: -50%;
  border-radius: 100%;
}
.image-circle li:nth-child(2) {
  animation-delay: .2s;
}
.image-circle li:nth-child(3) {
  animation-delay: .4s;
}
@keyframes preload {
  0% {
    opacity: 1
  }
  50% {
    opacity: .4
  }
  100% {
    opacity: 1
  }
}
.button {
  border-radius: 50px;
}
.button.is-primary  {
  background-color: #00d1b2;
  border-color: transparent;
  color: #fff;
}
.button.is-danger  {
  background-color: #ff3860;
  border-color: transparent;
  color: #fff;
}
</style>