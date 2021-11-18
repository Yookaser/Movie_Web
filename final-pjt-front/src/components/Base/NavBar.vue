<template>
  <nav>
    <v-app-bar app color="primary" dark>

      <v-icon class="mr-2">fas fa-video</v-icon>  <!-- 수정: 우리 로고 넣기 -->
      <v-toolbar-title>SSAFY-6</v-toolbar-title>  <!-- 수정: 우리 서비스명 넣기 -->
      <v-btn text class="ml-2" to="/">Movies</v-btn>
      <v-btn text class="ml-2" to="/actor-list">Actors</v-btn>
      <!-- <v-btn text class="ml-2" to="/">Profile</v-btn>
      <v-btn text class="ml-2" to="/">Contact</v-btn> -->

      <v-spacer></v-spacer>
      <div>
        <v-autocomplete
        class="mt-4"
        clearable
        hide-no-data
        hide-selected
        color="white"
        label="search"
        prepend-inner-icon="search"
        flat
        :items="movies"
        item-text="title"
        item-value="id"
        id="search"
        >
          <template v-slot:item="{item}">
            <v-btn text :to="`/movie/${item.id}`">{{item.title}}</v-btn>
          </template>
        </v-autocomplete>
      </div>

      <div v-if="!isLoggedIn">
        <v-btn text class="ml-2" :to="{ name: 'Signup' }">Signup</v-btn>
        <v-btn text class="ml-2" :to="{ name: 'Login' }">Login</v-btn>
      </div>

      <div v-else>
        <v-btn icon>
          <v-badge color="green" content="2" overlap>  <!-- 수정: content 수정? -->
            <v-icon>far fa-bell</v-icon>
          </v-badge>
        </v-btn>
        <v-badge bordered bottom color="green" dot offset-x="10" offset-y="10">
          <v-avatar size="40">
            <v-img src="https://images.dog.ceo/breeds/pitbull/IMG_20190826_121528_876.jpg"></v-img>  <!-- 수정: 유저의 프로필 이미지 넣기 -->
          </v-avatar>
        </v-badge>
        <v-btn text @click="logout" class="ml-2" to="#">Logout</v-btn>
      </div>

    </v-app-bar>
  </nav>
</template>

<script>
import { mapState } from 'vuex'

export default {
  data:()=>({
    drawer: null,
    model: '',
    search: null,
    movies: []
  }),
  mounted() {
    this.loadMovies()
  },
  methods: {
    logout: function () {
      localStorage.removeItem('jwt')
      this.$store.dispatch('Logout')
      this.$router.push({ name: 'Login' })
    },
    loadMovies: async function() {
      try{
        const response = await this.$http.get("/movie/popular")
        this.movies = response.data.results
      }catch(error){
        console.log(error)
      }
    }
  },
  computed: {
    ...mapState([
      'isLoggedIn',
    ])
  }
}
</script>

<style>

</style>