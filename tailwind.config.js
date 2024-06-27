/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.{html,js}"],
  theme: {
    extend: {
      fontFamily: {
        "header" : ["inter", "sans-serif"],
        "textFont" : ["poppins", "sans-serif"]
      },
    },
  },
  plugins: [],
}

