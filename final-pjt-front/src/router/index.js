import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Signup from '../views/Signup.vue'
import Login from '../views/Login.vue'

import MovieDetail from '../components/Home/MovieDetail.vue'
import ActorList from '../components/Home/ActorList.vue'
import ActorDetail from '../components/Home/ActorDetail.vue'

Vue.use(VueRouter)

const routes = [
  // 1. Main 화면
  {
    path: '/',
    name: 'Home',
    component: Home
  },

  // 2. Movie Detail
  {
    path: "/movie/:id",
    name: "MovieDetail",
    component: MovieDetail
  },
  // 3. Actor Detail
  {
    path:"/actor-list",
    name:"ActorList",
    component: ActorList,
  },
  {
    path: "/actor/:id",
    name: "actor",
    component: ActorDetail,
  },
  // 4. Account 기능
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router