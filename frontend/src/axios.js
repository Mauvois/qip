import axios from 'axios';

const instance = axios.create({
  baseURL: 'https://127.0.0.1:8000',
  withCredentials: true,  // Ensure cookies are sent with every request
});

export default instance;