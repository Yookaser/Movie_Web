<template>
  <div>
    <h2 class="mt-2 grey--text">배경</h2>
    <div class="scroll">
      <div
        v-for="(image, index) in images"
        :key="index"
      >
        <v-img 
          width="500"
          :src="movieImage(image)"
          alt="Movie Background"
        >
        </v-img>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    images: {
      required: true,
    }
  },
  methods: {
    movieImage(image) {
      if (image.file_path) {
        return "https://image.tmdb.org/t/p/w500/" + image.file_path
      } else {
        return "https://via.placeholder.com/300x450"
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
  padding: 8px;
  text-decoration: none;
}
</style>