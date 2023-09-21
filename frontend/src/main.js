import { createApp } from 'vue';
import axios from '@/axios'; // adjust the import path according to your folder structure
import App from '@/App.vue'; // adjust the import path according to your folder structure
import '@/assets/tailwind.css';

const app = createApp(App);

app.config.globalProperties.$axios = axios;
app.mount('#app');