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
    async signup({ commit, dispatch }, credentials) {
      try {
        // The POST request to the signup endpoint
        await axios.post(
          `${import.meta.env.VITE_APP_BACKEND_URL}signup/`,
          {
            username: credentials.username,
            email: credentials.email,
            password: credentials.password,
            first_name: credentials.first_name,
            last_name: credentials.last_name
          }
        );
        // Dispatch the login action with the username and password
        await dispatch('login', {
          username: credentials.username,
          password: credentials.password
        });
        // Redirection will be handled in Home.vue after this action completes
      } catch (error) {
        console.error('An error occurred during signup:', error);
        throw error;
      }
    },
  }
});