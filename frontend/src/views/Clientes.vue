<template>
    <div class="page-cart">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Clientes</h1>
            </div>
            <div class="column is-12 box">
                <div class="notification is-danger" v-if="errors.length">
                  <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div>
                <table class="table is-fullwidth" v-if="clientes.length>0">
                    <thead>
                        <tr>
                            <th>CPF</th>
                            <th>Nome</th>
                            <th>Endereço</th>
                            <th>E-mail</th>
                            <th>Telefone</th>
                            <th>Desconto</th>
                            <th>Bônus</th>
                            <th>Ação</th>
                        </tr>
                    </thead>

                    <tbody>
                    <tr v-for="cliente in clientes"
                            v-bind:key="cliente.id">
                        <td> <input v-model="cliente.cpf_cliente" type="number" max="99999999999" style="width: 11em" size="11"></td>
                        <td> <input v-model="cliente.nome" type="text" max="40"> </td>
                        <td> <input v-model="cliente.endereco" type="text" max="84"> </td>
                        <td> <input v-model="cliente.email" type="email" > </td>
                        <td> <input v-model="cliente.telefone" type="text" size="15" max="15"> </td>
                        <td> <input v-model="cliente.desconto" type="number" min="0" step="1" size="4">%</td>
                        <td> <input v-model="cliente.bonus" type="number" min="0" max="100" step="0.01"></td>
                        <td> <button @click="gravar(cliente)">Gravar</button>
                        <button @click="apagar(cliente)">Remover</button></td>
                    </tr>
                    <tr>
                      <td><input v-model="novo_cliente.cpf_cliente" type="number" max="99999999999" style="width: 11em" size="11"></td>
                      <td><input v-model="novo_cliente.nome" type="text" max="40"></td>
                      <td><input v-model="novo_cliente.endereco" type="text" max="84"> </td>
                      <td><input v-model="novo_cliente.email" type="email"> </td>
                      <td><input v-model="novo_cliente.telefone" type="text" size="15" max="15"></td>
                      <td><input v-model="novo_cliente.desconto" type="number" min="0" step="1" size="4">%</td>
                      <td><input v-model="novo_cliente.bonus" type="number" min="0" max="100" step="0.01"></td>
                      <td><button @click="novo(novo_cliente)">Incluir</button></td>
                    </tr>
                    </tbody>
                </table>

                <p v-else>Não foram encontrados clientes...</p>
            </div>

            
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
      cliente: Number,
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
    async validar_campos(cliente){
      this.errors = []
      if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(cliente.email) ==false) {
          this.errors.push('Preencha o e-mail corretamente')
          return null
      }
      if (cliente.nome==''){
        this.errors.push('Preencha o nome do cliente')
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
    async apagar(cliente){
      this.$store.commit('setIsLoading', true)
      console.log(cliente)
      await axios
        .delete ("/api/v1/clientes/"+cliente.id+"/", cliente)
        .then(response => {
          toast ({
          message: 'Cliente removido da base de dados',
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
        this.$store.commit('setIsLoading', false)
      }
    },
    async getClientes(){
      this.$store.commit('setIsLoading', true)
      await new Promise(r => setTimeout(r, 1000));
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