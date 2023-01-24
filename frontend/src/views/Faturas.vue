<template>
  <div class="page-cart">
    <div class="columns is-multiline">
      <div class="column is-12">
          <h1 class="title">Faturas</h1>
      </div>
      <div class="notification is-danger" v-if="errors.length">
        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
      </div>
      <div class="column is-12 box">
        <form @submit.prevent="nova_fatura">
          <label>Instalação cliente</label>
          <select required v-model="id_cliente">
            <option v-for="cliente in clientes" v-bind:value="cliente.id" v-bind:key="cliente.id"> 
              {{ cliente.nome }}
            </option>
          </select>
          <router-link to="/clientes">Criar Instalação</router-link>
          <br>
          <label>Distribuidora</label>
          <select required v-model="distribuidora">
            <option value="cemig">Cemig</option>
            <option value="copel">Copel</option>
          </select>
          <br><br>
          <input required type="file"
            id="nova_fatura" name="nova_fatura"
            accept=".pdf" @change="onFileChange">
          <button type="submit">Inserir Fatura</button>
        </form>
        <br><hr>
        <table class="table is-fullwidth" v-if="faturas.length>0">
          <thead>
            <tr>
              <th>Instalação</th>
              <th>Mês de Referência</th>
              <th>Ação</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="fatura in faturas"
                    v-bind:key="fatura.id">
              <td> {{fatura.nome_cliente}}</td>
              <td> {{fatura.referencia}} </td>
              <td> 
              <button @click="$router.push('/fatura/'+fatura.id)">Faturar</button>
              <button @click="apagar(fatura)">Remover</button>  </td>
            </tr>
          </tbody>
        </table>
        <p v-else>Não foram encontradas faturas...</p>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios'
import {toast} from 'bulma-toast'

 
export default {
  name: 'Faturas',
  data() {
    return {
      distribuidora: Text,
      faturas : [],
      clientes: [],
      errors: [],
      fatura: Object,
      id_cliente: -1,
      conta_pdf: Object,
    }
  },
  components: {

  },
  
  async mounted(){
    this.$store.commit('setIsLoading', true)
    await this.getClientes()
    await this.getFaturamentos()
    
    this.$store.commit('setIsLoading', false)
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
    async getClientes(){
      await axios
        .get ("/api/v1/clientes/")
        .then(response => {this.clientes=response.data
        })
        .catch(error => {
            if (error.response.status === 401) {
                console.log('Ticket expirado. Necessário novo login')
                this.logout()
            }
            console.log(error)
          })    
    },
    onFileChange(e) {
      var files = e.target.files || e.dataTransfer.files;
      if (!files.length) return;
      //this.fatura.conta_pdf = files[0]
      this.conta_pdf = files[0]
      //this.nova_fatura()
    },
    upload_fatura: async function (e){
      let formData = new FormData();
      if (this.conta_pdf){
        formData.append('conta_pdf', this.conta_pdf);
        formData.append('distribuidora', this.distribuidora)
      }
      axios.defaults.headers.put['Content-Type']='application/json' 
      await axios
        .put (`/api/v1/faturamentos/${this.fatura.id}/`, formData)
        .then (response => {
            this.fatura=response.data
        })
        .catch(error => {
            if (error.response) {
                for (const property in error.response.data) {
                    //this.errors.push(`${property}: ${error.response.data[property]}`)
                    console.log(error)
                }
            } else {
                this.errors.push('Something went wrong. Please try again')
                console.log(JSON.stringify(error))
            }
        })
      await this.carregarConta()
      
    },
    carregarConta: async function (e){
      
      let formData = new FormData();
      formData.append('id', this.fatura.id);
      await axios
        .post (`/api/v1/carregarConta`, formData)
        .then (response => {
            this.fatura=response.data
        })
        .catch(error => {
            if (error.response) {
                console.log(error)
                for (const property in error.response.data) {
                    this.errors.push(`${property}: ${error.response.data[property]}`)
                 }
            } else {
                this.errors.push('Something went wrong. Please try again')
                console.log(JSON.stringify(error))
            }
            this.apagar(this.fatura)
        })
    },
    async nova_fatura(){
      this.errors=[]
      this.$store.commit('setIsLoading', true)
      this.fatura={
        cpf_cliente: this.id_cliente,
        distribuidora: this.distribuidora
      }
      await axios
        .post ("/api/v1/faturamentos/",this.fatura)
        .then(response => {
          this.fatura=response.data
        })
        .catch(error => {
            if (error.response.status === 401) {
                console.log('Ticket expirado. Necessário novo login')
                this.logout()
            }
            console.log(error)
          })
      await this.upload_fatura()
      await this.getFaturamentos()
      this.$store.commit('setIsLoading', false)

    },
    async apagar(fatura){
      this.$store.commit('setIsLoading', true)
      await axios
        .delete ("/api/v1/faturamentos/"+fatura.id+"/")
        .then(response => {
          this.getFaturamentos()
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

    async getFaturamentos(){
      //await new Promise(r => setTimeout(r, 1000));
      await axios
        .get ("/api/v1/faturamentos/")
        .then(response => {this.faturas=response.data
        })
        .catch(error => {  
            if (error.response.status === 401) {
                console.log('Ticket expirado. Necessário novo login')
                this.logout()
            }
            console.log(error)
          })    

      // Vamos baixar o nome dos clientes:
      for(let i = 0; i < this.faturas.length; i = i + 1 ) {
        var result = this.clientes.find(cliente => cliente.id === this.faturas[i].cpf_cliente);
        this.faturas[i].nome_cliente=result.nome
      }
      
    },
  }

}
</script>
