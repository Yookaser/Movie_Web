<template>
  <div>
    <h2 class="mt-2 grey--text">Actor</h2>
    <v-container>
      <v-row>
        <v-col cols="12" sm="3" v-for="(actor, index) in actors" :key="index">
          <v-hover v-slot="{hover}" open-delay="200">
            <v-card :elevation="hover ? 16:2" :class="{'on-hover': hover}">
              <router-link :to="`/actor/${actor.id}`">
                <v-img :src="actorProfileImage(actor)" />
              </router-link>
              <v-card-title class="subtitle-2">{{ actor.name }}</v-card-title>
            </v-card>
          </v-hover>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  props: {
    actors: {
      required: true,
    },
  },
  methods: {
    actorProfileImage(actor) {
      if (actor.profile_path) {
        return "http://image.tmdb.org/t/p/w300/" + actor.profile_path
      } else {
        return "http://via.placeholder.com/300x450"
      }
    }
  }
}
</script>

<style>

</style>