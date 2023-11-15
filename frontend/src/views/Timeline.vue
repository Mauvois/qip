<template>
    <div class="timeline-container">
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
        <div class="timeline">
            <div v-for="post in filteredPosts" :key="post.id" class="timeline-post" :style="{ top: post.position + '%' }">
                <div class="post-icon">-</div>
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

<style scoped>
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

.timeline-post .post-icon {
    display: block;
    width: 20px;
    height: 20px;
    background-color: black;
    color: white;
    text-align: center;
    line-height: 20px;
    cursor: pointer;
    border-radius: 50%;
}

.timeline-post .post-content {
    position: absolute;
    background: white;
    padding: 10px;
    border-radius: 5px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    width: 200px;
    margin-bottom: 10px;
    display: none;
    /* Hide by default */
    left: 25px;
    /* Position next to the icon */
}

.timeline-post:hover .post-content {
    display: block;
    /* Show on hover */
}
</style>