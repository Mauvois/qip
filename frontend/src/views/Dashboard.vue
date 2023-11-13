<template>
    <div class="dashboard">
        <Sidebar />
        <div class="content">
            <!-- <h1>Dashboard</h1> -->
            <div v-if="posts.length" class="timelines">
                <Timeline :posts="posts" timescale="hour" />
                <Timeline :posts="posts" timescale="day" />
                <Timeline :posts="posts" timescale="week" />
                <Timeline :posts="posts" timescale="month" />
            </div>
            <p v-else>No posts available</p>
        </div>
    </div>
</template>

<script>
import axios from '@/axios.js';
import Sidebar from './Sidebar.vue';
import Timeline from './Timeline.vue';

export default {
    name: 'AppDashboard',
    components: {
        Sidebar,
        Timeline
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
};
</script>

<style scoped>
.dashboard {
    display: flex;
}

.content {
    flex-grow: 1;
    display: flex;
    flex-direction: column;
}

.timelines {
    display: flex;
    gap: 20px; /* Adjust the space between timelines */
}

/* Responsive adjustments if necessary */
@media (max-width: 600px) {
    .timelines {
        flex-direction: column;
    }
}
</style>