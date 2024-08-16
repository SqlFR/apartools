/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      "./templates/**/*.html",
      "./issues/templates/**/*.html",
      "./accounts/templates/**/*.html",
      "./project/templates/**/*.html",
  ],
  theme: {
    extend: {
        flexGrow: {
            '2': 2, // Ajoute flex-grow-2
            '3': 3, // Ajoute flex-grow-3
}
    },
  },
  plugins: [],
}

