<template>
  <div>
    <v-hover 
      v-slot="{hover}"
      open-delay="200"
    >
      <v-card
        :elevation="hover ? 16 : 4"
        :class="{'on-hover': hover}"
        class="pa-0 rounded-lg"
        width="235px"
      >
        <router-link :to="`/actor/${actor.id}`">
          <v-img
            :src="profileImage"
            alt="Actor Image"
            class="pa-0 rounded-lg"
          />
        </router-link>
        <v-card-title class="font">{{ actor.name }}</v-card-title>
      </v-card>
    </v-hover>
  </div>
</template>

<script>
export default {
  props: {
    actor: {
      required: true,
    }
  },
  computed: {
    profileImage(){
      if (this.actor.profile_path) {
        return "https://image.tmdb.org/t/p/w235_and_h235_face/" + this.actor.profile_path
      } else {
        return "http://via.placeholder.com/235x235"
      }
    },
  }
}
</script>

<style>

</style>