<template>
  <div>
    <div v-if="movie_list.length">
      <carousel-3d :contols-visible="true" :clickable="false" :key="movie_list.length" :listData="movie_list" :height="500">
        <slide :index="i" :key="i" v-for="(movie, i) in movie_list">
          <figure>
            <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path" />
            <figcaption>
              <v-btn :to="`/movie/${movie.movie}`" text color="white">{{ movie.title }}</v-btn>
            </figcaption>
          </figure>
        </slide>
      </carousel-3d>
    </div>
    <div v-else class="mt-16 text-center">
      <h1 class="vibrate">아직 영화를 카트에 담지 않았어요!</h1>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import {Carousel3d, Slide} from "vue-carousel-3d"

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  data() {
    return {
      movie_list: [],
      user_id: Number,
    }
  },
  components: {
    Carousel3d,
    Slide,
  },

  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `Bearer ${token}`
      }
      return config
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
        this.getmovie()
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getmovie: function () {
      const headers = this.setToken()
      axios({
        url: `${SERVER_URL}/accounts/movies/`,
        method: 'get',
        headers,
      })
      .then((res) => {
        this.movie_list = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },

  created: function () {
    this.getUserId()
  }
}
</script>

<style>
.carousel-3d-container figure {
  margin: 0;
}
.carousel-3d-container figcaption {
  position: absolute;
  background-color: rgba(0,0,0,0.5);
  color: white;
  bottom: 0;
  padding: 15px;
  font-size: 12px;
  min-width: 100%;
  box-sizing: border-box;
}

@keyframes vibrate-1 {
  0% {
    -webkit-transform: translate(0);
            transform: translate(0);
  }
  20% {
    -webkit-transform: translate(-2px, 2px);
            transform: translate(-2px, 2px);
  }
  40% {
    -webkit-transform: translate(-2px, -2px);
            transform: translate(-2px, -2px);
  }
  60% {
    -webkit-transform: translate(2px, 2px);
            transform: translate(2px, 2px);
  }
  80% {
    -webkit-transform: translate(2px, -2px);
            transform: translate(2px, -2px);
  }
  100% {
    -webkit-transform: translate(0);
            transform: translate(0);
  }
}

.vibrate {
  animation: vibrate-1 0.3s linear infinite both;
}
</style>