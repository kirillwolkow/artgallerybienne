const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
    content: [
        '../templates/**/*.html',
        '../../templates/**/*.html',
        '../../**/templates/**/*.html',
    ],
    theme: {
        extend: {
            colors: {
                'black-steel': '#080706',
                'paper': '#EFEFEF',
                'gold-leaf': '#D1B280',
                'silver': '#594D46',
            },
            fontFamily: {
                'sans': ['Fjalla One', ...defaultTheme.fontFamily.sans],
                'serif': ['Lora', ...defaultTheme.fontFamily.sans],
            }
        },
    },
    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
        require('@tailwindcss/line-clamp'),
    ],
}
