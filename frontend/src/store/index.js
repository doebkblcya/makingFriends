import { createStore } from 'vuex';

export default createStore({
  state: {
    user: null,
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    },
  },
  actions: {
    fetchUser({ commit }) {
      axios.get('/users/')
        .then(response => {
          commit('setUser', response.data);
        });
    },
  },
  getters: {
    getUser: (state) => state.user,
  },
});
