module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [require('taos/plugin')],
  safelist: ['!duration-[0ms]', '!delay-[0ms]', 'html.js :where([class*="taos:"]:not(.taos-init))'],
  content: {
    transform: (content) => content.replace(/taos:/g, ''),
    relative: true,
  },
}
