<template>
  <div class="home">
    <h1>Home</h1>
     
  </div>

    

</template>

<script>
/* eslint-disable */
import axios from 'axios'
 
export default {
  name: 'HomeView',
  data() {
    return {
      user_data : '',
    }
  },
  components: {

  },
  mounted(){
    //this.getMe(),
    
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
  }

}
</script>
