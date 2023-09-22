<template>
  <div class="home">
      <h1>Home</h1>
  </div>
</template>

<script>
export default {
name: 'HomePage', // Added name property
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