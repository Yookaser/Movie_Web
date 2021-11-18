<template>
  <div>
    <PopularMovies />
    <v-divider class="mt-2"></v-divider>
    <UpcomingMovies />
  </div>
</template>

<script>
import PopularMovies from '@/components/Home/PopularMovies'
import UpcomingMovies from '@/components/Home/UpcomingMovies'

export default {
  name: 'Home',
  components: {
    PopularMovies,
    UpcomingMovies,
  }
}
</script>