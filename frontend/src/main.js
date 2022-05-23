import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

//Desenv:
//axios.defaults.baseURL = 'http://127.0.0.1:8000'

//Prod:
//axios.defaults.baseURL = 'https://wilis.pythonanywhere.com'

axios.defaults.baseURL = 'wilis.pythonanywhere.com'

//Se estiver rodando no ambiente de desenvolvimento, avise o axios que é pra acessar a porta 8000.
if (axios.defaults.baseURL=='http://localhost:8080'){
    axios.defaults.baseURL = 'http://127.0.0.1:8000'
}


createApp(App).use(store).use(router,axios).mount('#app')
