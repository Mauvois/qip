import { createStore } from 'vuex';
import axios from 'axios';

export default createStore({
  state: {
    user: null,
    token: null,
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    },
    setToken(state, token) {
      state.token = token;
      // Optionally set the token to the axios headers for future requests
      if (token) {
        axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
      } else {
        delete axios.defaults.headers.common['Authorization'];
      }
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
        commit('setToken', response.data.token);
      } catch (error) {
        console.error('An error occurred during login:', error);
        throw error;
      }
    },
  },
});