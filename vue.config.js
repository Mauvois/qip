const path = require('path');

module.exports = {
    configureWebpack: {
        entry: '@/main.js',
        resolve: {
            alias: {
                '@': path.resolve(__dirname, 'frontend/src')
            }
        }
    }
}