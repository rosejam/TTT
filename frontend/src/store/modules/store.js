import api from "../../api";

// initial state
const state = {
  storeSearchList: [],
  storeSearchTotalCount: 0,
  storeSearchCount: 0,
  storeSearchPage: "1",
  storeInfo: {
    id: "",
    name: "",
    branch: "",
    area: "",
    tel: "",
    address: "",
    lat: 0.0,
    lng: 0.0,
    categories: [],
    review_cnt: 0,
    total_score: 0,
  },
  storesByReview: [],
  storesByReviewNum: 10,
  recommendStores: [], // Stores를 담은 list
  recommendStoresNum: [],
};

// actions
const actions = {
  async getStores({ commit }, params) {
    const append = params.append;
    const resp = await api.getStores(params);
    const totalCount = resp.data.count;
    if (resp.data.results.length > 0) {
      const stores = resp.data.results.map((d) => ({
        id: d.id,
        name: d.store_name,
        branch: d.branch,
        area: d.area,
        tel: d.tel,
        address: d.address,
        lat: d.latitude,
        lng: d.longitude,
        categories: d.category_list,
        review_cnt: d.review_cnt,
        total_score: d.total_score
      }));

      if (append) {
        commit("addStoreSearchList", stores);
        commit("setStoreSearchCount", state.storeSearchCount + resp.data.results.length);
      } else {
        commit("setStoreSearchList", stores);
        commit("setStoreSearchTotalCount", totalCount);
        commit("setStoreSearchCount", resp.data.results.length);
      }
      commit("setStoreSearchPage", resp.data.next);
    } else {
      commit("setStoreSearchList", []);
    }
  },
  async getStoreInfo({ commit }, id) {
    const resp = await api.getStoreInfo(id);
    const storeInfo = resp.data;
    commit("setStoreInfo", storeInfo);
    if (state.storeInfo.review_cnt > 0) {
      state.storeInfo.total_score /= state.storeInfo.review_cnt;
    }
  },
  async getMenus({ commit }, store_id) {
    const resp = await api.getMenusByStore(store_id);
    const menus = resp.data.results;
    return menus;
  },
  async getReviews({ commit }, { id, page }) {
    const resp = await api.getReviewsByStore(id, page);
    const reviews = resp.data.results;
    return reviews;
  },
  async setRecommendStores({ commit }, { userPk, index }) {
    try {
      commit('setRecommendStoresNum', { idx: index, num: 10 });
      if (index == state.recommendStores.length) {
        commit('addRecommendStores', []);
      } else {
        commit('setRecommendStores', { idx: index, newStores: [] });
      }
      let resp;
      let data;
      if (index == 0) {
        resp = await api.getKNNRecommendByUserPk(userPk, state.recommendStoresNum[index]);
        data = JSON.parse(resp.data).slice(-10).map(review => {
          return review;
        })
      } else if (index == 1) {
        resp = await api.getAgeGenderRecommendByUserPk(userPk, state.recommendStoresNum[index]);
        data = JSON.parse(resp.data).slice(-10).map(review => {
          let newReview = {};
          newReview.store = review.id;
          newReview.score = review.score;
          return newReview;
        })
      }
      let newStores = []
      data.forEach(review => { // 뒤에 10개만 뽑아내고 이전거에 붙임 -> 10개 단위로 늘어나게 하기 위함
        newStores.push(review);
      })
      commit('setRecommendStores', { idx: index, newStores: newStores });
    } catch (error) {
      return error;
    }
  },
  async loadMoreRecommendStores({ commit }, { userPk, index }) {
    try {
      commit('setRecommendStoresNum', { idx: index, num: state.recommendStoresNum[index] + 10 });
      let resp;
      let data;
      if (index == 0) {
        resp = await api.getKNNRecommendByUserPk(userPk, state.recommendStoresNum[index]);
        data = JSON.parse(resp.data).slice(-10).map(review => {
          return review;
        })
      } else if (index == 1) {
        resp = await api.getAgeGenderRecommendByUserPk(userPk, state.recommendStoresNum[index]);
        data = JSON.parse(resp.data).slice(-10).map(review => {
          let newReview = {};
          newReview.store = review.id;
          newReview.score = review.score;
          return newReview;
        })
      }
      let newStores = state.recommendStores[index]; // deep copy를 하기 위하여 string으로 만들고 다시 객체로 만듦
      data.forEach(review => { // 뒤에 10개만 뽑아내고 이전거에 붙임 -> 10개 단위로 늘어나게 하기 위함
        newStores.push(review);
      })
      commit('setRecommendStores', { idx: index, newStores: newStores });
    } catch (error) {
      return error;
    }
  }
};

// mutations
const mutations = {
  setStoreSearchList(state, stores) {
    state.storeSearchList = stores.map((s) => s);
  },
  addStoreSearchList(state, stores) {
    state.storeSearchList = state.storeSearchList.concat(stores);
  },
  setStoreSearchPage(state, url) {
    state.storeSearchPage = new URL(url).searchParams.get("page");
  },
  setStoreInfo(state, storeInfo) {
    state.storeInfo = storeInfo;
  },
  setStoresByReview(state, storesByReview) {
    state.storesByReview = storesByReview;
  },
  setStoresByReviewNum(state, num) {
    state.storesByReviewNum = num;
  },
  setRecommendStores(state, { idx, newStores }) {
    state.recommendStores.splice(idx, 1, newStores);
  },
  addRecommendStores(state, newStores) {
    state.recommendStores.push(newStores);
  },
  setRecommendStoresNum(state, { idx, num }) {
    state.recommendStoresNum.splice(idx, 1, num);
  },
  setStoreSearchTotalCount(state, count) {
    state.storeSearchTotalCount = count;
  },
  setStoreSearchCount(state, count) {
    state.storeSearchCount = count;
  },
};

export default {
  namespaced: true,
  state,
  actions,
  mutations,
};
