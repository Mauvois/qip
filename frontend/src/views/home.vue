<template>
  <div class="home flex flex-col items-center justify-center min-h-screen bg-gray-100">
    <section class="auth-section bg-white p-8 rounded-md shadow-md" style="max-width: 400px; width: 100%;">
      <div class="tabs flex mb-4">
        <button @click="activeTab = 'login'" :class="{ 'bg-blue-500': activeTab === 'login' }"
          class="flex-1 py-2 px-4 text-white rounded-l-md focus:outline-none hover:bg-blue-600">Login</button>
        <button @click="activeTab = 'signup'" :class="{ 'bg-blue-500': activeTab === 'signup' }"
          class="flex-1 py-2 px-4 text-white rounded-r-md focus:outline-none hover:bg-blue-600">Sign Up</button>
      </div>

      <div class="flex flex-col space-y-4">
        <form v-if="activeTab === 'login'" @submit.prevent="handleLogin" class="space-y-4">
          <input v-model="loginUsername" placeholder="Username"
            class="w-full p-2 border rounded-md focus:outline-none focus:border-blue-500" />
          <input type="password" v-model="loginPassword" placeholder="Password"
            class="w-full p-2 border rounded-md focus:outline-none focus:border-blue-500" />

          <!-- Error message display here -->
          <p class="text-green-500" v-if="successMessage">{{ successMessage }}</p>
          <p class="text-red-500" v-if="errorMessage">{{ errorMessage }}</p>

          <button type="submit" :disabled="isLoading"
            class="w-full py-2 bg-blue-500 text-white rounded-md focus:outline-none hover:bg-blue-600">
            <span v-if="!isLoading">Login</span>
            <span v-if="isLoading">Logging in...</span>
          </button>
        </form>

        <form v-if="activeTab === 'signup'" @submit.prevent="handleSignup" class="space-y-4">
          <input v-model="signupUsername" placeholder="Username"
            class="w-full p-2 border rounded-md focus:outline-none focus:border-blue-500" />
          <input type="password" v-model="signupPassword" placeholder="Password"
            class="w-full p-2 border rounded-md focus:outline-none focus:border-blue-500" />
          <input type="password" v-model="signupPasswordConfirmation" placeholder="Confirm Password"
            class="w-full p-2 border rounded-md focus:outline-none focus:border-blue-500" />

          <!-- Error message display here -->
          <p class="text-green-500" v-if="successMessage">{{ successMessage }}</p>
          <p class="text-red-500" v-if="errorMessage">{{ errorMessage }}</p>

          <button type="submit"
            class="w-full py-2 bg-blue-500 text-white rounded-md focus:outline-none hover:bg-blue-600">Sign Up</button>
        </form>
      </div>
    </section>

    <section class="info-section mt-12 text-center">
      <h1 class="text-3xl font-semibold mb-4">Welcome to Our Project!</h1>
      <p class="text-gray-700">Here you can find information about what we do and the benefits of our project...</p>
    </section>
  </div>
</template>


<script>
import { mapActions } from 'vuex';


export default {
  name: 'HomePage',
  data() {
    return {
      activeTab: 'login',
      loginUsername: '',
      loginPassword: '',
      signupUsername: '',
      signupPassword: '',
      errorMessage: '',
      successMessage: '',
      isLoading: false
    };
  },
  methods: {
    ...mapActions(['login', 'signup']),

    async handleLogin() {
      this.isLoading = true; // Set loading state to true at the start

      if (!this.loginUsername.trim() || !this.loginPassword.trim()) {
        this.errorMessage = "Both fields are required!";
        this.isLoading = false; // Immediately set loading state to false if validation fails
        return;
      }

      try {
        await this.login({
          username: this.loginUsername,
          password: this.loginPassword
        });
        // On successful login
        this.successMessage = 'Logged in successfully!';
        this.$router.push('/dashboard');
      } catch (error) {
        console.error("Login failed:", error);
        // On login failure
        this.errorMessage = 'Invalid credentials';
      } finally {
        this.isLoading = false; // Set loading state to false at the end, regardless of success or failure
      }
    },
    async handleSignup() {
      if (!this.signupUsername.trim() || !this.signupPassword.trim() || !this.signupPasswordConfirmation.trim()) {
        this.errorMessage = "All fields are required!";
        return;
      }

      const emailRegex = /^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$/;
      if (!emailRegex.test(this.signupUsername)) {
        this.errorMessage = "Invalid email format!";
        return;
      }
      if (this.signupPassword !== this.signupPasswordConfirmation) {
        this.errorMessage = "Passwords do not match!";
        return;
      }
    },
  },
};
</script> 