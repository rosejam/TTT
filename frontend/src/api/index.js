import axios from "axios";
axios.defaults.withCredentials = true;
const apiUrl = 'http://3.34.96.193:8000'
// const apiUrl = 'http://localhost:8000'

export default {
  // 주식 정보 관련 api

  // 현재 주식 리스트 데이터 받아옴
  async getStockList() {
    const ret = await axios.get(`${apiUrl}/api/stockinfo`);
    const stockList = ret.data.results;
    return stockList;
  },

  // 테스트 결과 데이터 받아옴
  async getTestData(data) {

    let testData = await axios.post(`${apiUrl}/rebalance/`, {
      startYear: data.startYear,
      startMonth: data.startMonth,
      endYear: data.endYear,
      endMonth: data.endMonth,
      initAmount: data.initAmount,
      period: data.period,
      rebalancing: data.rebalancing,
      stocks: data.stocks
    });

    return testData.data;
  },

  // 유저 관련 api
  async getUserInfo() {
    let userInfo = localStorage.getItem("user_token");
    return userInfo;
  },
};
