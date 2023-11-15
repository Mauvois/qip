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
                <Timeline :posts="posts" timescale="year" />
                <Timeline :posts="posts" timescale="decade" />
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
            posts: [],
            socket: null,
        };
    },
    mounted() {
        this.connectWebSocket();
    },
    beforeDestroy() {
        if (this.socket) {
            this.socket.close();
        }
    },
    mounted() {
        this.fetchPosts();
    },
    methods: {
        connectWebSocket() {
            this.socket = new WebSocket('ws://localhost:8000/ws/some_path/');
            this.socket.onmessage = (event) => {
                let data = JSON.parse(event.data);
                this.posts = data.message;
                // update your posts or handle the message
            };
            this.socket.onclose = function (e) {
                console.error('Chat socket closed unexpectedly');
            };
        },
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
    height: 100%;
    /* Ensure it takes full height of its container */
}

.content {
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    height: 100%;
    /* Ensure it expands to the full height */
}

.timelines {
    display: flex;
    justify-content: stretch;
    /* Adjust to stretch the child elements */
    align-items: stretch;
    flex-grow: 1;
    width: 100%;
    /* Ensure full width */

    /* Added styles */
    >* {
        flex: 1;
        /* Give equal width to all child elements */
    }
}

.timelines>*:nth-child(odd) {
    background-color: #f5f5f5;
    /* Very light grey for odd timelines */
}

.timelines>*:nth-child(even) {
    background-color: #eae9e9;
    /* Light grey for even timelines */
}

/* Responsive adjustments if necessary */
@media (max-width: 600px) {
    .timelines {
        flex-direction: column;
    }
}
</style>