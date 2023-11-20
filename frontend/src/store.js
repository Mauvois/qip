import { createStore } from 'vuex';
import axios from '@/axios.js';

export default createStore({
  state: {
    user: null,
    isSettingsVisible: false,
    isProfileVisible: false,
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    },
    clearUser(state) {
      state.user = null;
    },
    toggleSettingsVisibility(state) { // New mutation to toggle the visibility of settings
      state.isSettingsVisible = !state.isSettingsVisible;
    },
    toggleProfileVisibility(state) {
      state.isProfileVisible = !state.isProfileVisible;
    }
  },
  actions: {
    async initializeAuthenticationState({ commit }) {
      try {
        const response = await axios.get(`${import.meta.env.VITE_APP_BACKEND_URL}check_session/`, { withCredentials: true });
        commit('setUser', response.data.user);
      } catch (error) {
        console.error('Error during session check:', error);
        commit('clearUser');
      }
    },
    async login({ commit }, credentials) {
      try {
        const response = await axios.post(
          `${import.meta.env.VITE_APP_BACKEND_URL}login/`,
          credentials,
          { withCredentials: true }
        );
        commit('setUser', response.data.user);
      } catch (error) {
        console.error('An error occurred during login:', error);
        throw error;
      }
    },
    async signup({ commit, dispatch }, credentials) {
      try {
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
        await dispatch('login', {
          username: credentials.username,
          password: credentials.password
        });
      } catch (error) {
        console.error('An error occurred during signup:', error);
        throw error;
      }
    },
    async logout({ commit }) {
      try {
        await axios.post(`${import.meta.env.VITE_APP_BACKEND_URL}logout/`, {}, { withCredentials: true });
        commit('clearUser');
      } catch (error) {
        console.error('An error occurred during logout:', error);
      }
    },
    // No changes needed in existing actions
  }
});