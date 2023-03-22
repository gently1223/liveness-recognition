<template>
  <v-container
    id="container"
    :class="isSignInPanelActive ? 'container right-panel-active' : 'container'"
  >
    <SignUpForm />
    <SignInForm />
    <div class="overlay-container">
      <div class="overlay">
        <OverlaySignUp />
        <OverlaySignIn />
      </div>
    </div>
  </v-container>
</template>

<script>
import SignInForm from "../components/auth-page/sign-in-form.vue";
import SignUpForm from "../components/auth-page/sign-up-form.vue";
import OverlaySignUp from "../components/auth-page/overlay-sign-up.vue";
import OverlaySignIn from "../components/auth-page/overlay-sign-in.vue";
export default {
  components: {
    SignInForm,
    SignUpForm,
    OverlaySignUp,
    OverlaySignIn,
  },
  computed: {
    isSignInPanelActive: {
      get: function () {
        return this.$store.getters["authPageModule/getIsSignInPanelActive"];
      },
      set: function (newVal) {
        this.$store.commit("authPageModule/setIsSignInPanelActive", newVal);
      },
    },
    currentSignUpStep: {
      get: function () {
        return this.$store.getters["authPageModule/getCurrentSignUpStep"];
      },
      set: function (newVal) {
        this.$store.commit("authPageModule/setCurrentSignUpStep", newVal);
      },
    },
  },
};
</script>


<style>
@import url("https://fonts.googleapis.com/css?family=Montserrat:400,800");

form {
  background-color: #ffffff;
  height: 100%;
}

.container {
  background-color: #fff;
  position: relative;
  overflow: hidden;
  max-width: 100%!important;
  min-height: 100vh!important;
}

.form-container {
  position: absolute;
  top: 0;
  height: 100%;
  transition: all 0.6s ease-in-out;
}

.overlay-container {
  position: absolute;
  top: 0;
  left: 50%;
  width: 50%;
  height: 100%;
  overflow: hidden;
  transition: transform 0.6s ease-in-out;
  z-index: 100;
}

.container.right-panel-active .overlay-container {
  transform: translateX(-100%);
}

.overlay {
  background: #ff416c;
  background: -webkit-linear-gradient(to right, #e260c6, #417dff);
  background: linear-gradient(to right, #284563, #89c7fa);
  background-repeat: no-repeat;
  background-size: cover;
  background-position: 0 0;
  color: #ffffff;
  position: relative;
  left: -100%;
  height: 100%;
  width: 200%;
  transform: translateX(0);
  transition: transform 0.6s ease-in-out;
}

.container.right-panel-active .overlay {
  transform: translateX(50%);
}

.overlay-panel {
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  text-align: center;
  top: 0;
  height: 100%;
  width: 50%;
  transform: translateX(0);
  transition: transform 0.6s ease-in-out;
}
.container.right-panel-active .overlay-left {
  transform: translateX(0);
}

.container.right-panel-active .overlay-right {
  transform: translateX(20%);
}
/* font sizes */
.sm-title {
  font-size: 18px;
}
.md-title {
  font-size: 44px;
}
.sm-description {
  font-size: 12px;
}
.md-description {
  font-size: 16px;
}
</style>