const state = {
    storeName: "",
    locationName: "",
    // priceLow: null,
    // priceHigh: null,
    category: "",
    ////// 퀘스트 관련
    questName: "",
    Qcategory: "",
    notByClick: false,
  };
  
  // actions
  const actions = {
  };
  
  // mutations
  const mutations = {
    setStoreName(state, storeName) {
      state.storeName = storeName;
    },
    setLocationName(state, locationName) {
      state.locationName = locationName;
    },
    setCategory(state, category) {
      state.category = category;
    },
    setQuestName(state, questName) {
      state.questName = questName;
    },
    setQCategory(state, Qcategory) {
      state.Qcategory = Qcategory;
    },
    setNotByClick(state, notByClick) {
      state.notByClick = notByClick;
    },
  };
  
  export default {
    namespaced: true,
    state,
    actions,
    mutations,
  };
  