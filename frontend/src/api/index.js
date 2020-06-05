import axios from "axios";
axios.defaults.withCredentials = true;
// const apiUrl = 'http://3.34.96.193:8000'
const apiUrl = 'http://localhost:8000'

export default {
  // 주식 정보 관련 api

  // 주식 리스트
  async getStockList() {
    const ret = await axios.get(`${apiUrl}/api/stockinfo`);
    const stockList = ret.data.results;
    return stockList;
  },

  // 테스트 결과
  async getTestData(data) {

    const testData = await axios.post(`${apiUrl}/rebalance/`, {
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

  // 유저 정보
  async getUserInfo(uid) {
    console.log('index.js....uid>>', uid);
    const result = await axios.get(`${apiUrl}/api/portfolio?uid=`+uid);

    console.log('index.js...result>>', result);

    let userInfo = {
      uid: uid,
      portfolio: "포트폴리오~~"
    };

    return userInfo;
  },

  // 포트폴리오 저장
  async postPortfolio(data) {

    let stock = "";
    let portfolio1 = "";
    let portfolio2 = "";
    let portfolio3 = "";

    for (let i = 0; i < data.stocks.length; i++) {
      const stockinfo = data.stocks[i];
      stock += stockinfo.stock + '|';
      portfolio1 += stockinfo.portfolio1 + '|';
      portfolio2 += stockinfo.portfolio2 + '|';
      portfolio3 += stockinfo.portfolio3 + '|';
    }

    stock = stock.substring(0, stock.length-1);
    portfolio1 = portfolio1.substring(0, portfolio1.length-1);
    portfolio2 = portfolio2.substring(0, portfolio2.length-1);
    portfolio3 = portfolio3.substring(0, portfolio3.length-1);

    console.log('api save...', {
      uid: data.uid,
      name: data.name,
      startYear: data.startYear,
      startMonth: data.startMonth,
      endYear: data.endYear,
      endMonth: data.endMonth,
      initAmount: data.initAmount,
      period: data.period,
      rebalancing: data.rebalancing,
      stock: stock,
      portfolio1: portfolio1,
      portfolio2: portfolio2,
      portfolio3: portfolio3,
    })


    await axios.post(`${apiUrl}/api/portfolio`, {
      uid: data.uid,
      name: data.name,
      startYear: data.startYear,
      startMonth: data.startMonth,
      endYear: data.endYear,
      endMonth: data.endMonth,
      initAmount: data.initAmount,
      period: data.period,
      rebalancing: data.rebalancing,
      stock: stock,
      portfolio1: portfolio1,
      portfolio2: portfolio2,
      portfolio3: portfolio3,
    });
  }
};
