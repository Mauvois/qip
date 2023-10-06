/** @type {import('tailwindcss').Config} */
module.exports = {
  // mode: 'jit',
  content: [
    './src/views/**/*.vue', // scans all .vue files in the src folder
    './frontend/src/**/*.js',
    './index.html'
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
