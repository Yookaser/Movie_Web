<template>
  <div class="detail-container">
    <v-card class="mx-auto mt-10 mb-10 p-5" width="65%" height="65%" elevation="0">
      <v-card-title class="font-h1">제목: {{ review.title }}</v-card-title>
      <v-card-subtitle class="justify-space-around grey--text font-weight-light">
        <v-row>
          <v-col cols="4">
            <v-card-text class="font-h3" cols="4">작성자: {{ review.reviewusername }}</v-card-text>
          </v-col>
          <v-col cols="4">
            <v-card-text class="font-h3" cols="4">작성 일시: {{ review.created_at.slice(0,10) }} {{ review.created_at.slice(11,19) }}</v-card-text>
          </v-col>
          <v-col cols="4">
            <v-card-text class="font-h3" cols="4">수정 일시: {{ review.updated_at.slice(0,10) }} {{ review.updated_at.slice(11,19) }}</v-card-text>
          </v-col>
        </v-row>
      </v-card-subtitle>
      <v-divider class="mt-2"></v-divider>

      <v-card-text class="font-h2">
        {{ review.content }}
      </v-card-text>
    
      <v-card-actions class="justify-center">
        <v-btn v-if="review.like_users.find(el => el == user_id)" class="mr-3" color="primary" elevation="5" @click="isLike(1)">
          <v-icon left small>fas fa-thumbs-up</v-icon>
          <p class="my-auto">{{review.like_users.length}}</p>
        </v-btn>
        <v-btn v-else class="mr-3" color="primary" elevation="5" @click="isLike(1)">
          <v-icon left small>far fa-thumbs-up</v-icon>
          <p class="my-auto">{{review.like_users.length}}</p>
        </v-btn>
        <v-btn v-if="review.dislike_users.find(el => el == user_id)" color="error" elevation="5" @click="isLike(0)">
          <v-icon left small>fas fa-thumbs-down</v-icon>
          <p class="my-auto">{{review.dislike_users.length}}</p>
        </v-btn>
        <v-btn v-else color="error" elevation="5" @click="isLike(0)">
          <v-icon left small>far fa-thumbs-down</v-icon>
          <p class="my-auto">{{review.dislike_users.length}}</p>
        </v-btn>
      </v-card-actions>
      <v-divider class="mt-2"></v-divider>

      <v-row>
        <v-col cols="9">
          <v-card-text class="font-h3">댓글 {{ review.comment_count }}개</v-card-text>
        </v-col>
        <v-col cols="3">
          <v-card-actions outlined v-if="review.user === user_id" class="justify-center">
            <router-link :to="{ name: 'ReviewUpdate', params: { category: $route.params.category, category_id: $route.params.category_id, id: $route.params.id, review: review }}">
              <v-btn class="mr-2 font" color="primary" elevation="5">수정</v-btn>
            </router-link>
            <v-btn class="ml-2 mr-2 font" color="error" elevation="5" @click="deleteReview">삭제</v-btn>
            <v-btn class="ml-2" color="#a0a0a0" @click="back($route.params.category, $route.params.category_id)">목록</v-btn>
          </v-card-actions>
        </v-col>
      </v-row>

      
      <div v-if="review.comments">
        <review-detail-comment v-for="(comment, idx) in review.comments" :key="idx" :comment="comment" :idx="idx" :user_id="user_id" @update-comment="updateComment" @delete-comment="deleteComment" class="list my-5"></review-detail-comment>
      </div>
      <div v-else>
        <p>댓글을 달아주세요!</p>
      </div>
      <v-form class="mt-5">
        <v-row>
          <v-col cols="11">
            <v-text-field v-model.trim="information.content" label="Write your comment" name="comment" type="text" outlined class="mb-2"></v-text-field>
          </v-col>
          <v-col cols="1" class="pl-0">
            <div class="text-right">
              <v-btn @click="createcomment(information)" class="my-1 font" x-large color="primary" elevation="5">제출</v-btn>
            </div>
          </v-col>
        </v-row>
      </v-form>  
    </v-card>
  </div>
</template>

