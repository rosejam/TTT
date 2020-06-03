import api from "../../api";

// initial state
const state = {
  userInfo: {
    uid: null,
  },
};

// actions
const actions = {
  async setUser({ commit }) {
    const userInfo = await api.getUserInfo();
    commit("setUserInfo", userInfo);
  },
};

// mutations
const mutations = {
  setUserInfo(state, userInfo) {
    state.userInfo = {
      ...state.userInfo,
      uid: userInfo,
    }
  },
};

export default {
  namespaced: true,
  state,
  actions,
  mutations,
};
