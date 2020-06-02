import axios from "axios";
axios.defaults.withCredentials = true;
// axios.defaults.xsrfCookieName = 'csrftoken';
// axios.defaults.xsrfHeaderName = 'X-CSRFToken';
// const apiUrl = "/api";
// const apiUrl = process.env.VUE_APP_API_URL;
const apiUrl = 'http://3.34.96.193:8000'

export default {
  // 주식 정보 관련 api
  async getTestData(data) {
    // console.log({
    //   startYear: data.startYear,
    //   startMonth: data.startMonth,
    //   endYear: data.endYear,
    //   endMonth: data.endMonth,
    //   initAmount: data.initAmount,
    //   period: data.period.code,
    //   rebalancing: data.rebalancing.code,
    //   stocks: data.stocks
    // })

    // console.log(apiUrl);

    // let stockData = await axios.post(`${apiUrl}/rebalance/`, {
    //   startYear: data.startYear,
    //   startMonth: data.startMonth,
    //   endYear: data.endYear,
    //   endMonth: data.endMonth,
    //   initAmount: data.initAmount,
    //   period: data.period.code,
    //   rebalancing: data.rebalancing.code,
    //   stocks: data.stocks
    // });

    // console.log('returned data...', stockData);

    return data.stocks[0];
  },
  // 유저 관련 api
  async getUserInfo() {
    let userInfo = localStorage.getItem("user_token");
    return userInfo;
  },
  async logout() {
    const response = await axios.post(`${apiUrl}/rest-auth/logout/`);
    return response.data;
  },
  async signUp(user) {
    const response = await axios.post(
      `${apiUrl}/rest-auth/registration/`,
      user,
      {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      }
    );
  },
  async regUserInfo(user) {
    const response = await axios.post(`${apiUrl}/api/userinfo`, user, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });
  },
  async resetPw(email, csrftoken) {
    const config = {
      headers: { HTTP_X_CSRFTOKEN: csrftoken },
    };
    const response = await axios.post(
      `${apiUrl}/accounts/password/reset/`,
      { email: email },
      config
    );
    return response.data;
  },

  // 회원 상세정보
  async getUserInfoByPk(pk) {
    const response = await axios.get(`${apiUrl}/api/userinfo/${pk}`);
    return response.data;
  },
  async editUserInfoByPk(pk, userInfo) {
    const response = await axios.patch(`${apiUrl}/api/userinfo/${pk}`, userInfo, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });
  },
  async editUserByPk(pk, user) {
    const response = await axios.patch(`${apiUrl}/api/users/${pk}`, user);
  },

  // 회원 기본정보
  async getUserByPk(pk) {
    const response = await axios.get(`${apiUrl}/api/users/${pk}`);
    return response.data;
  },
  async getUserById(id) {
    const response = await axios.get(`${apiUrl}/api/users?username=${id}`);
    return response.data.results;
  },
  async getUserByEmail(email) {
    const response = await axios.get(`${apiUrl}/api/users?email=${email}`)
    return response.data.results;
  },
};
