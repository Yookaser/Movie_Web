<template>
  <v-app>
    <NavBar />
    <v-main>
      <router-view/>
    </v-main>
    <Footer />
  </v-app>
</template>

<script>
import Footer from '@/components/Base/Footer'
import NavBar from '@/components/Base/NavBar'

export default {
  name: 'App',
  components: {
    NavBar,
    Footer
  },

  data: () => ({

  }),
}

</script>

