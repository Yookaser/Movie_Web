<template>
  <v-row class="mt-1">
    <v-col cols="2" class="pl-6 pb-0">
      <v-text-field 
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
        outlined
      >
    </v-text-field>
    </v-col>
    <v-col cols="12" class="pt-3 pl-6 pr-6 pb-6">
    <v-data-table
      :headers="headers"
      :items="desserts"
      item-key="pk"
      :search="search"
      class="my-border font grey--text"
    >
      <template v-slot:item="{ item }" >
        <tr @click="goDetail(item.actor, item.pk)">      
          <td>{{ item.username }}</td>
          <td>{{ item.title }}</td>
          <td>{{ item.created_at.slice(0,10) }} {{ item.created_at.slice(11,19) }}</td>
          <td>{{ item.like_users.length }}</td>
          <td>{{ item.dislike_users.length }}</td>
        </tr>
      </template> 
    </v-data-table>
    </v-col>
  </v-row>
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
      desserts: []
    }
  },

  methods: {
    receiveReviews: function () {
      axios({
        url: `${SERVER_URL}/community/reviews/actor/list/`,
        method: 'get'
      })
      .then((res) => {
        this.desserts = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    goDetail: function (actor_id, review_id) {
      this.$router.push({ name: 'ReviewDetail', params: { category: "actor", category_id: actor_id ,id: review_id }})
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