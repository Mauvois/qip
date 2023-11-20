<template>
    <div
        :class="['sidebar', isCollapsed ? 'w-10' : 'w-55', 'bg-slate-700', 'h-screen', 'p-6', 'flex', 'flex-col', 'justify-between']">

        <div class="h-3/4 flex flex-col space-y-4 justify-between">
            <div class="mb-6">
                <h1 class="text-white text-4xl mb-4">QIP</h1>
            </div>

            <div class="mb-2 search-bar">
                <input type="text" placeholder="Search..." class="w-full px-3 py-2 bg-white rounded-md" />
            </div>

            <div class="mb-2">
                <h2 class="text-white mb-2">Tags</h2>
                <div class="options-list overflow-y-auto mb-6">

                </div>
            </div>

            <div class="mb-6 calendars">
                <h2 class="text-white mb-6">◎</h2>
                <div class="filters-list overflow-y-auto mb-6">

                </div>
            </div>
            <div class="mb-6">
                <p class="text-white text-lg" v-if="user">{{ user.username }}</p>
            </div>

            <div class="absolute bottom-6 left-6 right-6 flex justify-between">
                <div>
                    <button @click="toggleMenu">
                        <font-awesome-icon :icon="['fas', 'bars']" class="text-black" />
                    </button>
                    <div v-if="showMenu" class="menu-dropdown">
                        <a href="#" @click="showSettings">Settings</a>
                        <a href="#" @click="showProfile">Profile</a>
                        <router-link to="/about" class="menu-item">About</router-link>
                        <a href="#" @click="logout">Logout</a>
                    </div>
                </div>
                <div>
                    <button @click="toggleSidebar">
                        <font-awesome-icon :icon="toggleIcon" class="text-black" />
                    </button>
                </div>
            </div>
        </div>
    </div>
    <div class="search-container">
        <input type="text" placeholder="Search..." class="search-input" />
    </div>
</template>
  
<script>
import { mapState } from 'vuex';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faBars, faArrowLeft, faArrowRight } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import axios from '@/axios.js';



library.add(faBars, faArrowLeft, faArrowRight);


export default {
    name: 'Sidebar',
    components: {
        FontAwesomeIcon
    },
    data() {
        return {
            isCollapsed: false,
            showMenu: false,
        };
    },
    computed: {
        ...mapState(['user']),
        toggleIcon() {
            return this.isCollapsed ? faArrowRight : faArrowLeft;
        }
    },
    methods: {
        toggleSidebar() {
            this.isCollapsed = !this.isCollapsed;
        },
        toggleMenu() {
            this.showMenu = !this.showMenu;
        },
        showSettings() {
            this.$emit('show-settings');
        },
        showProfile() {
            this.$store.commit('toggleProfileVisibility');
        },
        async logout() {
            try {
                await axios.post(`${import.meta.env.VITE_APP_BACKEND_URL}logout/`);
                this.$store.commit('setUser', null);
                this.$router.push('/');
            } catch (error) {
                console.error('An error occurred during logout:', error);
            }
        }
    },
};
</script>


  
<style scoped>
.absolute {
    bottom: 10px;
}

.search-container {
    display: none;
}

@media (max-width: 600px) {
    .sidebar {
        height: auto;
    }

    .search-container {
        display: block;
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        padding: 10px;
        background-color: #2C2C2C;
        z-index: 1000;
    }

    .search-input {
        width: calc(100% - 20px);
        padding: 8px 10px;
        border-radius: 8px;
        border: none;

    }

    .search-bar {
        display: none;
    }
}
</style>