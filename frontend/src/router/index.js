import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import MyAccount from '../views/MyAccount.vue'
import Faturas from '../views/Faturas.vue'
import Fatura from '../views/Fatura.vue'
import Clientes from '../views/Clientes.vue'
import store from '../store'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/my-account',
    name: 'MyAccount',
    component: MyAccount,
    meta: {
        requireLogin: true
    }
  },
  {
    path: '/clientes',
    name: 'Clientes',
    component: Clientes,
    meta: {
        requireLogin: true
    }
  },
  {
    path: '/faturas',
    name: 'Faturas',
    component: Faturas,
    meta: {
        requireLogin: true
    }
  },
  {
    path: '/fatura/:id',
    name: 'Fatura',
    component: Fatura,
    meta: {
        requireLogin: true
    }
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.access) {
    next({ name: 'LogIn', query: { to: to.path } });
  } else {
    next()
  }
})
export default router
