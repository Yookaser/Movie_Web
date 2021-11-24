<template>
  <div>
    <h2 class="mt-2 grey--text">평점</h2>
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
        class="my-border"
      >
        <template v-slot:item="{ item }">
          <tr @click="goDetail(item.pk)">
            <td>{{ item.username }}</td>
            <td>{{ item.rank }}</td>
            <td>{{ item.content }}</td>
            <td>{{ item.created_at }}</td>
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
        { text: '평점', value: 'rank' },
        { text: '내용', value: 'content' },
        { text: '작성일', value: 'created_at' },
      ],
      desserts: []
    }
  },

  methods: {
    receiveRatings: function () {
      axios({
        url: `${SERVER_URL}/ratings/${this.category}/${this.$route.params.id}/`,
        method: 'get'
      })
      .then((res) => {
        this.desserts = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },

    modifyRating: function(information, flag) {
      if (!flag) {
        for (let i = 0; i < this.desserts.length; i++) {
          if (this.desserts[i].pk === information.pk) {
            this.desserts[i].rank = information.rank
            this.desserts[i].content = information.content
            break
          }
        }
      } else {
        this.desserts.unshift(information)
      }
    },
  },

  created: function () {
    this.receiveRatings()
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