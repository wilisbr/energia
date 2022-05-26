import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

//Desenv:
//axios.defaults.baseURL = 'http://127.0.0.1:8000'

//Prod:
//axios.defaults.baseURL = 'https://wilis.pythonanywhere.com'



//Se estiver rodando no ambiente de desenvolvimento, avise o axios que é pra acessar a porta 8000.
if (window.location.href.startsWith('http://localhost')){
    axios.defaults.baseURL = 'http://127.0.0.1:8000'
} else {
    axios.defaults.baseURL = 'http://wilis.pythonanywhere.com'
}

//axios.defaults.baseURL = 'http://127.0.0.1:8000'
//console.log (axios.defaults.baseURL)
createApp(App).use(store).use(router,axios).mount('#app')
