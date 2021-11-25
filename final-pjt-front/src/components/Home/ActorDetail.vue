<template>
  <div>
    <v-container>
      <v-row>
        <v-col cols="12" sm="3" offset-sm="1">
          <v-hover v-slot="{ hover }" open-delay="200">
            <v-card :elevation="hover ? 16 : 2" :class="{'on-hover' : hover}">
              <div v-if="actor.profile_path">
                <v-img :src="'https://image.tmdb.org/t/p/w300/' + actor.profile_path" alt="Actor Image" class="image-fit" />
              </div>
              <div v-else>
                <v-img src="http://via.placeholder.com/571x856" alt="No Image" />
              </div>

              <v-card-text>
                <v-row class="mx-0 d-flex justify-center">
                  <v-btn class="mx-4" fab dark small @click='gosocial("https://facebook.com/", socialDetails.facebook_id, actor.name, "페이스북")' :color="socialDetails.facebook_id ? '#4dd0e1' : '#B0BEC5'">
                    <v-icon dark>fab fa-facebook-f</v-icon>
                  </v-btn>
                  <v-btn class="mx-4" fab dark small @click='gosocial("https://instagram.com/", socialDetails.instagram_id, actor.name, "인스타그램")' :color="socialDetails.instagram_id ? '#4dd0e1' : '#B0BEC5'">
                    <v-icon dark>fab fa-instagram</v-icon>
                  </v-btn>
                  <v-btn class="mx-4" fab dark small @click='gosocial("https://twitter.com/", socialDetails.twitter_id, actor.name, "트위터")' :color="socialDetails.twitter_id ? '#4dd0e1' : '#B0BEC5'">
                    <v-icon dark>fab fa-twitter</v-icon>
                  </v-btn>
                </v-row>
              </v-card-text>
            </v-card>
          </v-hover>
        </v-col>

        <v-col cols="12" sm="7">
          <h1 class="grey--text text--darken-3 font-weight-bold mt-5 font">{{actor.name}}</h1>
          <v-row>
            <v-col cols="12" sm="3">
              <v-btn text>
                <v-icon color="error">fas fa-birthday-cake</v-icon>
              </v-btn>
              <span class="grey--text font">
                <span>{{ actor.birthday }}  ({{ getAge(actor.birthday) }})</span>
                <span v-if="actor.gender==2"> (남)</span>
                <span v-else> (여)</span>
              </span>
            </v-col>
            <v-col cols="12" sm="3">
              <v-btn tile color="error" class="ml-2 font" @click="islogin($route.params.id)">
                <v-icon left>fas fa-plus</v-icon>리뷰 쓰기
              </v-btn>
            </v-col>
          </v-row>

          <p class="mt-5 grey--text text-darken-3 subheader font">{{actor.biography}}</p>
          <div class="scroll">
            <v-col cols="12" sm="2" :key="movie.id" v-for="movie in this.knownFor" class="pa-0 mr-3">
              <v-hover v-slot="{ hover }" open-delay="200">
                <v-card class="pa-0 rounded-lg" max-width="170px" :elevation="hover ? 16 : 4" :class="{'on-hover' : hover}">
                  <router-link :to="`/movie/${movie.id}`">
                    <v-img max-height="241px" class="rounded-lg" alt="Movie Image" :src="movieImage(movie)"/>
                  </router-link>
                    <v-card-title v-if="movie.title.length > 8" class="rounded-lg font">{{ movie.title.slice(0, 8) }}...</v-card-title>
                    <v-card-title v-else class="rounded-lg font">{{ movie.title }}</v-card-title>
                </v-card>
              </v-hover>
            </v-col>
          </div>
        </v-col>
      </v-row>

      <v-row>
        <v-col cols="10" offset="1">
          <v-divider class="my-6"></v-divider>
          <review-list :category="'actor'"></review-list>

          <v-divider class="my-6"></v-divider>

          <h2 class="mt-2 grey--text font">크레딧</h2>
          <ul class="pl-5 mt-8">
            <li class="font grey--text" v-for="cast in castMovies" :key="cast.id">
              <strong> {{ castDetails(cast) }} </strong>
              <v-btn  class="font grey--text" text :to="`/movie/${cast.id}`">
                {{ cast.title }}
              </v-btn>
              as {{ cast.character }}
            </li>
          </ul>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import ReviewList from '@/components/Home/ReviewList'
import Swal from 'sweetalert2'

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
        "/person/" + actorId + "/combined_credits" + "?language=ko"
      )
      this.castMovies = response.data.cast
      .filter((x) => x.release_date)
      .sort(function (a, b){ return new Date(b.release_date) - new Date(a.release_date)})
      
      this.knownFor = response.data.cast
      .filter((x) => x.media_type =="movie")
      .filter((x) => x.poster_path)
      .sort(function (a, b){ return new Date(b.vote_average) - new Date(a.vote_average)})
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
      const month = new Date().getMonth() + 1 - birthday.getMonth()
      const date = new Date().getDate() - birthday.getDate()
      return month > 0 || (month === 0 && date > 0) ? year:year-1
    },
    islogin(actor_pk) {
      const token = localStorage.getItem('jwt')
      if(token) {
        this.$router.push({ name: 'ReviewCreate', params: { category: 'actor', id: actor_pk }})
      } else {
        Swal.fire({
          icon: 'warning',
          text: '로그인이 필요합니다!',
        }).then(() => {
          this.$router.push('/login')
        })
        return 
      }     
    },
    gosocial: function(base_url, socail_url, actor, social) {
      if (socail_url) {
        window.open(base_url+socail_url, "_blank")
      } else {
        Swal.fire({
          icon: 'warning',
          text: `${actor}님의 ${social} 페이지가 존재하지 않습니다.`,
        })
        return 
      }
    }
  }
}
</script>

<style>
.scroll {
  overflow: auto;
  overflow-y: hidden;
  white-space: nowrap;
}

div.scroll img {
  display: inline-block;
  text-align: center;
  text-decoration: none;
}

.image-fit {
  width: auto;
  height: 100%;
  object-fit: cover;
}
</style>