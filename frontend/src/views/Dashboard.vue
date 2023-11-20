<template>
    <div class="dashboard">
        <Sidebar @show-settings="handleShowSettings" />
        <div class="content">
            <!-- Content -->
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
        <Settings v-if="isSettingsVisible" />
        <Profile v-if="isProfileVisible" />
    </div>
</template>


<script>
import axios from '@/axios.js';
import Sidebar from './Sidebar.vue';
import Timeline from './Timeline.vue';
import Settings from './Settings.vue';
import Profile from './Profile.vue';

export default {
    name: 'AppDashboard',
    components: {
        Sidebar,
        Timeline,
        Settings,
        Profile
    },
    data() {
        return {
            posts: [],
            socket: null,
        };
    },
    computed: {
        isSettingsVisible() {
            return this.$store.state.isSettingsVisible;
        },
        isProfileVisible() {
            return this.$store.state.isProfileVisible;
        }
    },
    mounted() {
        this.connectWebSocket();
        this.fetchPosts();
    },
    beforeDestroy() {
        if (this.socket) {
            this.socket.close();
        }
    },
    methods: {
        connectWebSocket() {
            this.socket = new WebSocket('ws://localhost:8000/ws/some_path/');
            this.socket.onmessage = (event) => {
                let data = JSON.parse(event.data);
                this.posts = data.message;
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
        },
        handleShowSettings() {
            this.$store.commit('toggleSettingsVisibility');
            console.log('Settings button clicked!');
        }
    }
};
</script>

<style scoped>
.dashboard {
    display: flex;
    height: 100%;
    flex-direction: row;
    /* Horizontal layout by default */
}

.content {
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    height: 100%;
}

.timelines {
    display: flex;
    justify-content: stretch;
    align-items: stretch;
    flex-grow: 1;
    width: 100%;

    >* {
        flex: 1;
    }
}

.timelines>*:nth-child(odd) {
    background-color: #f5f5f5;
}

.timelines>*:nth-child(even) {
    background-color: #eae9e9;
}

@media (max-width: 600px) {
    .dashboard {
        flex-direction: column;
        /* Vertical layout for small screens */
    }

    .dashboard>.sidebar {
        order: -1;
        /* Sidebar on top */
        height: 10%;
        /* Sidebar takes up 12% of the screen height */
    }

    .dashboard>.content {
        height: 88%;
        /* Remaining content takes up 88% of the screen height */
    }

    .timelines {
        flex-direction: column;
        /* Adjust timelines for small screens */
    }
}</style>