const path = require('path');

module.exports = {
    configureWebpack: {
        entry: './frontend/src/main.js',
        resolve: {
            alias: {
                '@': path.resolve(__dirname, 'frontend/src')
            }
        }
    }
}