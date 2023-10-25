<template>
    <div class="dashboard flex">
        <Sidebar />
        <div class="flex-1">
            <h1>Dashboard</h1>
            <!-- List the fetched posts -->
            <ul v-if="posts.length">
                <li v-for="post in posts" :key="post.id">
                    <strong>{{ post.user.username }}:</strong> {{ post.content }}
                    <br>
                    <small>Posted on: {{ new Date(post.created_time).toLocaleString() }}</small>
                </li>
            </ul>
            <p v-else>No posts available</p>
        </div>
    </div>
</template>

<script>
import axios from '../axios.js';
import Sidebar from './Sidebar.vue';

export default {
    name: 'AppDashboard',
    components: {
        Sidebar
    },
    data() {
        return {
            posts: []
        };
    },
    mounted() {
        this.fetchPosts();
    },
    methods: {
        async fetchPosts() {
            try {
                const response = await axios.get('posts/');
                this.posts = response.data;
            } catch (error) {
                console.error('Failed to fetch posts:', error);
            }
        }
    }
    // Any data, computed properties, methods, etc. needed for the dashboard
};
</script>

<style scoped>
/* Styles specific to the Dashboard component */
</style>
