import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    LoadingStatus: false,

    isLoggedIn: false,
    username: ''
  },
  mutations: {
    startSpinner (state) {
      state.LoadingStatus = true;
    },
    endSpinner (state) {
        state.LoadingStatus = false;
    },

    LOGIN: function (state) {
      state.isLoggedIn = true
    },
    LOGOUT: function (state) {
      state.isLoggedIn = false
    },
  },
  actions: {
    Login: function ( { commit }, username ) {
      commit('LOGIN', username)
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
