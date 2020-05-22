import axios from "axios";
axios.defaults.withCredentials = true;
// axios.defaults.xsrfCookieName = 'csrftoken';
// axios.defaults.xsrfHeaderName = 'X-CSRFToken';
// const apiUrl = "/api";
const apiUrl = process.env.VUE_APP_API_URL;

export default {
  // 가게 관련 api
  getStores(params) {
    return axios.get(`${apiUrl}/api/stores`, {
      params,
    });
  },
  getStoreInfo(id) {
    return axios.get(`${apiUrl}/api/stores/${id}`);
  },
  getReviewsByStore(id, page) {
    return axios.get(`${apiUrl}/api/reviews?&store_id=${id}&page=${page}`);
  },
  getMenusByStore(store_id) {
    // menus?store_id=
    return axios.get(`${apiUrl}/api/menus?store_id=${store_id}`);
  },
  async updateTotalScoreReviewCnt(id, storeName, totalScore, reviewCnt) {
    return axios.put(`${apiUrl}/api/stores/${id}`, {
      store_name: storeName,
      review_cnt: reviewCnt,
      total_score: totalScore,
    });
  },

  // 유저 관련 api
  async login(email, password) {
    const response = await axios.post(
      `${apiUrl}/rest-auth/login/`,
      {
        email: email,
        password: password,
      }
      // {
      //   withCredentials: true
      // }
    );
    const userInfo = await axios.get(`${apiUrl}/rest-auth/user/`);
    return userInfo.data;
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

  // 리뷰 관련 api
  async submitReview(review) {
    const response = await axios.post(`${apiUrl}/api/reviews`, review, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });
    if (response.status == 201) {
      const storeInfo = await this.getStoreInfo(review.get('store'));
      let newTotalScore = storeInfo.data.total_score + parseFloat(review.get('score'));
      const updataRes = await this.updateTotalScoreReviewCnt(
        review.get('store'),
        storeInfo.data.store_name,
        newTotalScore,
        storeInfo.data.review_cnt + 1
      );
    }
    return response;
  },
  async modifyReview(id, review) {
    const prevReview = await axios.get(`${apiUrl}/api/reviews/${id}`);
    const response = await axios.put(`${apiUrl}/api/reviews/${id}`, review, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });
    if (response.status == 200) {
      const storeInfo = await this.getStoreInfo(review.get('store'));
      let newTotalScore =
        storeInfo.data.total_score - prevReview.data.score + parseFloat(review.get('score'));
      await this.updateTotalScoreReviewCnt(
        review.get('store'),
        storeInfo.data.store_name,
        newTotalScore,
        storeInfo.data.review_cnt
      );
    }
    return response;
  },
  async deleteReview(id) {
    const prevReview = await axios.get(`${apiUrl}/api/reviews/${id}`);
    const response = await axios.delete(`${apiUrl}/api/reviews/${id}`);
    if (response.status == 204) {
      const storeInfo = await this.getStoreInfo(prevReview.data.store);
      let newTotalScore = storeInfo.data.total_score - prevReview.data.score;
      await this.updateTotalScoreReviewCnt(
        prevReview.data.store,
        storeInfo.data.store_name,
        newTotalScore,
        storeInfo.data.review_cnt - 1
      );
    }
    return response;
  },
  async getReviewsByUserPk(pk, page) {
    const response = await axios.get(`${apiUrl}/api/reviews?user_id=${pk}&page=${page}`);
    return response;
  },

  // 추천 api
  // 사용자 리뷰 기반 KNN 알고리즘 추천
  async getKNNRecommendByUserPk(pk, n) {
    const response = await axios.get(`${apiUrl}/api/knn?user_id=${pk}&n=${n}`)
    return response;
  },

  // 사용자 나이 +-5살, 같은 성별 추천
  async getAgeGenderRecommendByUserPk(pk, n) {
    const response = await axios.get(`${apiUrl}/api/userbase?user_id=${pk}&n=${n}`);
    return response;
  },

  // 퀘스트 관련 api
  getMainQuests(params) {
    const ret = axios.get(`${apiUrl}/api/mainquests`, {
      params
    });
    return ret;
  },
  getMainQuestInfo(main_quest_id) {
    return axios.get(`${apiUrl}/api/mainquests/${main_quest_id}`);
  },
  getSubQuests(main_quest_id) {
    return axios.get(`${apiUrl}/api/subquests?main_quest_id=` + main_quest_id);
  },
  getSubQuestInfo(sub_quest_id) {
    return axios.get(`${apiUrl}/api/subquests/${sub_quest_id}`);
  },
  async completeQuest(completedQuest) {
    await axios.post(`${apiUrl}/api/completedquests`, {
      user_id: completedQuest.user_id,
      sub_quest_id: completedQuest.sub_quest_id,
      quest_finished_time: completedQuest.quest_finished_time,
    });
  },
  getCompletedQuestByUser(user_id) {
    return axios.get(`${apiUrl}/api/completedquests?user_id=` + user_id);
  },

  // 랭킹 관련 api
  getRanking(numOfRank) {
    return axios.get(`${apiUrl}/api/userinfo?n=${numOfRank}`);
  },
  getRankingByUserPk(pk) {
    return axios.get(`${apiUrl}/api/myranking?user_id=${pk}`)
  }
};
