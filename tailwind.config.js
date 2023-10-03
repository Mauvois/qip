/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: 'jit',
  content: [
    './src/**/*.vue', // scans all .vue files in the src folder
    './public/index.html', // scans the index.html in the public folder
    // You can add other file types that may contain Tailwind CSS classes, e.g.,
    // './src/**/*.js',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
