<template>
    <div class='sign-up-page'>
        <h1> Sign up </h1>
        <form @submit.prevent="submitForm">
            <label>Username:</label>
            <input type="email" name="username" v-model="username"> <br><br>
            <label>Password:</label>
            <input type="password" name="password" v-model="password"> <br><br>
            <label>Password 2:</label>
            <input type="password" name="password2" v-model="password2"> <br><br>
            <div class="notification is-danger" v-if="errors.length">
                <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
            </div>
            <button type="submit"> Sign up</button>
        </form>
    </div>
</template>

<script>

import axios from 'axios'
import {toast} from 'bulma-toast'

/* eslint-disable */
export default {
    name: 'SignUp',
    data(){
        return {
            username: '',
            password: '',
            password2: '',
            errors: []
        }
    },
    methods:{
        submitForm(e){
            this.errors = []
            if (this.username === '') {
                this.errors.push('The username is missing')
            }
            if (this.password === '') {
                this.errors.push('The password is too short')
            }
            if (this.password !== this.password2) {
                this.errors.push('The passwords doesn\'t match')
            }
            if (!this.errors.length) {

                const formData = {
                    username: this.username,
                    password: this.password,
                }

                axios
                    .post ('/api/v1/users/', formData)
                    .then (response => {
                            toast({
                            message: 'Account created, please log in!',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })
                        this.$router.push('/log-in')
                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                            console.log(JSON.stringify(error.response.data))
                        } else if (error.message) {
                            this.errors.push('Something went wrong. Please try again')
                            
                            console.log(JSON.stringify(error))
                        }
                    })
            }
        }
    }      
}
</script>
