import api from "../../api";

// initial state
const state = {
};

// actions
const actions = {
  async getStockData({commit}, data) {
    console.log('stock.js.....', data);
    const stockData = await api.getStockData(data);
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
