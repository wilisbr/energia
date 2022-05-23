<template>
    <div class="container">
      <div class="notification is-danger" v-if="errors.length">
        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
      </div>
      <form @submit.prevent="gravar_ou_criar">
      <table class="table">
        <tbody>
          <tr> <td>CPF do Cliente</td> <td> <input v-model="cliente.cpf_cliente" required type="number" max="99999999999" style="width: 11em" size="11"></td></tr>
          <tr> <td>Nome da Instalação</td> <td> <input v-model="cliente.nome" required type="text" max="40"> </td></tr>
          <tr> <td>Endereço</td> <td> <input v-model="cliente.endereco" type="text" max="84"> </td></tr>
          <tr> <td>E-mail</td> <td> <input v-model="cliente.email" type="email" > </td></tr>
          <tr> <td>Telefone</td> <td> <input v-model="cliente.telefone" type="text" size="13" max="15"> </td></tr>
          <tr> <td>Desconto</td> <td> <input v-model="cliente.desconto" required type="number" min="0" max="100" step="1" size="3">%</td></tr>
          <tr> <td>Bônus</td> <td> R$ <input v-model="cliente.bonus" required type="number" min="0"  step="0.01"></td></tr>
        </tbody>
      </table>
      <button @click="$router.push('/clientes')">Voltar</button>
      <button type="submit">Gravar</button>
      
      </form>
    </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios'
import {toast} from 'bulma-toast'
 
export default {
  name: 'Clientes',
  data() {
    return {
      cliente: {},
      errors: [],
      id:this.$route.params.id,
    }
  },
  
  components: {

  },
  mounted(){
    if (this.id!=0){ 
      this.cliente=this.getCliente()
    }
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

    async getCliente(){
      this.$store.commit('setIsLoading', true)
      await axios
          .get ("/api/v1/clientes/"+this.id+"/")
          .then(response => {
            this.cliente=response.data
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
    gravar_ou_criar(){
      if (this.id==0){
        this.novo()
      } else{
        this.gravar()
      }

    },
    async gravar(){
      
      if (!this.errors.length) {
        this.$store.commit('setIsLoading', true)
        console.log(this.cliente)
        await axios
          .put ("/api/v1/clientes/"+this.id+"/", this.cliente)
          .then(response => {
            toast ({
            message: 'Cliente alterado',
            type:'is-success',
            dismissible: true,
            pauseOnHover: true,
            duration: 2000,
            position: 'bottom-right'
            })
            this.cliente=response.data
            this.$router.push('/clientes')
          })
          
          .catch(error => {
            if (error.response.status === 401) {
                console.log('Ticket expirado. Necessário novo login')
                this.logout()
            }
            console.log(error)
          })    
        
        this.$store.commit('setIsLoading', false)
      }
    },
    async novo(){

      if (!this.errors.length) {
        this.$store.commit('setIsLoading', true)
        console.log(this.cliente)
        await axios
          .post ("/api/v1/clientes/", this.cliente)
          .then(response => {
            toast ({
            message: 'Cliente adicionado',
            type:'is-success',
            dismissible: true,
            pauseOnHover: true,
            duration: 2000,
            position: 'bottom-right'
            })
            this.cliente=response.data
            this.$router.push('/clientes')
          })
          
          .catch(error => {
              if (error.response.status === 401) {
                  console.log('Ticket expirado. Necessário novo login')
                  this.logout()
              }
              console.log(error)
            })    
        this.$store.commit('setIsLoading', false)
      }
    },
  }

}
</script>
<style scoped>
input[type='number']{
    width: 60px;
} 
</style>