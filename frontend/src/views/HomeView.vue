<template>
  <div class="home">
    <h1>Home</h1>
    <div v-for="faturamento in faturamentos" v-bind:key="faturamento.id"> {{faturamento}}</div> 
  </div>

    

</template>

<script>
/* eslint-disable */
import axios from 'axios'
import {toast} from 'bulma-toast'
 
export default {
  name: 'HomeView',
  data() {
    return {
      user_data : '',
      faturamentos : []
    }
  },
  components: {

  },
  mounted(){
    this.getMe(),
    this.getFaturamentos()
  },
  methods:{
    getMe(e){
      console.log(axios.defaults.headers.common['Authorization'])
      axios
          .get ("/api/v1/users/me")
          .then(response => {
            console.log(response)
            this.user_data = response.data.username
          })
          .catch(error => {
            console.log(error)
          })
    },
    async getFaturamentos(){
      this.$store.commit('setIsLoading', true)
      await new Promise(r => setTimeout(r, 1000));
      await axios
        .get ("/api/v1/faturamentos/")
        .then(response => {this.faturamentos=response.data
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
