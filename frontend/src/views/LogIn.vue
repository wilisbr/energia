<template>
    <div class='log-in-page'>
        <h1> Log In </h1>
        <form @submit.prevent="submitForm">
            <label>Username:</label>
            <input type="email" name="username" v-model="username"> <br><br>
            <label>Password:</label>
            <input type="password" name="password" v-model="password"> <br><br>
            <div class="notification is-danger" v-if="errors.length">
                <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
            </div>
            <button type="submit">Log in</button>
            <a href="`${this.$axios.defaults.baseURL}/accounts/password_reset/`"> Esqueci minha senha </a>
            Ou <router-link to="/sign-up">Clique aqui</router-link> para se cadastrar!
        </form>
    </div>
</template>

<script>
import axios from 'axios'
/* eslint-disable */
export default {
    name: 'LogIn',
    data(){
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    methods:{
        submitForm(e){
            axios.defaults.headers.common['Authorization']=''
            localStorage.removeItem('access')
            const formData = {
                username: this.username,
                password: this.password,
            }
            axios
                .post ('/api/v1/jwt/create/', formData)
                .then (response => {
                    console.log('Deu certo!')
                    console.log (response)
                    const access=response.data.access
                    this.$store.commit('setAccess', access)
                    axios.defaults.headers.common['Authorization']= "JWT "+access
                    localStorage.setItem("access",access)
                    this.$router.push("/clientes")
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
    }      
}
</script>
