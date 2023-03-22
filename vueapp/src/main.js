import Vue from 'vue'
import App from './App.vue'
import router from './router'
import { store } from './store'
import vuetify from './plugins/vuetify'
import '@babel/polyfill'
import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.config.productionTip = false;
// axios
Vue.use(VueAxios, axios);
// sweet alert config
const options = {
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
};
Vue.use(VueSweetalert2, options);


new Vue({
    router,
    store,
    vuetify,
    render: h => h(App)
}).$mount('#app')