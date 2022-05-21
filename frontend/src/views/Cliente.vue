<template>
    <div class="container">
      <div class="notification is-danger" v-if="errors.length">
        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
      </div>
      <table class="table">
        <tbody>
          <tr> <td>CPF do Cliente</td> <td> <input v-model="cliente.cpf_cliente" type="number" max="99999999999" style="width: 11em" size="11"></td></tr>
          <tr> <td>Nome da Instalação</td> <td> <input v-model="cliente.nome" type="text" max="40"> </td></tr>
          <tr> <td>Endereço</td> <td> <input v-model="cliente.endereco" type="text" max="84"> </td></tr>
          <tr> <td>E-mail</td> <td> <input v-model="cliente.email" type="email" > </td></tr>
          <tr> <td>Telefone</td> <td> <input v-model="cliente.telefone" type="text" size="13" max="15"> </td></tr>
          <tr> <td>Desconto</td> <td> <input v-model="cliente.desconto" type="number" min="0" max="100" step="1" size="3">%</td></tr>
          <tr> <td>Bônus</td> <td> R$ <input v-model="cliente.bonus" type="number" min="0"  step="0.01"></td></tr>
      
          

        </tbody>
      </table>
      <button @click="gravar(cliente)">Gravar</button>
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
    async validar_campos(cliente){
      this.errors = []
      if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(cliente.email) ==false) {
          this.errors.push('Preencha o e-mail corretamente')
          return null
      }
      if (cliente.nome==''){
        this.errors.push('Preencha o nome da instalação')
      }
      if (cliente.desconto<0 || cliente.desconto>100 || cliente.desconto==''){
        this.errors.push('O valor de desconto deve ser entre 0% e 100%')
      }
      if (cliente.bonus<0 || cliente.bonus==''){
        this.errors.push('O valor do bônus deve ser preenchido com 0 ou qualquer número positivo')
      }
    },
    async gravar(cliente){
      this.validar_campos(cliente)
      if (!this.errors.length) {
        this.$store.commit('setIsLoading', true)
        console.log(cliente)
        await axios
          .put ("/api/v1/clientes/"+cliente.id+"/", cliente)
          .then(response => {
            toast ({
            message: 'Cliente alterado',
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
        
        this.$store.commit('setIsLoading', false)
      }
    },
    async novo(cliente){
      await this.validar_campos(cliente)
      if (!this.errors.length) {
        this.$store.commit('setIsLoading', true)
        console.log(cliente)
        await axios
          .post ("/api/v1/clientes/", cliente)
          .then(response => {
            toast ({
            message: 'Cliente adicionado',
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