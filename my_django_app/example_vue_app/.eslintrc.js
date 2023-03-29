module.exports = {
  "root": true,
  "env": {
    "node": true,
    "browser": true,
    "es2021": true
  },
  "extends": [
    "eslint:recommended",
    "plugin:vue/vue3-essential"
  ],
  "overrides": [
  ],
  "parserOptions": {
    "parser": '@babel/eslint-parser',
    "ecmaVersion": "latest",
    "sourceType": "module",
    "ecmaFeatures": {
      "modules": true
    }
  },
  "plugins": [
    "vue"
  ],
  "rules": {
  }
}
