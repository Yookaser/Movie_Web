<template>
  <v-app >
    <v-main class="back">
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center" dense>
          <v-col cols="4">
            <clock></clock>
          </v-col>
          <v-col cols="12" sm="5" class="ml-12">
            <v-card elevation="0" class="transparent">
              <h1 class="mb-15">WIW</h1>
              <v-row justify="center">
                <v-col cols="12" sm="9">
                  <v-card-text>
                    <v-form>
                      <v-text-field dark v-model.trim="credentials.username" label="아이디를 입력해주세요" name="username" prepend-inner-icon="mdi-account" type="text" class="rounded-0" outlined></v-text-field>
                      <v-text-field dark v-model.trim="credentials.password" label="패스워드를 입력해주세요" name="password" prepend-inner-icon="mdi-lock" type="password" class="rounded-0" outlined></v-text-field>
                      <v-text-field dark v-model.trim="credentials.passwordConfirmation" label="패스워드를 다시 입력해주세요" name="passwordConfirmation" prepend-inner-icon="mdi-lock-outline" type="password" class="rounded-0" outlined @keypress.enter="signup(credentials)"></v-text-field>
                      <v-btn @click="signup(credentials)" class="rounded-0 font-weight-bold font" color="primary" x-large block dark>회원가입</v-btn>
                      <v-card-actions class="text--secondary white--text">
                        <v-spacer></v-spacer>
                        <h6 class="mt-2 white--text font">이미 가입하셨나요?</h6>
                        <router-link class="pl-2 font" style="color: #FFFFFF" :to="{ name: 'Login' }">로그인</router-link>
                      </v-card-actions>
                    </v-form>
                  </v-card-text>
                </v-col>
              </v-row>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
  
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL
import Clock from '@/views/Clock.vue'

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
  components: {
    Clock
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

<style scoped>
  @import url("https://fonts.googleapis.com/css?family=Sacramento&display=swap");
  .back {
      background: #0f3854;
      background: radial-gradient(ellipse at center,  #0a2e38  0%, #000000 70%);
      background-size: 100%;
  }

  .transparent {
   background-color: white;
   opacity: 1;
   border-color: transparent;
  }

  h1 {
    font-size: calc(20px + 18vh);
    line-height: calc(20px + 20vh);
  /*   text-shadow: 0 0 5px #f562ff, 0 0 15px #f562ff, 0 0 25px #f562ff,
      0 0 20px #f562ff, 0 0 30px #890092, 0 0 80px #890092, 0 0 80px #890092;
    color: #fccaff; */
    text-shadow: 0 0 5px #ffa500, 0 0 15px #ffa500, 0 0 20px #ffa500, 0 0 40px #ffa500, 0 0 60px #ff0000, 0 0 10px #ff8d00, 0 0 98px #ff0000;
      color: #fff6a9;
    font-family: "Sacramento", cursive;
    text-align: center;
    animation: blink 12s infinite;
    -webkit-animation: blink 12s infinite;
  }

  @-webkit-keyframes blink {
    20%,
    24%,
    55% {
      color: #111;
      text-shadow: none;
    }

    0%,
    19%,
    21%,
    23%,
    25%,
    54%,
    56%,
    100% {
  /*     color: #fccaff;
      text-shadow: 0 0 5px #f562ff, 0 0 15px #f562ff, 0 0 25px #f562ff,
        0 0 20px #f562ff, 0 0 30px #890092, 0 0 80px #890092, 0 0 80px #890092; */
    text-shadow: 0 0 5px #ffa500, 0 0 15px #ffa500, 0 0 20px #ffa500, 0 0 40px #ffa500, 0 0 60px #ff0000, 0 0 10px #ff8d00, 0 0 98px #ff0000;
      color: #fff6a9;
    }
  }

  @keyframes blink {
    20%,
    24%,
    55% {
      color: #111;
      text-shadow: none;
    }

    0%,
    19%,
    21%,
    23%,
    25%,
    54%,
    56%,
    100% {
  /*     color: #fccaff;
      text-shadow: 0 0 5px #f562ff, 0 0 15px #f562ff, 0 0 25px #f562ff,
        0 0 20px #f562ff, 0 0 30px #890092, 0 0 80px #890092, 0 0 80px #890092; */
    text-shadow: 0 0 5px #ffa500, 0 0 15px #ffa500, 0 0 20px #ffa500, 0 0 40px #ffa500, 0 0 60px #ff0000, 0 0 10px #ff8d00, 0 0 98px #ff0000;
      color: #fff6a9;
    }
  }
</style>