/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.{html,js}"],
  theme: {
    extend: {
      fontFamily: {
        "header" : ["inter", "sans-serif"],
        "textFont" : ["poppins", "sans-serif"]
      },
      backgroundImage: {
        "coverImg": "url('https://wallpapercave.com/wp/wp2722928.jpg')",
        "profileImg" : "url('https://wallpaperaccess.com/full/1672453.jpg')"
      }
    },
  },
  plugins: [],
}

