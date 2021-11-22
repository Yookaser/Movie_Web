import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Signup from '../views/Signup.vue'
import Login from '../views/Login.vue'

import MovieDetail from '../components/Home/MovieDetail.vue'
import ActorList from '../components/Home/ActorList.vue'
import ActorDetail from '../components/Home/ActorDetail.vue'
import ReviewCreate from '../components/Home/ReviewCreate.vue'
import ReviewList from '../components/Home/ReviewCreate.vue'
import ReviewDetail from '../components/Home/ReviewDetail.vue'
import ReviewUpdate from '../components/Home/ReviewUpdate.vue'

import CommunityHome from '../components/Community/CommunityHome.vue'

import Recommendation from '../components/Recommendation.vue'


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
    component: ActorList
  },
  {
    path: "/actor/:id",
    name: "ActorDetail",
    component: ActorDetail
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
  // 5. Review 기능
  {
    path: '/review-create/:category/:id',
    name: 'ReviewCreate',
    component: ReviewCreate
  },
  {
    path: '/reviews-list/:category/:id',
    name: 'ReviewList',
    component: ReviewList
  },
  {
    path: '/reviews-detail/:category/:category_id/:id',
    name: 'ReviewDetail',
    component: ReviewDetail
  },
  {
    path: '/reviews-update/:category/:category_id/:id',
    name: 'ReviewUpdate',
    component: ReviewUpdate,
    props: true
  },
  // 6. Community 기능
  {
    path: '/community-home',
    name: '/CommunityHome',
    component: CommunityHome
  },
  // 7. Recommendation 기능
  {
    path: '/recommendation',
    name: '/Recommendation',
    component: Recommendation
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
  scrollBehavior() { 
    return { x: 0, y: 0 } 
  },
})

export default router