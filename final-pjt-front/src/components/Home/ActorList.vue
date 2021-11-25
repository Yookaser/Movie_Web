<template>
  <div class="mx-3">
    <h2 class="mt-2 grey--text font">인기 배우</h2>

    <v-container fluid>
      <v-row>
        <v-col
          class="col-sm-2"
          v-for="actor in actorList"
          :key="actor.id"
        >
          <ActorListCard :actor="actor" />
        </v-col>

        <v-col
          cols="12"
          class="d-flex justify-center mt-5"
        >
          <v-btn
            class="mx-2"
            fab dark small
            color="error"
            v-on:click.prevent="previous(currentPage-1)"
          >
            <v-icon dark>
              fas fa-step-backward
            </v-icon>
          </v-btn>
          <v-btn
            class="mx-2"
            fab dark small
            color="error"
            v-on:click.prevent="next(currentPage+1)"
          >
            <v-icon dark>
              fas fa-step-forward
            </v-icon>
          </v-btn>
        </v-col>
      </v-row>
    </v-container>

  </div>
</template>

<script>
import ActorListCard from '@/components/Home/ActorListCard'

export default {
  data () {
    return {
      actorList: [],
      currentPage: 1,
    }
  },
  components: {
    ActorListCard,
  },
  mounted(){
    this.fetchActorList(this.currentPage)
  },
  methods: {
    async fetchActorList(page){
      try{
        const response = await this.$http.get(
          "/person/popular?page=" + page
        )
        this.actorList = response.data.results
      } catch (error) {
        console.log(error)
      }
    },
    previous() {
      if (this.currentPage > 1) {
        return this.fetchActorList(this.currentPage -= 1)
      }
    },
    next() {
      return this.fetchActorList(this.currentPage += 1)
    },
  }

}
</script>

<style>

</style>