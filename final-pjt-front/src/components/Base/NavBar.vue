<template>
  <nav>
    <v-app-bar app color="primary" dark>

      <v-icon class="mr-2">fab fa-waze</v-icon>  <!-- 수정: 우리 로고 넣기 -->
      <v-toolbar-title>WIIW</v-toolbar-title>  <!-- 수정: 우리 서비스명 넣기 -->
      <v-btn text class="ml-2" to="/">영화</v-btn>
      <v-btn text class="ml-2" to="/actor-list">배우</v-btn>
      <v-btn text class="ml-2" to="/community-home/1">커뮤니티</v-btn>
      <v-btn text class="ml-2" to="/recommendation">추천</v-btn>
      <theme-toggle class="ml-2" />
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <div class="mr-6">
        <v-autocomplete
        class="mt-5"
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

        <router-link :to="`/profile/${username}`">
          <v-badge>
            <v-avatar size="50">
              <v-img src="https://images.dog.ceo/breeds/pitbull/IMG_20190826_121528_876.jpg"></v-img>  <!-- 수정: 유저의 프로필 이미지 넣기 -->
            </v-avatar>
          </v-badge>
        </router-link>
        <v-btn text @click="logout" class="ml-2" to="#">Logout</v-btn>
      </div>

    </v-app-bar>
  </nav>
</template>

<script>
import ThemeToggle from "../UI/ThemeToggle.vue"
import { mapState } from 'vuex'

export default {
  data:()=>({
    drawer: null,
    model: '',
    search: null,
    movies: [],
  }),
  components: { ThemeToggle },
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
      'username',
    ]),
  }
}

</script>

<style>

</style>