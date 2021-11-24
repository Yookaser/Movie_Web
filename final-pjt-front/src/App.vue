<template>
  <v-app v-if="!$store.state.LoadingStatus">
    <NavBar />
    <v-main>
      <router-view/>
    </v-main>
    <Footer />
  </v-app>
  <v-app v-else>
    <spinner :loading="$store.state.LoadingStatus"/>
  </v-app>
</template>

<script>
import Footer from '@/components/Base/Footer'
import NavBar from '@/components/Base/NavBar'
import Spinner from '@/components/Spinner'

export default {
  name: 'App',
  components: {
    NavBar,
    Footer,
    Spinner,
  },
  data: () => ({

  }),
}

</script>

