import axios from "axios";
axios.defaults.withCredentials = true;
const apiUrl = 'http://3.34.96.193:8000'

export default {
  ////// 주식 정보 관련 api //////

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

  ////// 유저 관련 api //////

  // 유저 정보
  async getUserInfo(uid) {
    const ret = await axios.get(`${apiUrl}/api/portfolio?uid=` + uid);
    let portfolio = ret.data.results;

    for (let i = 0; i < portfolio.length; i++) {
      let stock = portfolio[i].stock.split("|");
      let portfolio1 = portfolio[i].portfolio1.split("|");
      let portfolio2 = portfolio[i].portfolio2.split("|");
      let portfolio3 = portfolio[i].portfolio3.split("|");
      portfolio[i].stocks = [];

      for (let j = 0; j < stock.length; j++) {
        const stockinfo = await axios.get(`${apiUrl}/api/stockinfo?code=` + stock[j]);
        const name = stockinfo.data.results[0].name + '[' + stock[j] + ']';
        portfolio[i].stocks.push({ name: name,stock: stock[j], portfolio1: portfolio1[j], portfolio2: portfolio2[j], portfolio3: portfolio3[j] });
      }

      portfolio[i].initAmount = Number(portfolio[i].initAmount);
      portfolio[i].detail = false;
      portfolio[i].testClicked = false;
      portfolio[i].del = false;
    }

    const userInfo = {
      uid: localStorage.getItem("user"),
      portfolio: portfolio,
    }

    return userInfo;
  },

  ////// 포트폴리오 관련 api //////

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
  },

  // 포트폴리오 삭제
  async deletePortfolio(id) {
    await axios.delete(`${apiUrl}/api/portfolio/` + id);
  }
};
