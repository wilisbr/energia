<template>
    <div class="page-cart">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Faturas</h1>
            </div>
            <div class="column is-12 box">
                <table class="table is-fullwidth" v-if="faturas.length>0">
                    <thead>
                        <tr>
                            <th>Cliente</th>
                            <th>Total a Receber</th>
                            <th>Ação</th>
                        </tr>
                    </thead>

                    <tbody>
                    <tr v-for="fatura in faturas"
                            v-bind:key="fatura.id">
                        <td> {{ fatura.desconto }}</td>
                        <td> {{fatura.totalPagar}} </td>
                        <td> <router-link :to="'/fatura/'+fatura.id"> Editar </router-link> </td>
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
      faturas : []
    }
  },
  components: {

  },
  mounted(){
    this.getFaturamentos()
  },
  methods:{
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
      this.$store.commit('setIsLoading', false)
    },
  }

}
</script>
