// mainapp/static/js/main.js
const { createApp, ref } = Vue;

createApp({
    setup() {
        const message = ref('Hello from Vue.js!');
        return {
            message
        };
    }
}).mount('#app');