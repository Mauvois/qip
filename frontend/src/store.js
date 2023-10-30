import { createStore } from 'vuex';
import axios from '@/axios.js';


export default createStore({
  state: {
    user: null
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    }
  },
  actions: {
    async login({ commit }, credentials) {
      try {
        const response = await axios.post(
          `${import.meta.env.VITE_APP_BACKEND_URL}login/`,
          credentials,
          { withCredentials: true }  // Make sure cookies are sent and received
        );
        commit('setUser', response.data.user);
      } catch (error) {
        console.error('An error occurred during login:', error);
        throw error;
      }
    },
    async signup({ dispatch }, credentials) {
      try {
        await axios.post(
          `${import.meta.env.VITE_APP_BACKEND_URL}signup/`,
          credentials
        );
        // Login after successful signup
        await dispatch('login', credentials);
      } catch (error) {
        console.error('An error occurred during signup:', error);
        throw error;
      }
    },
    logout({ commit }) {
      commit('setUser', null);
    }
  }
});