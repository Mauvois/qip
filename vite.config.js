import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'  // ES module syntax

// https://vitejs.dev/config/
export default defineConfig({
    root: 'frontend',  // this sets the root directory for the frontend
    plugins: [vue()],
    css: {
        postcss: {
            plugins: [
                require('tailwindcss'),
                require('autoprefixer')
            ]
        }
    },
    resolve: {
        alias: {
            // Considering the root, the alias should now be set relative to the frontend directory
            "@": path.resolve(__dirname, "frontend/src"),
        },
    },
    server: {
        proxy: {
            '/api': 'http://localhost:8000',  // assuming your Django API endpoints start with "/api"
        },
    },
    build: {
        outDir: '../dist' // if you want build files to be outside of frontend directory
    }
})