<script>
import axios from 'axios'
import Swal from 'sweetalert2'
import ReviewDetailComment from '@/components/Home/ReviewDetailComment'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  data: function () {
    return {
      review: {
        title: '',
        content: '',
        like_users: [],
        dislike_users: [],
      },
      information: {
        content: '',
      },
      user_id: Number,
    }
  },
  components: {
    ReviewDetailComment
  },

  methods: {
    receiveReviewDetail: function () {
      axios({
        url: `${SERVER_URL}/community/reviews/${this.$route.params.category}/${this.$route.params.id}/`,
        method: 'get',
      })
      .then((res) => {
        this.review = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },

    getUserId: function () {
      const headers = this.setToken()
      axios({
        url: `${SERVER_URL}/accounts/getuserdata/`,
        method: 'get',
        headers,
      })
      .then((res) => {
        this.user_id = res.data.user_id
      })
      .catch((err) => {
        console.log(err)
      })
    },

    isLike: function (flag) {
      const headers = this.setToken()
      if (headers['Authorization'] === "Bearer null") {
        Swal.fire({
          icon: 'warning',
          text: '로그인이 필요합니다!',
        }).then(() => {
          this.$router.push('/login')
        })
        return 
      }
      axios({
        url: `${SERVER_URL}/community/reviews/${this.$route.params.category}/${this.$route.params.id}/${flag}/`,
        method: 'post',
        headers,
      })
      .then((res) => {
        if (flag) {
          if (res.data.liked) {
            this.review.like_users.push(this.user_id)
          } else {
            const idx = this.review.like_users.indexOf(this.user_id)
            if (idx > -1){
              this.review.like_users.splice(idx, 1)
            }
          }
        } else {
          if (res.data.disliked) {
            this.review.dislike_users.push(this.user_id)
          } else {
            const idx = this.review.dislike_users.indexOf(this.user_id)
            if (idx > -1){
              this.review.dislike_users.splice(idx, 1)
            }
          }
        }
      })
      .catch((err) => {
        console.log(err)
      })
    },

    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `Bearer ${token}`
      }
      return config
    },

    createcomment: function (information) {
      const headers = this.setToken()

      if (headers['Authorization'] === "Bearer null") {
        Swal.fire({
          icon: 'warning',
          text: '로그인이 필요합니다!',
        }).then(() => {
          this.$router.push('/login')
        })
        return 
      }
      if (!information.content) {
        Swal.fire({
          icon: 'warning',
          text: '댓글 내용을 작성해주세요.',
        })
        return 
      }
      axios({
        url: `${SERVER_URL}/community/reviews/${this.$route.params.category}/${this.$route.params.id}/comment/`,
        method: 'post',
        data: information,
        headers,
      })
      .then((res) => {
        this.review.comments.push(res.data)
        this.review.comment_count += 1
        this.information.content = ''
      })
      .catch((err) => {
        console.log(err)
      })
    },

    updateComment: function (comment_idx, comment_content) {
      this.review.comments[comment_idx].content = comment_content
    },

    deleteComment: function (comment_idx) {
      this.review.comments.splice(comment_idx, 1)
    },

    deleteReview: function () {
      const headers = this.setToken()
      
      axios({
        url: `${SERVER_URL}/community/reviews/${this.$route.params.category}/${this.$route.params.id}/`,
        method: 'delete',
        headers,
      })
      .then(() => {
        const category_id = this.$route.params.category_id
        if (this.$route.params.category === 'movie') {
          this.$router.push({ name: 'MovieDetail', params: { id: category_id }})
        } else {
          this.$router.push({ name: 'ActorDetail', params: { id: category_id }})
        }
      })
      .catch((err) => {
        console.log(err)
      })
    },

    back: function (category, id) {
      if (category == 'actor') {
        this.$router.push({ name: 'ActorDetail', params: { id }})
      } else {
        this.$router.push({ name: 'MovieDetail', params: { id }})
      }
    }
  },

  created: function () {
    this.receiveReviewDetail()
    this.getUserId()
  },
}
</script>

<style>

</style>
