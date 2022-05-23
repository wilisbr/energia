<template>
  <div id="wrapper">
    <nav class="navbar is-success">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong> C.W. Gestão de Energia Fotovoltaica</strong></router-link> 
        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
      </div>

      <div class="navbar-end">

        <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu }">
          
      
          <div class="navbar-item">
            <div class="buttons">
              <template v-if="$store.state.access!=''">
                <router-link to="/clientes" class="navbar-item">Instalações</router-link>
                <router-link to="/faturas" class="navbar-item">Faturas</router-link>
                <router-link to="/my-account" class="navbar-item">Meu Perfil</router-link>
              </template>
              <template v-else>
                <router-link to="/log-in" class="button is-light">Log in</router-link>
              </template>
            </div>
          </div>
        </div>

      </div>
    </nav>
    <progress v-show=$store.state.isLoading />
    <section class="section">
      <router-view/>
    </section>
    <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2021</p>
    </footer>
  </div>
</template>
<script>

import axios from 'axios'

export default {
  name: 'App',
  data() {
    return {
      showMobileMenu: false,
   }
  },
  mounted(){
    this.$router.push('/')
  },
  beforeCreate() {
    this.$store.commit('initializeStore')

    const access = this.$store.state.access

    if (access) {
      axios.defaults.headers.common['Authorization'] = 'JWT '+access
    } else {
      axios.defaults.headers.common['Authorization'] =''
    }
    document.title='Gestão Energia'
  },
}
</script>

<style lang="scss">
@import '../node_modules/bulma/bulma.sass';
</style>
