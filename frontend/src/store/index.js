import Vue from "vue";
import Vuex from "vuex";
import stock from "./modules/stock";
import user from "./modules/user";
import app from "./modules/app";

Vue.use(Vuex);

export default new Vuex.Store({

  modules: {
    stock,
    user,
    app,
  }
  
});
