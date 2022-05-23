<template>
  <div class="container">
    <div  >
      <h1 class="title">Instalações</h1>
      <div class="notification is-danger" v-if="errors.length">
        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
      </div>
      <button @click="$router.push('/cliente/'+'0')">Nova Instalação</button>
      <table class="table">
          <thead>
              <tr>
                  <th>Nome da instalação</th>
                  <th>Endereço da Instalação</th>
                  <th> </th>
              </tr>
          </thead>

          <tbody>
            <tr v-for="cliente in clientes"
                  v-bind:key="cliente.id">
              <td>{{cliente.nome}}</td>
              <td>{{cliente.endereco}}</td>
              <td><button @click="apagar(cliente)">Remover</button>
              <button @click="$router.push('/cliente/'+cliente.id)">Editar</button></td>
            </tr>
          
          </tbody>
      </table>

    </div>      
  </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios'
import {toast} from 'bulma-toast'
import { Text } from '@vue/runtime-core'

 
export default {
  name: 'Clientes',
  data() {
    return {
      clientes : [],
      cliente: Object,
      errors: [],
      novo_cliente: {
                cpf_cliente: Number,
                nome: '',
                telefone: '',
                endereco: '', 
                email: '',
                desconto:20 ,
                bonus:0 ,
            },
    }
  },
  
  components: {

  },
  mounted(){
    this.getClientes()
  },
  methods:{
    logout() {
          toast ({
          message: 'Ticket expirado. Faça novo login',
          type:'is-success',
          dismissible: true,
          pauseOnHover: true,
          duration: 2000,
          position: 'bottom-right'
          })
            axios.defaults.headers.common["Authorization"] = ""
            localStorage.removeItem("access")
            this.$store.commit('removeToken')
            this.$router.push('/log-in')
    },
    async apagar(cliente){
      this.$store.commit('setIsLoading', true)
      console.log(cliente)
      await axios
        .delete ("/api/v1/clientes/"+cliente.id+"/", cliente)
        .then(response => {
          toast ({
          message: 'Instalação removida',
          type:'is-success',
          dismissible: true,
          pauseOnHover: true,
          duration: 2000,
          position: 'bottom-right'
          })
          this.getClientes()
        })
        
        .catch(error => {
            if (error.response.status === 401) {
                console.log('Ticket expirado. Necessário novo login')
                this.logout()
            }
            console.log(error)
          })    
      await new Promise(r => setTimeout(r, 3000));
      this.$store.commit('setIsLoading', false)
    },
    
    async getClientes(){
      this.$store.commit('setIsLoading', true)
      await axios
        .get ("/api/v1/clientes/")
        .then(response => {this.clientes=response.data
        console.log(response)
        })
        
        .catch(error => {
            if (error.response.status === 401) {
                console.log('Ticket expirado. Necessário novo login')
                this.logout()
            }
            console.log(error)
          })    
      this.$store.commit('setIsLoading', false)
    },
  }

}
</script>
<style scoped>
input[type='number']{
    width: 60px;
} 
</style>