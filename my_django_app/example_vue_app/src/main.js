import { createApp } from 'vue'
import App from './App.vue'

const propJson = document.getElementById('example_vue_app_props').textContent
const props = JSON.parse(propJson)

const vueApp = createApp(App, props)
vueApp.mount('#example_vue_app_container')
