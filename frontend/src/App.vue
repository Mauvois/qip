
<template>
  <div class="container">
    <RouterView></RouterView>
  </div>
</template>

<script>
import { RouterView, RouterLink } from 'vue-router';
import axios from '@/axios.js';

export default {
  components: {
    RouterView,
    RouterLink,
  },
};
</script>
<style scoped>
/* You can add Tailwind classes here or custom styles if needed */
</style>