<template>
  <div class="page-cart">
    <div class="columns is-multiline">
      <div class="column is-12">
          <h1 class="title">Faturas</h1>
      </div>
      <div class="column is-12 box">
        <form @submit.prevent="nova_fatura">
          <label>CPF</label>
          <input type="number" name="cliente" v-model="fatura.id_cliente"> <br><br>
          <input type="file"
            id="nova_fatura" name="nova_fatura"
            accept=".pdf" @change="onFileChange">
          <button type="submit">Inserir Fatura</button>
        </form>
        <br><hr>
        <table class="table is-fullwidth" v-if="faturas.length>0">
          <thead>
            <tr>
              <th>Cliente</th>
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
              <button @click="$router.push('/fatura/'+fatura.id)">Gerar Cobrança</button>
              <button @click="apagar(fatura)">Remover Fatura</button>  </td>
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
      faturas : [],
      fatura: {cpf_cliente: 1},
      conta_pdf: Object,
    }
  },
  components: {

  },
  mounted(){
    this.getFaturamentos()
  },
  methods:{
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
        console.log ('achei um anexo')
        console.log (this.conta_pdf)
        formData.append('conta_pdf', this.conta_pdf);
      }
      axios.defaults.headers.put['Content-Type']='application/json' 
      console.log (axios.defaults.headers)
      await axios
          .put (`/api/v1/faturamentos/${this.fatura.id}/`, formData)
          .then (response => {
              console.log('Deu certo!')
              console.log (response)
              this.fatura=response.data
          })
          .catch(error => {
              if (error.response) {
                  for (const property in error.response.data) {
                      this.errors.push(`${property}: ${error.response.data[property]}`)
                  }
              } else {
                  this.errors.push('Something went wrong. Please try again')
                  
                  console.log(JSON.stringify(error))
              }
          })
        this.carregarConta()
    },
    carregarConta: async function (e){
        console.log(this.fatura)
        let formData = new FormData();
        formData.append('id', this.fatura.id);
        await axios
          .post (`/api/v1/carregarConta`, formData)
          .then (response => {
              this.fatura=response.data
          })
          .catch(error => {
              if (error.response) {
                  for (const property in error.response.data) {
                      this.errors.push(`${property}: ${error.response.data[property]}`)
                  }
              } else {
                  this.errors.push('Something went wrong. Please try again')
                  console.log(JSON.stringify(error))
              }
          })
    },
    async nova_fatura(){
      this.$store.commit('setIsLoading', true)
      await axios
        .post ("/api/v1/faturamentos/",this.fatura)
        .then(response => {
          this.fatura=response.data
        })
        .catch(error => {
            console.log(error)
          })
      this.upload_fatura()
      this.getFaturamentos()
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
            console.log(error)
          })  
      this.$store.commit('setIsLoading', false)
    },

    async getFaturamentos(){
      this.$store.commit('setIsLoading', true)
      await new Promise(r => setTimeout(r, 1000));
      await axios
        .get ("/api/v1/faturamentos/")
        .then(response => {this.faturas=response.data
        console.log(response)
        
        })
        
        .catch(error => {
            console.log(error)
          })    
      toast ({
          message: 'Teste',
          type:'is-success',
          dismissible: true,
          pauseOnHover: true,
          duration: 2000,
          position: 'bottom-right'
        })

      // Vamos baixar o nome dos clientes:
      for(let i = 0; i < this.faturas.length; i = i + 1 ) {
        await axios
        .get ("/api/v1/clientes/"+this.faturas[i].cpf_cliente+"/")
        .then(response => {
        this.faturas[i].nome_cliente=response.data.nome
        
        })
        .catch(error => {
            console.log(error)
          })    
      }
      this.$store.commit('setIsLoading', false)
    },
  }

}
</script>
