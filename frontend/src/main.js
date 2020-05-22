/*!

 =========================================================
 * Vue Now UI Kit - v1.1.0
 =========================================================

 * Product Page: https://www.creative-tim.com/product/now-ui-kit
 * Copyright 2019 Creative Tim (http://www.creative-tim.com)

 * Designed by www.invisionapp.com Coded by www.creative-tim.com

 =========================================================

 * The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

 */
import Vue from 'vue';
import App from './App.vue';
// You can change this import to `import router from './starterRouter'` to quickly start development from a blank layout.
import router from './router';
import NowUiKit from './plugins/now-ui-kit';
import firebase from 'firebase';
import VueSession from 'vue-session'


Vue.config.productionTip = false;

var sessionOptions = {
  persist: true
}

Vue.use(VueSession, sessionOptions)
Vue.use(NowUiKit);

// EK web app's Firebase configuration
const firebaseConfig = {
	apiKey: "AIzaSyAQcDuePSnmmdWecgcYpxkfg_qMsSWiRQk",
	authDomain: "cre8or-2a293.firebaseapp.com",
	databaseURL: "https://cre8or-2a293.firebaseio.com",
	projectId: "cre8or-2a293",
	storageBucket: "cre8or-2a293.appspot.com",
	messagingSenderId: "760192275657",
	appId: "1:760192275657:web:1a1a9ab7a20c6ac02d2918"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

new Vue({
  router,
  render: h => h(App)
}).$mount('#app');
