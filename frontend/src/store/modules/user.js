import api from "../../api";

// initial state
const state = {
  userInfo: {
    pk: "",
    username: "",
    gender: "",
    age: "",
    img: "",
    introduction: "",
    playing: false,
    playingQuest: null,
    completedQuests: [],
    quest_finished_time: "",
    exp: 0,
  },
  isAdmin: false,
};

// actions
const actions = {
  async login({ commit }, params) {
    const email = params.email;
    const passwd = params.passwd;
    const response = await api.login(email, passwd);
    commit("setPk", response.pk);
    sessionStorage.setItem("pk", response.pk);
    let userInfo = await api.getUserInfoByPk(response.pk);
    userInfo.username = response.username;

    // 내가 완료한 퀘스트 목록 넣어줌
    const completedQuests = await api.getCompletedQuestByUser(response.pk);
    const completedQuestInfo = completedQuests.data.results;
    userInfo.completedQuests = [];
    for (let i = 0; i < completedQuestInfo.length; i++) {
      const questId = completedQuestInfo[i].sub_quest_id;
      const response = await api.getSubQuestInfo(questId);
      const quest = response.data;
      quest.quest_finished_time = completedQuestInfo[i].quest_finished_time;
      userInfo.completedQuests = [];
      userInfo.completedQuests.push(quest);
    }

    // 내가 진행중인 퀘스트 넣어줌
    if (userInfo.playing) {
      let playingQuest = await api.getSubQuestInfo(userInfo.playingQuest);
      userInfo.playingQuest = playingQuest.data;
    }
    commit("setUserInfo", userInfo);
  },
  async logout() {
    await api.logout();
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
  async getReviewsByPkPage({ commit }, { pk, page }) {
    const resp = await api.getReviewsByUserPk(pk, page);
    const reviews = resp;
    return reviews;
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

    // userInfo.playingQuest 기존 : subQuest pk -> subQuest 객체 로바꾸기
    let result = await api.getSubQuestInfo(response.playingQuest);
    let playingQuest = result.data;
    response.playingQuest = playingQuest;

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
  setPk(state, pk) {
    state.userInfo.pk = pk;
  },
  setUserInfo(state, userInfo) {
    state.userInfo = {
      ...state.userInfo,
      username: userInfo.username,
      gender: userInfo.gender,
      img: userInfo.img,
      age: new Date().getFullYear() - userInfo.born_year,
      introduction: userInfo.introduction,
      playing: userInfo.playing,
      playingQuest: userInfo.playingQuest,
      completedQuests: userInfo.completedQuests,
      quest_finished_time: userInfo.quest_finished_time,
      exp: userInfo.exp,
    };
  },
  setIsAdmin(state, isAdmin) {
    state.isAdmin = isAdmin;
  },
  setPlayingQuest(state, playingQuest) {
    state.playingQuest = {
      ...state.playingQuest,
      id: playingQuest.id,
      main_quest_id: playingQuest.main_quest_id,
      sub_quest: playingQuest.sub_quest,
      exp: playingQuest.exp,
      http_url: playingQuest.http_url,
      search_condition: playingQuest.search_condition,
      search_keyword: playingQuest.search_keyword,
    };
  },
};

export default {
  namespaced: true,
  state,
  actions,
  mutations,
};
