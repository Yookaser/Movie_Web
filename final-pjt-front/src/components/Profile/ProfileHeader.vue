<template>
  <v-container class="fill-height" fluid text-center>
    <v-row>
      <v-col>      
        <v-row justify="space-between">
          <v-col cols="1"></v-col>
          <v-col cols="3" class="px-0">
            <v-btn color="error" @click="select(0)">찜한 영화</v-btn>
          </v-col>
          <v-col cols="3" class="px-0">
            <v-btn color="error" @click="select(1)">영화 리뷰</v-btn>
          </v-col>
          <v-col cols="3" class="px-0">
            <v-btn color="error" @click="select(2)">배우 리뷰</v-btn>
          </v-col>
          <v-col cols="1"></v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  data: function () {
    return {
      user_id: Number,
    }
  },

  props: {
    username: {
      type: String,
      required: true
    },
    choice: Number,
  },

  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `Bearer ${token}`
      }
      return config
    },

    getUserId: function () {
      const headers = this.setToken()
      axios({
        url: `${SERVER_URL}/accounts/getuserdata/`,
        method: 'get',
        headers,
      })
      .then((res) => {
        this.user_id = res.data.user_id
      })
      .catch((err) => {
        console.log(err)
      })
    },

    select: function (num) {
      this.$emit('user-choice', num)
    }
  },

  created: function () {
    this.getUserId()
  },
}
</script>

<style>

</style>