<template>
  <div id="app" class="card-overlay">
    <v-app>
      <div>
        <router-view />
      </div>
    </v-app>
  </div>
</template>

<style>
@import url("https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;500;600;700;800;900&display=swap");

#app {
  font-family: Raleway, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-repeat: no-repeat;
  background-size: cover;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
}
.footer-md {
  padding: 30px 0px;
}
.footer-md a {
  text-decoration: none;
  color: white !important;
  font-size: 1.1rem;
  font-family: cursive;
  font-weight: 600;
}

.footer-sm {
  padding: 20px 0px;
}
.footer-sm a {
  text-decoration: none;
  color: white !important;
  font-size: 0.8rem;
  font-family: cursive;
  font-weight: 600;
}

.overflow-hidden {
  overflow: hidden;
}

.button {
  border: none;
  color: #FFF;
  background: #42b983;
  appearance: none;
  font: inherit;
  font-size: 1.8rem;
  padding: .5em 1em;
  border-radius: .3em;
  cursor: pointer;
}

.modal {
  position: absolute;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  margin: auto;
  text-align: center;
  width: 800px;
  max-height: 800px;
  height: fit-content;
  padding: 2rem;
  border-radius: 1rem;
  box-shadow: 0 5px 5px rgba(0, 0, 0, 0.2);
  background: #FFF;
  z-index: 999;
  transform: none;
}

.faq-body {
  background: #fff;
  overflow: scroll;
  border: 1px solid #7b7d7f;
}

.faq-body::-webkit-scrollbar {
  width: 16px;
}
.faq-body::-webkit-scrollbar-thumb {
  background-color: #7b7d7f;
  border: 5px solid #fff;
  border-radius: 10rem;
}
.faq-body::-webkit-scrollbar-track {
  position: absolute;
  right: -3rem;
  top: -50rem;
  background: transparent;
}

.modal h3 {
  margin: 0 0 1rem;
}

.modal-overlay {
  content: '';
  position: absolute;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 998;
  background: #2c3e50;
  opacity: 0.6;
  cursor: pointer;
}

/* ---------------------------------- */
.fade-enter-active,
.fade-leave-active {
  transition: opacity .4s linear;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}

.pop-enter-active,
.pop-leave-active {
  transition: transform 0.4s cubic-bezier(0.5, 0, 0.5, 1), opacity 0.4s linear;
}

.pop-enter,
.pop-leave-to {
  opacity: 0;
  transform: scale(0.3) translateY(-50%);
}
</style>
