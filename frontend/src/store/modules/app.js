import { set, toggle } from "@/utils/vuex";

const state = {
  drawer: null,
  page: ""
};

// mutations
const mutations = {
  setDrawer: set("drawer"),
  toggleDrawer: toggle("drawer"),
  setPage: set("page")
};

export default {
  namespaced: true,
  state,
  mutations
};
