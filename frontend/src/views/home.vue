<template>
  <div class="home flex flex-col items-center justify-center min-h-screen bg-gray-100">
    <section class="auth-section bg-white p-8 rounded-md shadow-md">
      <div class="tabs flex mb-4">
        <button @click="activeTab = 'login'" :class="{ 'bg-blue-500': activeTab === 'login' }" class="flex-1 py-2 px-4 text-white rounded-l-md focus:outline-none hover:bg-blue-600">Login</button>
        <button @click="activeTab = 'signup'" :class="{ 'bg-blue-500': activeTab === 'signup' }" class="flex-1 py-2 px-4 text-white rounded-r-md focus:outline-none hover:bg-blue-600">Sign Up</button>
      </div>
      
      <form v-if="activeTab === 'login'" @submit.prevent="handleLogin" class="space-y-4">
        <input v-model="loginUsername" placeholder="Username" class="w-full p-2 border rounded-md focus:outline-none focus:border-blue-500" />
        <input type="password" v-model="loginPassword" placeholder="Password" class="w-full p-2 border rounded-md focus:outline-none focus:border-blue-500" />
        <button type="submit" class="w-full py-2 bg-blue-500 text-white rounded-md focus:outline-none hover:bg-blue-600">Login</button>
      </form>
      
      <form v-if="activeTab === 'signup'" @submit.prevent="handleSignup" class="space-y-4">
        <input v-model="signupUsername" placeholder="Username" class="w-full p-2 border rounded-md focus:outline-none focus:border-blue-500" />
        <input type="password" v-model="signupPassword" placeholder="Password" class="w-full p-2 border rounded-md focus:outline-none focus:border-blue-500" />
        <button type="submit" class="w-full py-2 bg-blue-500 text-white rounded-md focus:outline-none hover:bg-blue-600">Sign Up</button>
      </form>
    </section>
    
    <section class="info-section mt-12 text-center">
      <h1 class="text-3xl font-semibold mb-4">Welcome to Our Project!</h1>
      <p class="text-gray-700">Here you can find information about what we do and the benefits of our project...</p>
    </section>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  data() {
    return {
      activeTab: 'login',
      loginUsername: '',
      loginPassword: '',
      signupUsername: '',
      signupPassword: '',
    };
  },
  methods: {
    async handleLogin() {
      // Handle Login Logic
    },
    async handleSignup() {
      // Handle Signup Logic
    },
  },
};
</script>