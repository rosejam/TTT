import api from "../../api";

// initial state
const state = {
  userInfo: {
    uid: null,
    portfolio: null,
  },
};

// actions
const actions = {
  async getUserInfo({ commit }) {
    const uid = localStorage.getItem("user");
    const userInfo = await api.getUserInfo(uid);
    commit("setUserInfo", userInfo);
  },

  async postPortfolio({commit}, data) {
    await api.postPortfolio(data);
  }
};

// mutations
const mutations = {
  setUserInfo(state, userInfo) {
    if(userInfo == null) {
      state.userInfo = {
        ...state.userInfo,
        uid: null,
        portfolio: null,
      }
    }
    else {
      state.userInfo = {
        ...state.userInfo,
        uid: userInfo.uid,
        portfolio: userInfo.portfolio,
      }
    }
  },
};

export default {
  namespaced: true,
  state,
  actions,
  mutations,
};
