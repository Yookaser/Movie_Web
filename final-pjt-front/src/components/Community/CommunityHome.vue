<template>
  <v-sheet elevation="0">
    <v-tabs
      dark
      background-color="primary"
      next-icon="mdi-arrow-right-bold-box-outline"
      prev-icon="mdi-arrow-left-bold-box-outline"
      show-arrows
    >
      <v-tabs-slider color="yellow"></v-tabs-slider>
      <v-tab
        v-for="tab in tabs" 
        :key="tab.id" 
        :to="tab.route"
        class="font"
      >
        {{ tab.name }}
      </v-tab>
    </v-tabs>
    <router-view></router-view>
  </v-sheet>
</template>

<script>
export default {
  data() {
    return {
      activeTab: `/community-home/1`,

      tabs: [
        { id: 1, name: "영화 리뷰", route: `/community-home/1`},
        { id: 2, name: "배우 리뷰", route: `/community-home/2`}
      ]
    };
  }
};
</script>

