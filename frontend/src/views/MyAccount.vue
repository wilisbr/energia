<template>
    <div class="page-my-account">
        <div class="columns is-multiline">
            <div class="column is-12">
                <span :src="user_data">{{user_data}}</span>
            </div>

            <div class="column is-12">
                <button @click="logout()" class="button is-danger">Log out</button>
            </div>

            <hr>


        </div>
    </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios'

export default {
    name: 'MyAccount',
    components: {
    },
    data() {
        return {
            user_data : '',
        }
    },
    mounted() {
        this.getMe()
    },
    methods: {
        logout() {
            axios.defaults.headers.common["Authorization"] = ""
            localStorage.removeItem("access")
            this.$store.commit('removeToken')
            this.$router.push('/')
        },

        async getMe(e){
            this.$store.commit('setIsLoading', true)
            console.log(axios.defaults.headers.common['Authorization'])
            await axios
                .get ("/api/v1/users/me")
                .then(response => {
                    console.log(response)
                    this.user_data = response.data.username
                })
                .catch(error => {
                    console.log(error)
                })
            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>