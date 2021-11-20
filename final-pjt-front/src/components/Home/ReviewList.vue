<template>
  <div>
    <v-card>
      <v-card-title>
        리뷰
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
          <tr @click="goDetail(item.pk)">
            <td>{{ item.pk }}</td>
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
  props: {
    category: String
  },

  data: function () {
    return {
      search: '',
      headers: [
        {
          align: 'start',
          sortable: false,
          text: '순번',
          value: 'pk',
        },
        { text: '작성자', value: 'username' },
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
    goDetail: function (review_id) {
      this.$router.push({ name: 'ReviewDetail', params: { category: this.category, category_id: this.$route.params.id ,id: review_id }})
    },
  },

  created: function () {
    this.receiveReviews()
  }
}
</script>
