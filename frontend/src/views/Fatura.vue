<template>
    <div class="page-cart">
        <form @submit.prevent="upload_fatura">
            <a :href="fatura.conta_pdf" target="_blank">Ver Fatura Atual </a>

            <input type="file"
              id="avatar" name="avatar"
              accept=".pdf" @change="onFileChange">
            <button type="submit">Substituir Fatura</button>
        </form>
        <form @submit.prevent="gravar">
            <label>Percentual de desconto:</label>
            <input type="number" min="0" max="100" step="1" v-model="fatura.desconto" />
            <br><br>
            <label>Bônus (R$):</label>
            <input type="number" name="bonus" v-model="fatura.bonus"> <br><br>
            <button type="submit">Gravar</button>
            ou <router-link to="/faturas">Sair</router-link>
        </form>
        <iframe :key="id_iFrameCobrancaPDF" :src="`http://localhost:8000/api/v1/getFaturaPdf?id=${id}`" width="100%" height="700px"></iframe>
    </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios'
import {toast} from 'bulma-toast'
import download from 'downloadjs'



export default {
  name: 'Fatura',
  data() {
    return{
      id:this.$route.params.id,
      fatura: Object,
      conta_pdf: Object,
      id_iFrameCobrancaPDF: Number
    }
  },
  components: {
      
  },
  props: {

  },
  mounted(){
    this.id_iFrameCobrancaPDF=0
    this.getFatura()
    //this.downloadFatura()
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
      this.upload_fatura()
    },
    upload_fatura: async function (e){
      let formData = new FormData();
      if (this.conta_pdf){
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
              this.carregarConta()
              this.id_iFrameCobrancaPDF=this.id_iFrameCobrancaPDF+1
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
    carregarConta: async function (e){
        let formData = new FormData();
        formData.append('id', this.fatura.id);
        await axios
          .post (`/api/v1/carregarConta`, formData)
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
            delete this.fatura.conta_pdf
            await axios
                .put (`/api/v1/faturamentos/${this.id}/`, this.fatura)
                .then (response => {
                    console.log('Deu certo!')
                    console.log (response)
                    this.fatura=response.data
                    this.id_iFrameCobrancaPDF=this.id_iFrameCobrancaPDF+1
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

  },
  

}
</script>
