<template>
  <div id="example">
    <h2 class="mx-3 grey--text">개봉 예정 영화</h2>
    <carousel-3d
      :contols-visible="true"
      :clickable="false"
      :key="upcomingMovies.length"
      :listData="upcomingMovies"
      :height="500"
    >
    <slide :index="i" :key="i" v-for="(movie, i) in upcomingMovies">
      <figure>
        <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path" />
        <figcaption>
          <v-btn :to="`/movie/${movie.id}`" text color="white">{{ movie.title }}</v-btn>
        </figcaption>
      </figure>
    </slide>
    </carousel-3d>
  </div>
</template>

<script>
import {Carousel3d, Slide} from "vue-carousel-3d"

export default {
  data(){
    return{
      upcomingMovies: [],
    }
  },
  components: {
    Carousel3d,
    Slide,
  },
  mounted(){
    this.fetchUpcomingMovies()
  },
  methods: {
    moviePush: function (results) {
      const t_y = new Date().getFullYear()
      const t_m = new Date().getMonth() + 1
      const t_d = new Date().getDate()
      for (let i=0; i<results.length; i++) {
        const y = Number(results[i].release_date.slice(0, 4))
        const m = Number(results[i].release_date.slice(5, 7))
        const d = Number(results[i].release_date.slice(8, 10))

        if ((y > t_y) || (t_y === y && m > t_m) || (t_y === y && m === t_m && d > t_d) ) {
          this.upcomingMovies.push(results[i])
        }
      }
    },

    async fetchUpcomingMovies() {
      const response1 = await this.$http.get(
        "https://api.themoviedb.org/3/movie/upcoming?language=ko&page=1",
      )
      const response2 = await this.$http.get(
        "https://api.themoviedb.org/3/movie/upcoming?language=ko&page=2",
      )
      const response3 = await this.$http.get(
        "https://api.themoviedb.org/3/movie/upcoming?language=ko&page=3",
      )
      const response4 = await this.$http.get(
        "https://api.themoviedb.org/3/movie/upcoming?language=ko&page=4",
      )

      this.moviePush(response1.data.results)
      this.moviePush(response2.data.results)
      this.moviePush(response3.data.results)
      this.moviePush(response4.data.results)
    },
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

.next span,
.prev span {
  color: red
}
</style>