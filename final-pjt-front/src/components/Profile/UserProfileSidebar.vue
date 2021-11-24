<template>
  <v-card class="mx-auto">
    <v-container class="fill-height" fluid text-center justify-center align-center >
      <v-row dense>
        <v-col cols="12" class="mx-auto mt-4">
          <v-img class="v-avatar image" src="https://www.gravatar.com/avatar/default?s=200&r=pg&d=mm"/>
        </v-col>
      </v-row>
      
      <v-card-text class="mt-4"> 
        <span class="text-h4"> {{additional.nickname}} </span>
        <v-divider></v-divider>
        <div class="text-h5 text-start">
          <v-icon left color="red">fas fa-birthday-cake</v-icon> {{additional.birth_date}}
        </div>
        <div class="mt-4 text-h7 text-start">
         {{additional.context}}
        </div>
      </v-card-text> 

      <v-card-actions>
        <v-dialog
          v-model="dialog"
          persistent
          width="60%"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              v-if="isadditional"
              color="primary"
              v-bind="attrs"
              v-on="on"
              elevation="5"
              @click="check"
            >수정
            </v-btn>
            <v-btn
              v-else
              color="primary"
              v-bind="attrs"
              v-on="on"
              elevation="5"
            >생성
            </v-btn>
          </template>

          <v-card>
            <v-card-title>
              <span v-if="isadditional" class="headline">상세 정보 수정</span>
              <span v-else class="headline">상세 정보 생성</span>
            </v-card-title>
            <br>
            <v-card-text>
              <v-text-field
                v-model.trim="information.nickname"
                label="닉네임"
                type="text"
                outlined
              ></v-text-field>
              <v-menu
                ref="menu"
                v-model="menu"
                :return-value.sync="information.birth_date"
                :close-on-content-click="false"
                transition="scale-transition"
                offset-y
                min-width="auto"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field
                    outlined
                    v-model="information.birth_date"
                    label="생년월일"
                    prepend-icon="mdi-calendar"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker
                  v-model="information.birth_date"
                  no-title
                  scrollable
                >
                  <v-spacer></v-spacer>
                  <v-btn
                    text
                    color="primary"
                    @click="$refs.menu.save(information.birth_date)"
                  >
                    OK
                  </v-btn>
                  <v-btn
                    text
                    color="primary"
                    @click="menu = false"
                  >
                    Cancel
                  </v-btn>
                </v-date-picker>
              </v-menu>
              <v-textarea
                v-model.trim="information.context"
                label="자기소개"
                outlined
              ></v-textarea>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn v-if="isadditional" color="primary" @click="additionalChange(information, 1)">확인</v-btn>
              <v-btn v-else color="primary"  @click="additionalChange(information, 0)">확인</v-btn>
              <v-btn color="error"  @click="dialog = false">취소</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-card-actions>
    </v-container>
  </v-card>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  props: {
    additional: {
      required: true
    },
    isadditional: {
      required: true
    }
  },

  data: function () {
    return {
      information: {
        nickname: this.additional.nickname,
        birth_date: this.additional.birth_date,
        context: this.additional.context,
      },
      dialog: false,
      menu: false,
      modal: false,
      menu2: false,
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
    additionalChange: function (information, flag) {
      const headers = this.setToken()
      if (!information.nickname) {
        return alert('닉네임을 작성해주세요.')
      }
      if (!information.birth_date) {
        return alert('생일을 입력해주세요.')
      }
      if (!information.context) {
        return alert('소개글을 작성해주세요.')
      }

      if (flag) {
        axios({
          url: `${SERVER_URL}/accounts/additional/`,
          method: 'put',
          data: information,
          headers,
        })
        .then((res) => {
          this.dialog = false
          this.additional = res.data
        })
        .catch((err) => {
          console.log(err)
        })
      } else {
        axios({
          url: `${SERVER_URL}/accounts/additional/`,
          method: 'post',
          data: this.information,
          headers,
        })
        .then((res) => {
          this.dialog = false
          this.isadditional = true
          this.additional = res.data
        })
        .catch((err) => {
          console.log(err)
        })
      }
    },
    check: function () {
      this.information = this.additional
    }
  },

  mounted: function () {
    console.log(this.additional)
  }
}
</script>

<style>

</style>