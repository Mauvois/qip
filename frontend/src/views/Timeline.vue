<template>
    <div class="relative p-2.5">
        <h2>
            <template v-if="timescale === 'hour'">
                {{ String(currentTime.getHours()).padStart(2, '0') }}:{{ String(currentTime.getMinutes()).padStart(2, '0')
                }}
            </template>
            <template v-else-if="timescale === 'day'">
                {{ currentTime.toLocaleDateString(undefined, { weekday: 'long' }) }}
            </template>
            <template v-else-if="timescale === 'week'">
                {{ currentTime.getDate() }}
            </template>
            <template v-else-if="timescale === 'month'">
                {{ currentTime.toLocaleDateString(undefined, { month: 'long' }) }}
            </template>
            <template v-if="timescale === 'year'">
                {{ currentTime.getFullYear() }}
            </template>
            <template v-if="timescale === 'decade'">
                {{ Math.floor(currentTime.getFullYear() / 10) * 10 }}s
            </template>
        </h2>
        <div class="relative pl-5 ml-2.5 h-[1000px]">
            <div v-for="post in filteredPosts" :key="post.id" class="absolute left-0" :style="{ top: post.position + '%' }">
                <div class="block w-5 h-5 bg-black text-white text-center leading-5 cursor-pointer rounded-full"></div>
                <div class="absolute bg-white p-2.5 rounded-md shadow-md w-52 mb-2.5 hidden left-6">
                    <strong>{{ post.user.username }}:</strong> {{ post.content }}
                    <br>
                    <small>Posted on: {{ new Date(post.created_time).toLocaleString() }}</small>
                </div>
            </div>
        </div>
    </div>
</template>




<script>
export default {
    props: {
        timescale: String,
        posts: Array
    },
    data() {
        return {
            currentTime: new Date(),
            intervalId: null
        };
    },
    mounted() {
        this.intervalId = setInterval(() => {
            this.currentTime = new Date();
        }, 60000); // Update every minute
    },
    beforeDestroy() {
        clearInterval(this.intervalId);
    },
    computed: {
        filteredPosts() {
            const timescaleMilliseconds = {
                'hour': 3600000,
                'day': 86400000,
                'week': 604800000,
                'month': 2592000000,
                'year': 31536000000,
                'decade': 315360000000
            };

            let timescale = timescaleMilliseconds[this.timescale];
            let oldestTime = this.currentTime.getTime() - timescale;
            let threshold = 5; // Top 5%

            return this.posts.filter(post => {
                const postTime = new Date(post.created_time).getTime();
                return postTime >= oldestTime && postTime <= this.currentTime.getTime();
            }).map(post => {
                const postTime = new Date(post.created_time).getTime();
                let position = ((this.currentTime - postTime) / timescale) * 100;

                if (position <= threshold) {
                    return null; // Exclude this post
                }

                return { ...post, position: position };
            }).filter(post => post !== null); // Remove nulls from the filtered array
        }
    }
};
</script>