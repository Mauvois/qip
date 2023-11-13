<template>
    <div class="timeline-container">
        <h2>
            <template v-if="timescale === 'hour'">
                {{ String(new Date().getHours()).padStart(2, '0') }}:{{ String(new Date().getMinutes()).padStart(2, '0') }}
            </template>
            <template v-else-if="timescale === 'day'">
                {{ new Date().toLocaleDateString(undefined, { weekday: 'long' }) }}
            </template>
            <template v-else-if="timescale === 'week'">
                {{ new Date().getDate() }}
            </template>
            <template v-else-if="timescale === 'month'">
                {{ new Date().toLocaleDateString(undefined, { month: 'long' }) }}
            </template>
        </h2>
        <div class="timeline">
            <div v-for="post in filteredPosts" :key="post.id" class="timeline-post" :style="{ top: post.position + '%' }">
                <div class="post-content">
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
    computed: {
        filteredPosts() {
            const now = new Date();
            const timescaleMilliseconds = {
                'hour': 3600000,
                'day': 86400000,
                'week': 604800000,
                'month': 2592000000
            };

            let timescale = timescaleMilliseconds[this.timescale];
            let oldestTime = now.getTime() - timescale;

            return this.posts.filter(post => {
                const postTime = new Date(post.created_time).getTime();
                return postTime >= oldestTime && postTime <= now.getTime();
            }).map(post => {
                const postTime = new Date(post.created_time).getTime();
                let position = ((now - postTime) / timescale) * 100;
                return { ...post, position: position }; // Adjusted to use direct scaling
            });
        }
    }
};
</script>

<style scoped>
/* existing styles */
.timeline-container {
    position: relative;
    padding: 10px;
}

.timeline {
    position: relative;

    padding-left: 20px;
    margin-left: 10px;
    height: 1000px;
}

.timeline-post {
    position: absolute;
    left: 0;
}

.timeline-post .post-content {
    position: relative;
    background: white;
    padding: 10px;
    border-radius: 5px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    width: 200px;
    /* Adjust the width as needed */
    margin-bottom: 10px;
}
</style>