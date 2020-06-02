import api from "../../api";

// initial state
const state = {
  userInfo: {
    email: null,
  },
};

// actions
const actions = {
  async setUser({ commit }) {
    const userInfo = await api.getUserInfo();
    commit("setUserInfo", userInfo);
  },
  async signUp({ commit }, user) {
    await api.signUp(user);
  },
  async regUserInfo({ commit }, user) {
    await api.regUserInfo(user);
  },
  async resetPw({ commit }, params) {
    const email = params.email;
    const csrftoken = params.csrftoken;
    await api.resetPw(email, csrftoken);
  },
  async editUser({ commit }, { pk, user }) {
    await api.editUserByPk(pk, user);
    const userInfo = await api.getUserInfoByPk(pk);
    const response = await api.getUserByPk(pk);
    userInfo.username = response.username;
    commit("setUserInfo", userInfo);
  },
  async editUserInfo({ commit }, { pk, userInfo }) {
    await api.editUserInfoByPk(pk, userInfo);
    let response = await api.getUserInfoByPk(pk);
    response.username = state.userInfo.username;
    commit("setUserInfo", response);
  },
  async getUserInfoById({ commit }, id) {
    try {
      const resp = await api.getUserById(id);
      const pk = resp[0].id;
      const response = await api.getUserInfoByPk(pk);
      return response;
    } catch (error) {
      return error;
    }
  },
};

// mutations
const mutations = {
  setUserInfo(state, userInfo) {
    // state.userInfo = {
    //   ...state.userInfo,
    //   username: userInfo.username,
    //   gender: userInfo.gender,
    //   img: userInfo.img,
    //   age: new Date().getFullYear() - userInfo.born_year,
    //   introduction: userInfo.introduction,
    //   playing: userInfo.playing,
    //   playingQuest: userInfo.playingQuest,
    //   completedQuests: userInfo.completedQuests,
    //   quest_finished_time: userInfo.quest_finished_time,
    //   exp: userInfo.exp,
    // };
    state.userInfo = {
      ...state.userInfo,
      email: userInfo,
    }
  },
};

export default {
  namespaced: true,
  state,
  actions,
  mutations,
};
