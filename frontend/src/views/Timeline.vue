<template>
    <div>
        <h2>{{ timescale }} Timeline</h2>
        <ul>
            <li v-for="post in filteredPosts" :key="post.id">
                <strong>{{ post.user.username }}:</strong> {{ post.content }}
                <br>
                <small>Posted on: {{ new Date(post.created_time).toLocaleString() }}</small>
            </li>
        </ul>
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

            return this.posts.filter(post => {
                const postDate = new Date(post.created_time);
                let timeDifference = now - postDate;

                // Exclude future-dated posts
                if (timeDifference < 0) {
                    console.error("Post is dated in the future:", post);
                    return false;
                }

                switch (this.timescale) {
                    case 'hour':
                        return timeDifference <= 3600000; // 1 hour in milliseconds
                    case 'day':
                        return timeDifference <= 86400000; // 1 day in milliseconds
                    case 'week':
                        return timeDifference <= 604800000; // 1 week in milliseconds
                    case 'month':
                        return timeDifference <= 2592000000; // 30 days in milliseconds
                    default:
                        return false;
                }
            });
        }
    }
};
</script>

<style scoped>
/* Styles specific to the Timeline component */
</style>