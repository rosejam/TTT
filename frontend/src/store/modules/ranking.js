import api from '../../api';

const state = {
    rankerList: [],
}

const actions = {
    async setRankerList({ commit }, numOfRank) {
        let response = null;
        try {
            response = await api.getRanking(numOfRank);
        } catch (error) {
            console.log(error);
        }
        if (response != null) {
            const promises = response.data.results.map(async (element) => {
                try {
                    const resp = await api.getUserByPk(element.id);
                    element.username = resp.username;
                } catch (error) {
                    element.username = "(알수없음)";
                }
                return element;
            });
            await Promise.all(promises);
            // response.data.results.forEach(async element => {
            //     try {
            //         const resp = await api.getUserByPk(element.id);
            //         element.username = resp.username;
            //     } catch (error) {
            //         element.username = "(알수없음)";
            //     }
            // });
        }
        commit('setRankerList', response.data.results);
    }
}

const mutations = {
    setRankerList(state, list) {
        state.rankerList = list;
    }
}

export default {
    namespaced: true,
    state,
    actions,
    mutations,
};