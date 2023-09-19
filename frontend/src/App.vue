
import { RouterView } from 'vue-router';
import { RouterLink } from 'vue-router';

<template>
    <div id="nav">
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
    </div>

    <div class="container">
        <RouterView></RouterView>
    </div>
</template>

<script>

</script>