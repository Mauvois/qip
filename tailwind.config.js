/** @type {import('tailwindcss').Config} */
module.exports = {
  // mode: 'jit',
  purge: [
    './src/views/**/*.vue', // scans all .vue files in the src folder
    './frontend/src/**/*.js',
    './public/index.html', // scans the index.html in the public folder
    // You can add other file types that may contain Tailwind CSS classes, e.g.,
    // './src/**/*.js',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
