import api from "../../api";

// initial state
const state = {
  questSearchList: [],
  questSearchPage: "1",
  questSearchCount: 0,
  questSearchTotalCount: 0,
  mainQuestInfo: {
    id: "",
    main_quest: "",
    categories: []
  },
  questSuccessFlag: false,
  prevExp: 0,
  newExp: 0,
};

// actions
const actions = {
  // 메인퀘스트 목록 가져오기
  async getMainQuests({ commit }, params) {
    const append = params.append;
    const resp = await api.getMainQuests(params);
    if (resp.data.results.length > 0) {
      const mainQuests = resp.data.results.map((d) => ({
        id: d.id,
        main_quest: d.main_quest,
        categories: d.category_list,
        content: d.content,
      }));

      if (append) {
        commit("addQuestSearchList", mainQuests);
        commit("setQuestSearchCount", state.questSearchCount + resp.data.results.length);
      } else {
        commit("setQuestSearchList", mainQuests);
        commit("setQuestSearchTotalCount", resp.data.count);
        commit("setQuestSearchCount", resp.data.results.length);
      }
      if (resp.data.next != null) {
        commit("setQuestSearchPage", resp.data.next);
      }
    } else {
      commit("setQuestSearchList", []);
    }
  },
  // 메인퀘스트 상세정보 가져오기
  async getMainQuestInfo({ commit }, main_quest_id) {
    const resp = await api.getMainQuestInfo(main_quest_id);
    const mainQuestInfo = resp.data;
    commit("setMainQuestInfo", mainQuestInfo);
  },
  // 서브퀘스트 목록 가져오기
  async getSubQuests({ commit }, main_quest_id) {
    const resp = await api.getSubQuests(main_quest_id);
    const subQuests = resp.data.results;
    return subQuests;
  },
  // 서브퀘스트 상세정보 가져오기
  async getSubQuestInfo({ commit }, sub_quest_id) {
    const subQuestInfo = await api.getSubQuestInfo(sub_quest_id).data.results;
    return subQuestInfo;
  },
  // 완료된 퀘스트 목록으로 옮기기
  async completeQuest({ commit }, completedQuest) {
    await api.completeQuest(completedQuest);
  }
};

// mutations
const mutations = {
  setQuestSearchList(state, quests) {
    state.questSearchList = quests.map((s) => s);
  },
  addQuestSearchList(state, quests) {
    state.questSearchList = state.questSearchList.concat(quests);
  },
  setQuestSearchPage(state, url) {
    state.questSearchPage = new URL(url).searchParams.get("page");
  },
  setMainQuestInfo(state, mainQuestInfo) {
    state.mainQuestInfo = mainQuestInfo;
  },
  setQuestSearchCount(state, count) {
    state.questSearchCount = count;
  },
  setQuestSearchTotalCount(state, count) {
    state.questSearchTotalCount = count;
  },
  setQuestSuccessFlag(state, flag) {
    state.questSuccessFlag = flag;
  },
  setPrevExp(state, prevExp) {
    state.prevExp = prevExp;
  },
  setNewExp(state, newExp) {
    state.newExp = newExp;
  },
};

export default {
  namespaced: true,
  state,
  actions,
  mutations,
};
