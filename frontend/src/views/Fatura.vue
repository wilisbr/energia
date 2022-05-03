<template>
    <div class="page-cart">
        Aqui vai aparecer a faturamento
        {{fatura}}
        <form @submit.prevent="upload_fatura">
            <a :href="fatura.conta_pdf" target="_blank">Ver Fatura Atual </a>

            <input type="file"
              id="avatar" name="avatar"
              accept=".pdf" @change="onFileChange">
            <button type="submit">Substituir Fatura</button>
        </form>
        <form @submit.prevent="gravar_old">
            <label>Percentual de desconto:</label>
            <input type="number" min="0" max="100" step="1" v-model="fatura.desconto" />
            <br><br>
            <label>Bônus (R$):</label>
            <input type="number" name="bonus" v-model="fatura.bonus"> <br><br>
            <button type="submit">Gravar</button>
            ou <router-link to="/faturas">Sair</router-link>
        </form>
    </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios'
import {toast} from 'bulma-toast'
 
export default {
  name: 'Fatura',
  data() {
    return{
      id:this.$route.params.id,
      fatura: Object,
      conta_pdf: Object
    }
  },
  components: {

  },
  props: {

  },
  mounted(){
    this.getFatura()
  },
  methods:{
    async getFatura(){
      await axios
        .get ("/api/v1/faturamentos/"+this.id)
        .then(response => {this.fatura=response.data
        console.log(response)
        
        })
        
        .catch(error => {
            console.log(error)
          })    
    },
    onFileChange(e) {
      var files = e.target.files || e.dataTransfer.files;
      if (!files.length) return;
      //this.fatura.conta_pdf = files[0]
      this.conta_pdf = files[0]
      console.log (files[0])
    },
    upload_fatura: async function (e){
      let formData = new FormData();
      if (this.fatura.conta_pdf){
        console.log ('achei um anexo')
        console.log (this.conta_pdf)
        formData.append('conta_pdf', this.conta_pdf);
        //formData.append('bonus', 30)
      }
      axios.defaults.headers.put['Content-Type']='application/json' 
      console.log (axios.defaults.headers)
      await axios
          .put (`/api/v1/faturamentos/${this.id}/`, formData)
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
      },
    gravar: async function (e){
      console.log (axios.defaults.headers)
      console.log (this.fatura)
      axios.defaults.headers.put['Content-Type']='application/x-www-form-urlencoded' 
      await axios
          .put (`/api/v1/faturamentos/${this.id}/`, this.fatura)
          .then (response => {
              console.log('Deu certo!')
              console.log (response)
              const access=response.data.access
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
      gravar_old: async function (e){
            delete this.fatura.conta_pdf
            await axios
                .put (`/api/v1/faturamentos/${this.id}/`, this.fatura)
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
      }
  
  },
  

}
</script>
