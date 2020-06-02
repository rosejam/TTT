import api from "../../api";

// initial state
const state = {
};

// actions
const actions = {
  async getTestData({commit}, data) {
    const stockData = await api.getTestData(data);
    return stockData;
  }
};

// mutations
const mutations = {
};

export default {
  namespaced: true,
  state,
  actions,
  mutations,
};
