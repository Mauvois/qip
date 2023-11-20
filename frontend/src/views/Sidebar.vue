<template>
    <div
        :class="['sidebar', isCollapsed ? 'w-10' : 'w-55', 'bg-slate-700', 'h-screen', 'p-6', 'flex', 'flex-col', 'justify-between']">

        <div class="h-3/4 flex flex-col space-y-4 justify-between">
            <div class="mb-6">
                <h1 class="text-white text-4xl mb-4">QIP</h1>
            </div>
            <div class="mb-2">
                <input type="text" placeholder="Search..." class="w-full px-3 py-2 bg-white rounded-md" />
            </div>

            <div class="mb-2">
                <h2 class="text-white mb-2">Tags</h2>
                <div class="options-list overflow-y-auto mb-6">
                    <!-- Options items here -->
                </div>
            </div>

            <div class="mb-6 calendars">
                <h2 class="text-white mb-6">◎</h2>
                <div class="filters-list overflow-y-auto mb-6">
                    <!-- Filter options here -->
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
            isCollapsed: false, // Sidebar state
            showMenu: false,  // Hamburger menu state
        };
    },
    computed: {
        ...mapState(['user']),  // Map the user state from Vuex store to this component
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
                // Make a request to the logout endpoint
                await axios.post(`${import.meta.env.VITE_APP_BACKEND_URL}logout/`);

                // Update Vuex state if needed
                this.$store.commit('setUser', null);

                // Redirect to login or home page
                this.$router.push('/');
            } catch (error) {
                console.error('An error occurred during logout:', error);
            }
        }
    },
};
</script>


  
<style scoped>
.menu-dropdown {
    position: absolute;
    background-color: #2C2C2C;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    border-radius: 8px;
    padding: 10px;
    z-index: 1;
    /* Styling for the dropdown menu */
}

.menu-dropdown {
    display: block;
    background-color: #2C2C2C;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    border-radius: 8px;
    padding: 10px;
    z-index: 1;
    bottom: 100%;
    margin-bottom: 8px;
}

.menu-dropdown a {
    display: block;
    /* This ensures the <a> tags stack vertically */
    padding: 8px 10px;
    color: white;
    /* Set the text color to white */
    text-decoration: none;
}

.menu-dropdown a:hover {
    background-color: rgba(255, 255, 255, 0.1);
}

.menu-dropdown a:hover {
    background-color: rgba(255, 255, 255, 0.1);
}

.absolute {
    bottom: 10px;
    /* Adjust as needed for better positioning */
}
</style>