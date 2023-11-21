<template>
    <div class="sidebar bg-slate-700 lg:w-1/4 md:w-1/3 w-full h-screen p-6 flex flex-col justify-between">
        <div class="h-3/4 flex flex-col space-y-4 justify-between">
            <div class="mb-6">
                <h1 class="text-white text-4xl mb-4">QIP</h1>
            </div>

            <div class="mb-2">
                <input type="text" placeholder="Search..."
                    class="sidebar-search-bar w-full px-3 py-2 bg-white rounded-md" />

            </div>

            <div class="mb-2">
                <h2 class="text-white mb-2">Tags</h2>
                <div class="overflow-y-auto mb-6">
                    <!-- options list content -->
                </div>
            </div>

            <div class="mb-6">
                <h2 class="text-white mb-6">◎</h2>
                <div class="overflow-y-auto mb-6">
                    <!-- filters list content -->
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

            </div>
        </div>
    </div>
    <div class="block lg:hidden fixed bottom-0 left-0 w-full p-2.5 bg-gray-800 z-50">
        <input type="text" placeholder="Search..." class="w-full px-2.5 py-2 rounded-lg border-0" />
    </div>
</template>
  




<script>
import { mapState } from 'vuex';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import axios from '@/axios.js';

export default {
    name: 'Sidebar',
    components: {
        FontAwesomeIcon
    },
    data() {
        return {
            showMenu: false,
            // Removed isCollapsed
        };
    },
    computed: {
        ...mapState(['user']),
        // Removed toggleIcon
    },
    methods: {
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
        },
        // Removed toggleSidebar method
    },
};
</script>


<style scoped>
@media (max-width: 600px) {
    .sidebar {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: auto;
        padding-top: 10px;
        /* Adjust as needed */
    }

    .sidebar .absolute {
        position: relative;
        top: 0;
        left: 0;
        right: auto;
        bottom: auto;
        padding: 10px 0;
        /* Adjust as needed */
    }

    .sidebar-search-bar {
        display: none;
    }
}
</style>
