<template>
  <div>
    <v-container>
      <v-row>
        <v-col cols="12" sm="3" offset-sm="1">
          <v-hover v-slot="{hover}" open-delay="200">
            <v-card :elevation="hover ? 16:2" :class="{'on-hover': hover}">
              <v-img class="image-fit" :src="posterPath" alt="poster"/></v-card>
          </v-hover>
        </v-col>

        <v-col cols="12" sm="7">
          <h1 class="grey--text font-weight-bold mt-5 font">{{ this.movie.title }}</h1>
          <v-row>
            <v-col cols="12" sm="3">
              <v-rating :value="movie.vote_average / 2" color="amber" dense half-increments readonly size="25"></v-rating>
            </v-col>
            <v-col cols="12" sm="4">
              <div class="grey--text font-weight-bold font">평점: {{ movie.vote_average * 10 }}% | 개봉일: {{ movie.release_date }}</div>
            </v-col>
            <v-col cols="12" sm="5">
              <div class="grey--text font-weight-bold font">장르:
                <span v-for="(item, index) in movie.genres" :key="index" class="ml-1">{{ item.name }}
                  <span v-if="(movie.genres.length - 1 != index)">,</span>
                </span>
              </div>
            </v-col>
          </v-row>
          
          <v-col cols="12">
            <p class="mt-5 grey--text subheader font-h3">{{ movie.overview }}</p>
          </v-col>
          <v-col cols="12">
            <h2 class="grey--text font">제작진</h2>
            <div v-for="(crew, index) in movie.credits.crew" :key="index" class="mt-3 ml-5">
              <div v-if="index < 2" class="">
                <h3 class="grey--text font">{{ crew.name }}</h3>
                <span class="grey--text font">{{ crew.job }}</span>
              </div>
            </div>
          </v-col>

          <v-row>
            <v-col cols="12" sm="1" class="ml-6">
              <v-dialog v-model="dialog1" persistent width="65%">
                <template v-slot:activator="{ on, attrs }">
                  <v-btn tile color="error" v-bind="attrs" v-on="on" @click.prevent="openYouTubeModel" class="font">
                    <v-icon left>far fa-play-circle</v-icon>예고편
                  </v-btn>
                </template>

                <v-card>
                  <v-card-title>
                    <span class="font-h2">{{ movie.title }}</span>
                  </v-card-title>

                  <v-card-text>
                    <div class="iframe-container">
                      <img :src="mediaURL" v-if="!isVideo" />
                      <iframe allowfullscreen v-if="isVideo" :src="mediaURL"></iframe>
                    </div>
                  </v-card-text>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="error" class="font" @click="dialog1=false">Close</v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </v-col>

            <v-col cols="12" sm="1" class="ml-6">

              <v-btn v-if="isincart" tile color="error" class="ml-2 font" @click="myCart">
                <v-icon left>fas fa-heart</v-icon>싫어요
              </v-btn>
              <v-btn v-else tile color="error" class="ml-2 font" @click="myCart">
                <v-icon left>far fa-heart</v-icon>좋아요
              </v-btn>
            </v-col>

            <v-col cols="12" sm="1" class="ml-8">
              <v-btn tile color="error" class="ml-2 font" @click="islogin($route.params.id)">
                <v-icon left>fas fa-plus</v-icon>리뷰 쓰기
              </v-btn>
            </v-col>

            <v-col cols="12" sm="1" class="ml-14">
              <v-btn tile color="error" class="ml-2 font" dark @click.stop="dialog2 = true">
                <v-icon left>fas fa-star</v-icon>한줄평
              </v-btn>

              <v-dialog v-model="dialog2">
                <v-card class="pl-5 pt-5" min-width="500px">
                 <p class="font-h2">{{ movie.title }}</p>

                  <v-card-text class="pl-0">
                    <v-text-field v-model.trim="rating.content" label="content" name="content" type="text" outlined></v-text-field>
                      <div class="text-center">
                        <v-rating v-model="rating.rank" color="yellow darken-3" background-color="grey darken-1" empty-icon="$ratingFull" half-increments hover large></v-rating>
                      </div>
                  </v-card-text>
                  
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="green darken-1" text @click="addRating()" class="font">등록</v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </v-col>

          </v-row>
        </v-col>
      </v-row>

      <v-row>
        <v-divider class="my-4"></v-divider>
        <v-col cols="12">
          <v-row>
            <v-col cols="12" sm="6">
              <review-list :category="'movie'"></review-list>
            </v-col>
            <v-col cols="12" sm="6">
              <rating-list ref="modifyRating" :category="'movie'"></rating-list>
            </v-col>
          </v-row>
        </v-col>

        <v-divider class="mt-2"></v-divider>
        <v-col cols="12">
          <Actors :actors="movie.credits.cast" />
        </v-col>
        <v-divider class="mt-2"></v-divider>
        <v-col cols="12" class="mb-5">
          <Images :images="background.images" />
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import axios from 'axios'
import Swal from 'sweetalert2'
import Actors from '@/components/Home/Actors'
import Images from '@/components/Home/Images'
import ReviewList from '@/components/Home/ReviewList'
import RatingList from '@/components/Home/RatingList'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  components: {
    Actors,
    Images,
    ReviewList,
    RatingList,
  },
  data() {
    return {
      movie: {
        credits: {
          crew: {},
        },
      },
      rating: {
        content: '',
        rank: 0,
      },
      background: {
        backdrop_path: '',
        images: {
          backdrops: [],
        }
      },
      user_id: Number,
      isincart: false,
      israting: false,
      rating_pk: 0,
      isVideo: false,
      mediaURL: "",
      dialog1: false,
      dialog2: false,
    }
  },
  watch: {
    "$route.params.id": {
      handler() {
        this.fetchMovie(this.$route.params.id)
      },
      imediate: true,
    }
  },

  methods: {
    async fetchMovie(movieId) {
      const response1 = await this.$http.get(
        "/movie/" + movieId + "?append_to_response=credits,videos,images&language=ko"
      )
      this.movie = response1.data
      
      const response2 = await this.$http.get(
        "/movie/" + movieId + "?append_to_response=images"
      )
      this.background = response2.data
    },
    openYouTubeModel() {
      this.mediaURL = this.youtubeVideo()
      this.isVideo = true
    },
    youtubeVideo() {
      if (!this.movie.videos) return
      return (
        "https://www.youtube.com/embed/" + this.movie.videos.results[0].key
      )
    },
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `Bearer ${token}`
      }
      return config
    },
    islogin(movie_pk) {
      const token = localStorage.getItem('jwt')
      if(token) {
        this.$router.push({ name: 'ReviewCreate', params: { category: 'movie', id: movie_pk }})
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

    getUserId: function () {
      const headers = this.setToken()
      axios({
        url: `${SERVER_URL}/accounts/getuserdata/`,
        method: 'get',
        headers,
      })
      .then((res) => {
        this.user_id = res.data.user_id
        this.isReview()
        this.iscart()
      })
      .catch((err) => {
        console.log(err)
      })
    },

    isReview: function () {
      axios({
        url: `${SERVER_URL}/ratings/movie/${this.$route.params.id}/${this.user_id}/`,
        method: 'get',
      })
      .then((res) => {
        if (res.data.length) {
          this.israting = true
          this.rating.content = res.data[0]['content']
          this.rating.rank = res.data[0]['rank']
          this.rating_pk = res.data[0]['pk']
        }
      })
      .catch((err) => {
        console.log(err)
      })
    },

    iscart: function () {
      const headers = this.setToken()
      axios({
        url: `${SERVER_URL}/accounts/movies/`,
        method: 'get',
        headers,
      })
      .then((res) => {
        if (res.data.find(el => el.movie == this.$route.params.id)) {
          this.isincart = true
        }
      })
      .catch((err) => {
        console.log(err)
      })
    },

    myCart: function () {
      const headers = this.setToken()
      if (headers['Authorization'] === "Bearer null") {
        Swal.fire({
          icon: 'warning',
          text: '로그인이 필요합니다!',
        }).then(() => {
          this.$router.push('/login')
        })
        return
      }
      axios({
        url: `${SERVER_URL}/accounts/movies/`,
        method: 'post',
        data: {
          movie_pk: this.$route.params.id
        },
        headers,
      })
      .then(() => {
        if (this.isincart) {
          this.isincart = false
        } else {
          this.isincart = true
          }
      })
      .catch((err) => {
        console.log(err)
      })
    },

    addRating: function () {
      const headers = this.setToken()
      if (!this.rating.content) {
        Swal.fire({
          icon: 'warning',
          text: '내용을 작성해주세요.',
        })
        return 
      }
      if (!this.rating.rank) {
        Swal.fire({
          icon: 'warning',
          text: '평점을 입력해주세요.',
        })
        return 
      }
      if (this.israting) {
        axios({
          url: `${SERVER_URL}/ratings/movie/${this.rating_pk}/update/`,
          method: 'put',
          data: this.rating,
          headers,
        })
        .then ((res) => {
          this.dialog2 = false
          this.$refs.modifyRating.modifyRating(res.data, 0)
        })
        .catch ((err) => {
          console.log(err)
        })
      } else {
        axios({
          url: `${SERVER_URL}/ratings/movie/${this.$route.params.id}/create/`,
          method: 'post',
          data: this.rating,
          headers,
        })
        .then ((res) => {
          this.dialog2 = false
          this.$refs.modifyRating.modifyRating(res.data, 1)
        })
        .catch ((err) => {
          console.log(err)
        })
      }    
    },
  },

  created: function () {
    this.fetchMovie(this.$route.params.id)
    this.getUserId()
  },

  computed: {
    posterPath() {
      if (this.movie.poster_path) {
        return "http://image.tmdb.org/t/p/w500/" + this.movie.poster_path
      } else {
        return "http://via.placeholder.com/571x856"
      }
      
    },
  },

}
</script>

<style>
.iframe-container {
  position: relative;
  overflow: hidden;
  padding-top: 56.25%;
}
.iframe-container iframe {
  border: 0;
  height: 100%;
  left: 0;
  position: absolute;
  top: 0;
  width: 100%;
}

.image-fit {
  width: auto;
  height: 100%;
  object-fit: cover;
}
</style>