import axios from 'axios';

const instance = axios.create({
  baseURL: 'https://api.example.com',
  // other configurations
});

export default instance;