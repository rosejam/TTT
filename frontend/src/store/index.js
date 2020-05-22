import Vue from "vue";
import Vuex from "vuex";
import store from "./modules/store";
import user from "./modules/user";
import app from "./modules/app";
import search from "./modules/search";
import quest from "./modules/quest";
import ranking from "./modules/ranking";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    store,
    user,
    search,
    app,
    quest,
    ranking,
  }
});
