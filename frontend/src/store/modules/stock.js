import api from "../../api";

// initial state
const state = {
  stockList: [],
};

// actions
const actions = {
  async getStockList({commit}) {
    const stockList = await api.getStockList();
    commit("setStockList", stockList);
  },
  async getTestData({commit}, data) {
    const testData = await api.getTestData(data);
    return testData;
  },
};

// mutations
const mutations = {
  setStockList(state, stockList) {
    state.stockList = {
      ...state.stockList,
      stockList: stockList
    }
  }
};

export default {
  namespaced: true,
  state,
  actions,
  mutations,
};
