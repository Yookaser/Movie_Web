<template>
  <div class="mt-15">
    <v-container>
      <v-row>
        <v-col cols="12" sm="3">
          <v-col cols="12">
            <UserProfileSidebar
              :additional="additional"
              :isadditional="isadditional"
            />
          </v-col>

          <v-col cols="12">
            <ProfileHeader
              :username="username"
              :choice="choice"
              @user-choice="changeChoice"
            />
          </v-col>
        </v-col>

        <v-col cols="12" sm="9">
            <div v-show="choice === 0"><ProfileUserMovie/></div>
            <div v-show="choice === 1"><ProfileMovieReview/></div>
            <div v-show="choice === 2"><ProfileActorReview/></div>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import axios from 'axios'

import ProfileHeader from '@/components/Profile/ProfileHeader'
import UserProfileSidebar from '@/components/Profile/UserProfileSidebar'
import ProfileUserMovie from '@/components/Profile/ProfileUserMovie'
import ProfileMovieReview from '@/components/Profile/ProfileMovieReview'
import ProfileActorReview from '@/components/Profile/ProfileActorReview'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  components: {
      ProfileHeader,
      UserProfileSidebar,
      ProfileUserMovie,
      ProfileMovieReview,
      ProfileActorReview,
  },

  data () {
    return {
      username: this.$route.params.username,
      tweets: [],
      user_id: Number,
      additional: Object,
      moviereviews: Object,
      isadditional: true,
      choice: 0,
    }
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
    getAdditional: function () {
      const headers = this.setToken()
      axios({
        url: `${SERVER_URL}/accounts/additional/`,
        method: 'get',
        headers,
      })
      .then((res) => {
        this.additional = res.data
      })
      .catch(() => {
        this.isadditional = false
      })
    },
    changeChoice: function (num) {
      this.choice = num
    },
  },

  created: function () {
    this.getUserId()
    this.getAdditional()
  }
}
</script>

<style>

</style>