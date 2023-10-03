
<template>
  <div id="nav">
    <RouterLink to="/">Home</RouterLink>
    <RouterLink to="/dashboard">Dashboard</RouterLink>
    <RouterLink to="/about">About</RouterLink>
  </div>

  <div class="container">
    <RouterView></RouterView>
  </div>
</template>

<script>
import { RouterView, RouterLink } from 'vue-router';

export default {
  components: {
    RouterView,
    RouterLink,
  },
  async mounted() {
    try {
      const response = await this.$axios.get('/endpoint');
      console.log(response.data);
    } catch (error) {
      console.error('There was an error!', error);
    }
  },
};
</script>
<style scoped>
/* You can add Tailwind classes here or custom styles if needed */
</style>