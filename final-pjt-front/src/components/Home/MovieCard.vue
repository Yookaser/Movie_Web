<template>
  <v-hover
  v-slot="{hover}"
  open-delay="200"
  >
  <v-card :elevation="hover ? 16:2" :class="{'on-hover' : hover}" class="rounded-lg">
    <router-link :to="`/movie/${movie.id}`">
    <v-img :src="posterPath" alt="Movie Poster" max-height="680px" class="rounded-lg"></v-img>
    </router-link>

    <v-card-title class="h2 pb-1 font">{{ movie.title }}</v-card-title>

    <v-card-text>
      <v-row align="center" class="mx-0">
        <v-rating :value="movie.vote_average / 2" color="amber" dense half-increments readonly size="20"> </v-rating>
        <div class="grey--text ml-4 font">
          {{ movie.vote_average  * 10 }} % | {{ movie.release_date }}
        </div>
      </v-row> 
      
      <div class="mt-5 h6 font">
        <span v-for="(genre, index) in movie.genre_ids" :key="genre">
          {{ genretypeName(genre, index) }}
        </span>
      </div>
    </v-card-text>
  </v-card>
  
  </v-hover>
</template>

<script>
export default {
  props: {
    movie: {
      required: true,
    },
    genres: {
      required: true,
    }
  },
  computed: {
    posterPath(){
      return "https://image.tmdb.org/t/p/w500/" + this.movie.poster_path
    }
  },
  methods: {
    genretypeName(geraId, index) {
      for(const item of this.genres) {
        if(item.id == geraId) {
          if(this.movie.genre_ids.length - 1 == index) {
            return item.name;
          } else {
            return item.name + ",";
          }
        }
      }
    }
  }
}
</script>

<style>

</style>