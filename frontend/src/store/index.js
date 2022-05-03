import { createStore } from 'vuex'


export default createStore({
  state: {
    access: '',
    refresh: '',
    isLoading: false
  },
  mutations: {
    initializeStore(state){
      if (localStorage.getItem('access')){
        state.access = localStorage.getItem('access')
      } else{
        state.access = ''

      }
    },
    setAccess(state,access){
      state.access=access
    },
    setIsLoading(state, status) {
      state.isLoading = status
    },
    removeToken(state) {
      state.access = ''
  },
  },

  actions: {
  },
  modules: {
  }
})
