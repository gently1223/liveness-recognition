<template>
  <div  class="overlay-panel overlay-right">
    <h1
      :class="{
        'px-2 my-4 sm-title font-weight-bold ': $vuetify.breakpoint.smAndDown,
        'px-8 my-4 md-title font-weight-bold ': $vuetify.breakpoint.mdAndUp,
      }"
    >
      Welcome !
    </h1>
    <div
      :class="{
        'sm-description ': $vuetify.breakpoint.smAndDown,
        'md-description ': $vuetify.breakpoint.mdAndUp,
      }"
    >
      You don't have an account ?
    </div>
    <div
      :class="{
        'sm-description ': $vuetify.breakpoint.smAndDown,
        'md-description ': $vuetify.breakpoint.mdAndUp,
      }"
    >
      Please Sign Up from here
    </div>
    <v-btn
      color="info"
      dark
      rounded
       :class="{
        'pa-4 my-10 font-weight-bold': $vuetify.breakpoint.smAndDown,
        'pa-6 my-10 font-weight-bold': $vuetify.breakpoint.mdAndUp,
      }"
      elevation="0"
      @click="isSignInPanelActive = true"
    >
      Sign Up
    </v-btn>
  </div>
</template>



<script>
export default {
  computed: {
    isSignInPanelActive: {
      get: function () {
        return this.$store.getters["authPageModule/getIsSignInPanelActive"];
      },
      set: function (newVal) {
        this.$store.commit("authPageModule/setIsSignInPanelActive", newVal);
      },
    },
  },
};
</script>


<style scoped>
.overlay-right {
  right: 0;
  transform: translateX(0);
}


</style>