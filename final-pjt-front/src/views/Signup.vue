<template>
  <v-app>
    <v-main>
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center" dense>
          <v-col cols="12" sm="8" md="4" lg="4">
            <v-card>
              <a href="https://edu-fedorae.netlify.app" name="Fedorae Education" title="Fedorae Education" target="_blank">
                <v-img src="@/assets/logo.png" alt="Fedorae Education Log" contain height="200"></v-img>
              </a>
              <v-card-text>
                <v-form>
                  <v-text-field v-model.trim="credentials.username" label="Enter your username" name="username" prepend-inner-icon="mdi-account" type="text" class="rounded-0" outlined></v-text-field>
                  <!-- <v-text-field label="Enter your email" name="email" prepend-inner-icon="mdi-email" type="email" class="rounded-0" outlined></v-text-field> -->
                  <v-text-field v-model.trim="credentials.password" label="Enter your password" name="password" prepend-inner-icon="mdi-lock" type="password" class="rounded-0" outlined></v-text-field>
                  <v-text-field v-model.trim="credentials.passwordConfirmation" label="Re-enter password" name="passwordConfirmation" prepend-inner-icon="mdi-lock-outline" type="password" class="rounded-0" outlined @keypress.enter="signup(credentials)"></v-text-field>
                  <v-btn @click="signup(credentials)" class="rounded-0" color="#000000" x-large block dark>Signup</v-btn>
                  <v-card-actions class="text--secondary">
                    <v-spacer></v-spacer>
                    Already have an account?
                    <router-link class="pl-2" style="color: #000000" :to="{ name: 'Login' }">Login</router-link>
                    
                  </v-card-actions>
                </v-form>
              </v-card-text>
              <v-card-actions class="ml-6 mr-6 text-center">
                <p>By continuing, you agree to Fedorae Education's <a href="#" class="pl-2" style="color: #000000">Policy</a> and <a href="#" class="pl-2" style="color: #000000">Terms of Use</a></p>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
  <!-- <div>
    <h2>Signup</h2>
    <div>
      <label for="username">아이디: </label>
      <input type="text" id="username" v-model.trim="credentials.username">
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input type="password" id="password" v-model.trim="credentials.password">
    </div>
    <div>
      <label for="passwordConfirmation">비밀번호 확인: </label>
      <input 
        type="password"
        id="passwordConfirmation"
        v-model.trim="credentials.passwordConfirmation"
        @keypress.enter="signup(credentials)"  
      >
    </div>
    <button @click="signup(credentials)">회원가입</button>
  </div> -->
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
        passwordConfirmation: '',
      },
    }
  },
  methods: {
    signup: function (credentials) {
      axios({
        url: `${SERVER_URL}/accounts/signup/`,
        method: 'post',
        data: credentials,
      })
      .then((res) => {
        console.log(res)
        this.$router.push({ name: 'Login'})
      })
      .catch((err) => {
        console.log(err)
      })
    },
  }
}
</script>

<style>

</style>