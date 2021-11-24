<template>
  <div>
     <div>
      <h2 class="mt-2 grey--text">출연진</h2>
      <div class="scroll">
        <div v-for="(actor, index) in actors" :key="index">
          <v-hover v-slot="{hover}" open-delay="200">
            <v-card :elevation="hover ? 16:4" :class="{'on-hover': hover}" width="200px" class="pa-0 rounded-lg">
              <router-link :to="`/actor/${actor.id}`">
                <v-img :src="actorProfileImage(actor)" alt="Actor Image" class="rounded-lg"/>
              </router-link>
              <v-card-title class="subtitle-2">{{ actor.name }}</v-card-title>
            </v-card>
          </v-hover>
        </div>
      </div>
    </div>
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
.scroll {
  overflow: auto;
  white-space: nowrap;
}

div.scroll div {
  display: inline-block;
  text-align: center;
  text-decoration: none;
}
</style>