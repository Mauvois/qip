import { createApp } from 'vue';
import axios from '@/axios'; // Correct the import path according to your folder structure
import App from '@/App.vue'; // Ensure the import path is correct according to your folder structure
import '@/assets/tailwind.css';
import router from './router'

const app = createApp(App);

app.use(router); // Use the router

app.config.globalProperties.$axios = axios; // Set axios

app.mount('#app'); // Mount the app once
