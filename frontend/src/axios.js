import axios from 'axios';

const instance = axios.create({
  baseURL: 'https://api.example.com',

});

export const setAuthToken = token => {
  if (token) {
    instance.defaults.headers.common['Authorization'] = 'Bearer ' + token;
  } else {
    delete instance.defaults.headers.common['Authorization'];
  }
};

export default instance;