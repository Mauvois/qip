import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue' // PascalCase for component name
import About from '@/views/About.vue' // PascalCase for component name
import Dashboard from '@/views/Dashboard.vue'


const routes = [
    { path: '/', name: 'Home', component: Home }, // PascalCase for route name and component name
    { path: '/about', name: 'About', component: About }, // PascalCase for route name and component name
    { path: '/dashboard', name: 'Dashboard', component: Dashboard }
]

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes
})

export default router
