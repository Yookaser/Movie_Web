<template>
  <div>
    <h2 class="mt-2 grey--text font">리뷰</h2>
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
        class="my-border font grey--text"
      >
        <template v-slot:item="{ item }">
          <tr @click="goDetail(item.pk)">
            <td class="font">{{ item.username }}</td>
            <td class="font">{{ item.title }}</td>
            <td class="font">{{ item.created_at.slice(0,10) }} {{ item.created_at.slice(11,19) }}</td>
            <td class="font">{{ item.like_users.length }}</td>
            <td class="font">{{ item.dislike_users.length }}</td>
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
  props: {
    category: String
  },

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
      desserts: []
    }
  },

  methods: {
    receiveReviews: function () {
      axios({
        url: `${SERVER_URL}/community/reviews/${this.category}/list/${this.$route.params.id}/`,
        method: 'get'
      })
      .then((res) => {
        this.desserts = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    goDetail: function (id) {
      this.$router.push({ name: 'ReviewDetail', params: { category: this.category, category_id: this.$route.params.id ,id }})
    },
  },

  created: function () {
    this.receiveReviews()
  }
}
</script>

<style>
  tbody tr:nth-of-type(odd) {
    background-color: rgba(0, 0, 0, .05);
  }
  .my-border {
    border: 1px solid rgba(0, 0, 0, 0.37);
  }
</style>