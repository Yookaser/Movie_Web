<template>
   <div>
    <v-container 
      class="fill-height fluid"
    >
      <v-row class="justify-center">
        <v-col cols="12" sm="8" md="7" lg="6">
          <v-card outlined>
            <h2 class="mt-5 ml-5 grey--text">리뷰 작성</h2>
            <v-img 
              src="@/assets/Arishem.png"
              alt="Arishem" 
              contain height="200"
            />
            <v-card-text>
              <v-form>
                <v-text-field v-model.trim="information.title" label="title" name="title" type="text" outlined></v-text-field>
                <v-textarea height="300px" v-model.trim="information.content" label="content" name="content"  type="text" outlined @keypress.enter="createreview(information)"></v-textarea>
                <div class="text-right">
                  <v-btn x-large color="primary" elevation="10" @click="createreview(information, $route.params.category, $route.params.id)">제출</v-btn>
                </div>
              </v-form>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
   </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Login',
  data: function () {
    return {
      information: {
        title: '',
        content: '',
      },
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
    createreview: function (information, category, id) {
      const headers = this.setToken()
      axios({
        url: `${SERVER_URL}/community/reviews/${category}/create/${id}/`,
        method: 'post',
        data: information,
        headers,
      })
      .then((res) => {
        this.$router.push({ name: 'ReviewDetail', params: { category: `${category}`, category_id: this.$route.params.id, id: `${res.data.pk}` }})
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