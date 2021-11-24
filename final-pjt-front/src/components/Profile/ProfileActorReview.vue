<template>
  <div>
    <h2 class="mt-2 grey--text">배우 리뷰</h2>
    <v-card elevation="0">
      <v-card-title>
        <v-spacer></v-spacer>
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Search"
          single-line
          hide-details
        >
        </v-text-field>
      </v-card-title>
      <v-data-table
        :headers="headers"
        :items="desserts"
        item-key="pk"
        :search="search"
      >
        <template v-slot:item="{ item }">
          <tr @click="goDetail(item.actor, item.pk)">
            <td>{{ item.username }}</td>
            <td>{{ item.title }}</td>
            <td>{{ item.created_at }}</td>
            <td>{{ item.like_users.length }}</td>
            <td>{{ item.dislike_users.length }}</td>
          </tr>
        </template>

      </v-data-table>
    </v-card>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  data: function () {
    return {
      search: '',
      headers: [
        {
          align: 'start',
          text: '작성자',
          value: 'username',
        },
        { text: '제목', value: 'title' },
        { text: '작성일', value: 'created_at' },
        { text: '추천', value: 'like_users.length' },
        { text: '비추천', value: 'dislike_users.length' },
      ],
      desserts: [],
      user_id: Number,
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
        this.receiveReviews()
      })
      .catch((err) => {
        console.log(err)
      })
    },
    receiveReviews: function () {
      axios({
        url: `${SERVER_URL}/community/user/actor/reviews/${this.user_id}`,
        method: 'get'
      })
      .then((res) => {
        this.desserts = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    goDetail: function (movie_id, review_id) {
      this.$router.push({ name: 'ReviewDetail', params: { category: "movie", category_id: movie_id , id: review_id }})
    },
  },

  created: function () {
    this.getUserId()
  }
}
</script>

<style>

</style>