import { createStore } from 'vuex';
import axios from 'axios';

export default createStore({
  state: {
    user: null,
    token: localStorage.getItem('token') || null,  // Get the token from local storage
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    },
    setToken(state, token) {
      state.token = token;
      localStorage.setItem('token', token);  // Store the token in local storage

      // Optionally set the token to the axios headers for future requests
      if (token) {
        axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
      } else {
        delete axios.defaults.headers.common['Authorization'];
        localStorage.removeItem('token');  // Remove the token from local storage
      }
    },
  },
  actions: {
    async login({ commit }, credentials) {
      try {
        const response = await axios.post(
          `${import.meta.env.VITE_APP_BACKEND_URL}login/`,
          credentials
        );
        commit('setUser', response.data.user);
        commit('setToken', response.data.token);
      } catch (error) {
        console.error('An error occurred during login:', error);
        throw error;
      }
    },
    async signup({ dispatch }, credentials) {  // New signup action
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
    logout({ commit }) {  // New logout action
      commit('setUser', null);
      commit('setToken', null);
    },
  },
});