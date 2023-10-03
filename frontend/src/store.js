import { createStore } from 'vuex';
import axios from 'axios';

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
    async login({ commit }, credentials) {
      try {
        const response = await axios.post(
          `${process.env.VUE_APP_BACKEND_URL}your-login-endpoint/`, // replace your login endpoint by the actual endpoint
          credentials
        );
        commit('setUser', response.data.user);
      } catch (error) {
        console.error('An error occurred during login:', error);
        throw error;
      }
    },
  },
});