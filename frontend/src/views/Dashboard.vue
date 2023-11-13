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
    height: 100%; /* Ensure it takes full height of its container */
}

.content {
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    height: 100%; /* Ensure it expands to the full height */
}

.timelines {
    display: flex;
    gap: 20px;
    justify-content: space-around;
    align-items: stretch;
    flex-grow: 1; /* Added to take up available space */
}

.timelines>* {
    flex: 1;
    /* Assigns equal flex-grow value to each timeline */
    min-width: 0;
    /* Prevents overflow issues in some browsers */
}

/* Responsive adjustments if necessary */
@media (max-width: 600px) {
    .timelines {
        flex-direction: column;
    }
}</style>