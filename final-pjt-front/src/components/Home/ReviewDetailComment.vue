<template>
  <v-container class="pa-0">
    <v-card outlined>
      <v-row>
        <v-col cols="12 pb-0">
          <v-card-title class="pb-0">
            <v-row>
              <v-col cols="10" class="py-1 px-2">
                <h5 class="font card-title">{{ comment.commentusername }}</h5>
              </v-col>
              <v-col cols="2" class="py-1 pl-5">
                <div v-if="comment.user === user_id">
                  <v-dialog v-model="dialog" persistent width="60%">
                    <template v-slot:activator="{ on, attrs }">
                      <v-icon left small>fas fa-pencil-ruler</v-icon>
                      <a v-bind="attrs" v-on="on"  style="color: grey" class="a-tag">수정</a>
                    </template>

                    <v-card>
                      <v-card-title>
                        <span class="font-h3">댓글 수정</span>
                      </v-card-title>

                      <v-card-text>
                        <v-text-field v-model.trim="information.content" label="Write your comment" type="text" outlined></v-text-field>
                      </v-card-text>

                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="primary" class="font" text @click="updateComment(information)">수정</v-btn>
                        <v-btn color="error" class="font" text @click="dialog = false">취소</v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
                  <v-icon left small class="pl-4">fas fa-trash-alt</v-icon>
                  <a @click="deleteComment" style="color: grey" class="a-tag">삭제</a>
                </div>
              </v-col>
            </v-row>
          </v-card-title>
        </v-col>

        <v-col cols="12">
          <p class="ml-3 mb-5 card-text font">{{ comment.content }}</p>
          <p class="ml-3 mb-2 card-text font">{{ comment.created_at }}</p>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script>
import axios from 'axios'
import Swal from 'sweetalert2'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  data: function () {
    return {
      information: {
        content: this.comment.content,
      },
      dialog: false,
    }
  },

  props: {
    comment: {
      type: Object
    },
    idx: {
      type: Number
    },
    user_id: {
      require: true
    }
  },

  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `Bearer ${token}`
      }
      return config
    },

    updateComment: function (information) {
      if (!information.content) {
        Swal.fire({
          icon: 'warning',
          text: '댓글 내용을 작성해주세요.',
        })
        return 
      }
      const headers = this.setToken()
      axios({
        url: `${SERVER_URL}/community/reviews/${this.$route.params.category}/comment/${this.comment.pk}/`,
        method: 'put',
        data: information,
        headers: headers,
      })
      .then(() => {
        this.$emit('update-comment', this.idx, this.information.content)
        this.dialog = false
      })
      .catch((err) => {
        console.log(err)
      })
    },

    deleteComment: function () {
      const headers = this.setToken()
      axios({
        url: `${SERVER_URL}/community/reviews/${this.$route.params.category}/comment/${this.comment.pk}/`,
        method: 'delete',
        headers: headers,
      })
      .then(() => {
        this.$emit('delete-comment', this.idx)
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
}
</script>

<style>
.a-tag {
  display: inline-block;
  text-decoration: none;
  font-size: 15px;
  font-weight: bold;
  font-family: 'Gowun Dodum', sans-serif;
}
</style>