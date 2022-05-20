import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

//Desenv:
axios.defaults.baseURL = 'http://127.0.0.1:8000'

//Prod:
axios.defaults.baseURL = 'https://wilis.pythonanywhere.com'


createApp(App).use(store).use(router,axios).mount('#app')
