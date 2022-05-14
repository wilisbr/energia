<template>
    <div class="page-cart">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Clientes</h1>
            </div>
            <div class="column is-12 box">
                <table class="table is-fullwidth" v-if="clientes.length>0">
                    <thead>
                        <tr>
                            <th>CPF</th>
                            <th>Nome</th>
                            <th>Telefone</th>
                            <th>Ação</th>
                        </tr>
                    </thead>

                    <tbody>
                    <tr v-for="cliente in clientes"
                            v-bind:key="cliente.id">
                        <td> <input v-model="cliente.cpf_cliente" type="number"></td>
                        <td> <input v-model="cliente.nome" type="text" > </td>
                        <td> <input v-model="cliente.telefone" type="text" > </td>
                        <td> <button @click="gravar(cliente)">Gravar</button></td>
                    </tr>
                    <tr>
                      <td><input v-model="novo_cliente.cpf_cliente" type="number" id="cpf_cliente" name="cpf_cliente"></td>
                      <td><input v-model="novo_cliente.nome" type="text" id="nome" name="nome"></td>
                      <td><input v-model="novo_cliente.telefone" type="text" id="telefone" name="telefone"></td>
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
      novo_cliente: {
                cpf_cliente: Number,
                nome: 'Nome',
                telefone: 'Telefone',
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
    async gravar(cliente){
      this.$store.commit('setIsLoading', true)
      console.log(cliente)
      await axios
        .put ("/api/v1/clientes/"+cliente.id+"/", cliente)
        .then(response => {
        console.log('gravado')
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
      this.$store.commit('setIsLoading', true)
      console.log(cliente)
      await axios
        .post ("/api/v1/clientes/", cliente)
        .then(response => {
        console.log('gravado')
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
