<template>
  <div>
    <v-container>
      <v-row>
        <v-col cols="12" sm="4">
          <v-hover v-slot="{ hover }" open-delay="200">
            <v-card :elevation="hover ? 16 : 2" :class="{'on-hover' : hover}">
              <div v-if="actor.profile_path">
                <v-img :src="'https://image.tmdb.org/t/p/w300/' + actor.profile_path" alt="" />
              </div>
              <div v-else>
                <v-img src="http://via.placeholder.com/571x856" alt="" />
              </div>              
              <v-card-text>
                <v-row class="mx-0 d-flex justify-center">
                  <v-btn class="mx-2" fab dark small color="error"
                  :href="'https://facebook.com/' + socialDetails.facebook_id">
                    <v-icon dark>
                      fab fa-facebook-f
                    </v-icon>
                  </v-btn>
                  <v-btn class="mx-2" fab dark small color="error"
                  :href="'https://instagram.com/' + socialDetails.instagram_id">
                  <v-icon dark>
                    fab fa-instagram
                  </v-icon>
                  </v-btn>
                  <v-btn class="mx-2" fab dark small color="error"
                  :href="'https://twitter.com/' + socialDetails.twitter_id">
                  <v-icon dark>
                    fab fa-twitter
                  </v-icon>
                  </v-btn>
                  <v-btn class="mx-2" fab dark small color="error">
                    <v-icon dark>
                      fas fa-globe-asia
                    </v-icon>
                  </v-btn>
                </v-row>
              </v-card-text>
            </v-card>
          </v-hover>
        </v-col>
        <v-col cols="12" sm="8">
          <h1 class="grey--text text--darken-3 mt-5">{{actor.name}}</h1>
          <v-row>
            <v-col cols="3">
              <v-btn text>
                <v-icon color="error">fas fa-birthday-cake</v-icon>
              </v-btn>
              <span class="grey--text">{{ actor.birthday }}  ({{ getAge(actor.birthday) }})</span>
            </v-col>
            <v-col cols="3">
              <v-btn tile color="error" class="ml-2" @click="islogin($route.params.id)">
                <v-icon left>fas fa-plus</v-icon>Create Review
              </v-btn>
            </v-col>
          </v-row>
          <p class="mt-5 grey--text text-darken-3 subheader">{{actor.biography}}</p>
          <h4 class="mt-1 grey--text">known For</h4>
          <v-row>
            <v-col cols="12" sm="3" :key="movie.id" v-for="movie in this.knownFor" class="mt-5">
              <v-hover v-slot="{ hover }" open-delay="200">
                <v-card :elevation="hover ? 16 : 2" :class="{'on-hover' : hover}">
                  <router-link :to="`/movie/${movie.id}`">
                    <v-img :src="movieImage(movie)"/>
                  </router-link>
                </v-card>
              </v-hover>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
      <v-divider class="mt-2"></v-divider>
      <h2 class="mt-2 grey--text">Credits</h2>
      <ul class="pl-5 mt-8">
        <li v-for="cast in castMovies" :key="cast.id">
          <strong>{{ castDetails(cast) }}</strong>
          <v-btn text :to="`/movie/${cast.id}`">
            {{ cast.title }}
          </v-btn>
          as {{ cast.character }}
        </li>
      </ul>
      <v-col cols="6">
          <review-list :category="'actor'"></review-list>
      </v-col>
    </v-container>
  </div>
</template>

<script>
import ReviewList from '@/components/Home/ReviewList'

export default {
  components: {
    ReviewList,
  },
  data () {
    return {
      socialDetails: [],
      actor: {},
      knownFor: [],
      castMovies: {},
    }
  },
  mounted () {
    this.fetchActor(this.$route.params.id)
    this.fetchCredits(this.$route.params.id)
    this.fetchSocial(this.$route.params.id)
  },
  methods: {
    async fetchActor(actorId) {
      const response = await this.$http.get(
        "/person/" + actorId
      )
      this.actor = response.data
    },
    async fetchCredits(actorId) {
      const response = await this.$http.get(
        "/person/" + actorId + "/combined_credits"
      )
      this.castMovies = response.data.cast
      .filter((x) => x.release_date)
      this.knownFor = response.data.cast
      .filter((x) => x.media_type =="movie")
      .slice(1, 9)
    },
    async fetchSocial(actorId){
      const response = await this.$http.get(
        "https://api.themoviedb.org/3/person/" + actorId + "/external_ids"
      )
      this.socialDetails = response.data
    },
    movieImage(movie){
      const posterPath = movie.poster_path
      if(posterPath) {
        return "https://image.tmdb.org/t/p/w185" + posterPath
      }
      return "https://via.placeholder.com/185x278"
    },
    castDetails(cast) {
      return parseInt(cast.release_date) + " ."
    },
    getAge(birthday) {
      birthday = new Date(birthday)
      const year = new Date().getFullYear() - birthday.getFullYear()
      const month = new Date().getMonth() - birthday.getMonth()
      const date = new Date().getDate() - birthday.getDate()
      return month > 0 || (month === 0 && date > 0) ? year:year-1
    },
    islogin(actor_pk) {
      const token = localStorage.getItem('jwt')
      if(token) {
        this.$router.push({ name: 'ReviewCreate', params: { category: 'actor', id: actor_pk }})
      } else {
        alert('리뷰를 쓰기 위해서는 로그인이 필요합니다.')
        this.$router.push('/login')
      }     
    },
  }
}
</script>

<style>

</style>