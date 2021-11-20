<template>
  <div class="detail-container">
    <v-card class="mx-auto mt-10" width="65%" height="65%" elevation="0">
      <v-card-title>제목: {{ review.title }}</v-card-title>
      <v-card-subtitle class="mx-5 justify-space-around">
        <v-card-text cols="4">작성자: {{ review.reviewusername }}</v-card-text>
        <v-card-text cols="4">
          작성 일시: {{ review.created_at }}
          수정 일시: {{ review.updated_at }}
        </v-card-text>
      </v-card-subtitle>
      <v-divider class="mt-2"></v-divider>

      <v-card-text>
        {{ review.content }}
      </v-card-text>
    
      <v-card-actions class="justify-center">
        <v-btn
          v-if="review.like_users.find(el => el == user_id)"
          class="mr-3"
          color="primary"
          elevation="5"
          @click="isLike(1)"
        >
          좋아요취소
        </v-btn>
        <v-btn 
          v-else
          class="mr-3"
          color="primary"
          elevation="5"
          @click="isLike(1)"
        >
          좋아요
        </v-btn>
        <v-btn
          v-if="review.dislike_users.find(el => el == user_id)"
          color="error"
          elevation="5"
          @click="isLike(0)"
        >
          싫어요취소
        </v-btn>
        <v-btn
          v-else
          color="error"
          elevation="5"
          @click="isLike(0)"
        >
          싫어요
        </v-btn>
      </v-card-actions>
      <v-divider class="mt-2"></v-divider>

      <v-card-actions class="justify-center">
        <v-btn class="mr-3" color="primary" elevation="5" >수정</v-btn>
        <v-btn class="mr-3" color="primary" elevation="5" @click="deleteReview">삭제</v-btn>
      </v-card-actions>

      <v-card-text>
        댓글 개수: {{ review.comment_count }}
      </v-card-text>
      <div v-if="review.comments">
        <review-detail-comment
          v-for="(comment, idx) in review.comments"
          :comment="comment"
          :key="idx"
        >
        </review-detail-comment>
      </div>
      <div v-else>
        <p>댓글을 달아주세요!</p>
      </div>
      <v-form class="mt-5">
        <v-text-field
          v-model.trim="information.content"
          label="Write your comment"
          name="comment"
          type="text"
          outlined
          class="mb-2"
          @keypress.enter="createcomment(information)"
        >
        </v-text-field>
        <div class="text-right mb-4">
          <v-btn 
            @click="createcomment(information)"
            class="my-1"
            x-large 
            color="primary"
            elevation="5"
          >
           제출 
          </v-btn>
        </div>
      </v-form>  
    </v-card>
  </div>
</template>

<script>
import axios from 'axios'
import ReviewDetailComment from '@/components/Home/ReviewDetailComment'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  data: function () {
    return {
      review: {
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
    },

    isLike: function (flag) {
      const headers = this.setToken()
      if (headers['Authorization'] === "Bearer null") {
        alert('좋아요와 싫어요를 이용하기 위해서는 로그인이 필요합니다.')
        return this.$router.push('/login')
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
        alert('댓글을 쓰기 위해서는 로그인이 필요합니다.')
        return this.$router.push('/login')
      }
      if (!information.content) {
        return alert('댓글 내용을 작성해주세요.')
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

    deleteReview: function () {
      const headers = this.setToken()
      
      axios({
        url: `${SERVER_URL}/community/reviews/${this.$route.params.category}/${this.$route.params.id}`,
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
  },

  created: function () {
    this.receiveReviewDetail()
    this.getUserId()
  },
}
</script>

<style>

</style>
