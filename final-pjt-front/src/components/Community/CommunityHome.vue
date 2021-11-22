<template>
  <div>
    <v-container fluid>
      <v-row align="start" justify="center">
        <v-col cols="12">
          <h1 class="text-center">Home Dashboard</h1>
        </v-col>
      </v-row>
      <v-row align="start" justify="start">
        <v-col md="3">
  
          <v-card class="mx-auto">
            <v-img class="white--text" height="200px" :src="'https://placeimg.com/400/200/nature?rand=' + Math.random()">
              <v-card-title class="align-end fill-height">Lorem ipsum</v-card-title>
            </v-img>
  
            <v-card-text>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas eleifend elit quis lorem malesuada lobortis. Cras et est nec libero venenatis cursus.</v-card-text>
  
            <v-card-actions>
              <v-btn>Action</v-btn>
              <div class="flex-grow-1"></div>
              <v-btn icon>
                <v-icon>mdi-heart-outline</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
  
        </v-col>
        <v-col md="6">
  
          <v-card class="mx-auto">
            <v-img class="white--text" height="200px" :src="'https://placeimg.com/400/200/nature?rand=' + Math.random()">
              <v-card-title class="align-end fill-height">Lorem ipsum dolor sit amet</v-card-title>
            </v-img>
  
            <v-card-text>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas eleifend elit quis lorem malesuada lobortis. Cras et est nec libero venenatis cursus. Sed lacinia ut arcu eget dignissim. Phasellus eget dapibus mauris. Duis et interdum ex, eu
              pellentesque lectus. Phasellus gravida ligula in purus tincidunt vehicula nec sit amet orci. Donec et auctor sapien. Cras lobortis ante nisl, non faucibus sem luctus id. Quisque tristique ante eget pharetra posuere.</v-card-text>
  
            <v-card-actions>
              <v-btn color="primary">Action</v-btn>
              <v-btn color="accent" outlined>Action</v-btn>
              <div class="flex-grow-1"></div>
              <v-btn icon>
                <v-icon>mdi-email-outline</v-icon>
              </v-btn>
              <v-btn icon>
                <v-icon>mdi-heart-outline</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
  
        </v-col>
        <v-col md="3">
  
          <v-card class="mx-auto">
            <v-card-title>
              <p class="headline">Card List</p>
            </v-card-title>
  
            <v-list two-line>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>Item 1</v-list-item-title>
                  <v-list-item-subtitle>Item 1 description - Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas eleifend elit quis lorem malesuada lobortis. Cras et est nec libero venenatis cursus.</v-list-item-subtitle>
                </v-list-item-content>
                <v-list-item-action>
                  <v-btn icon>
                    <v-icon color="accent">mdi-star</v-icon>
                  </v-btn>
                </v-list-item-action>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>Item 2</v-list-item-title>
                  <v-list-item-subtitle>Item 2 description - Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas eleifend elit quis lorem malesuada lobortis. Cras et est nec libero venenatis cursus.</v-list-item-subtitle>
                </v-list-item-content>
                <v-list-item-action>
                  <v-btn icon>
                    <v-icon color="accent">mdi-star-half</v-icon>
                  </v-btn>
                </v-list-item-action>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>Item 3</v-list-item-title>
                  <v-list-item-subtitle>Item 3 description - Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas eleifend elit quis lorem malesuada lobortis. Cras et est nec libero venenatis cursus.</v-list-item-subtitle>
                </v-list-item-content>
  
                <v-list-item-action>
                  <v-btn icon>
                    <v-icon color="grey lighten-1">mdi-star-outline</v-icon>
                  </v-btn>
                </v-list-item-action>
              </v-list-item>
            </v-list>
  
            <v-card-actions>
              <v-btn color="accent" outlined>Action</v-btn>
              <div class="flex-grow-1"></div>
              <v-btn icon>
                <v-icon>mdi-email-outline</v-icon>
              </v-btn>
              <v-btn icon>
                <v-icon>mdi-heart-outline</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
  
        </v-col>
      </v-row>
      <v-row align="start" justify="start">
        <v-col md="6">
  
          <v-card class="mx-auto">
            <v-img class="white--text" height="200px" :src="'https://placeimg.com/600/200/nature?rand=' + Math.random()">
              <v-card-title class="align-end fill-height">Lorem ipsum dolor sit amet</v-card-title>
            </v-img>
  
            <v-card-text>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas eleifend elit quis lorem malesuada lobortis. Cras et est nec libero venenatis cursus.</v-card-text>
  
            <v-card-actions>
              <v-btn color="primary">Action</v-btn>
              <v-btn>Action</v-btn>
              <div class="flex-grow-1"></div>
              <v-btn icon>
                <v-icon>mdi-heart-outline</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
  
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
}
</script>

<style>

</style>