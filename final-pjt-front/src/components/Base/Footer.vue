<template>
  <v-footer dark padless>
    <v-card width="100%" flat tile class="primary white--text text-center">
      <v-card-text class="white--text font text-right pr-16">
        <strong>WIW Developer : 유동완, 이상훈</strong>
      </v-card-text>
    </v-card>
  </v-footer>
</template>

<script>
export default {
  data: () =>({
    icons:[
      'mdi-facebook',
      'mdi-twitter',
      'mdi-linkedin',
      'mdi-instagram'
    ]
  }),
}
</script>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&display=swap');

  .font{
    font-weight: bold;
    font-family: 'Gowun Dodum', sans-serif;
  }
</style>