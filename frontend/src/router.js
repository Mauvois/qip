import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue' // PascalCase for component name
import About from '@/views/About.vue' // PascalCase for component name

const routes = [
    { path: '/', name: 'Home', component: Home }, // PascalCase for route name and component name
    { path: '/about', name: 'About', component: About } // PascalCase for route name and component name
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL), // Corrected BASE_URL
    routes
})

export default router
