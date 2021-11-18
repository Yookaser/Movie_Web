import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isLoggedIn: false,
  },
  mutations: {
    LOGIN: function (state) {
      state.isLoggedIn = true
    },
    LOGOUT: function (state) {
      state.isLoggedIn = false
    },
  },
  actions: {
    Login: function ( { commit } ) {
      commit('LOGIN')
    },
    Logout: function ( { commit } ) {
      commit('LOGOUT')
    },
  },
  getters: {
  },
  modules: {
  },
})
