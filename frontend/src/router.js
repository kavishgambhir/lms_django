import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import QuizList from './views/QuizList.vue'
import SignUp from './views/SignUp.vue'
import Calendar from './views/Calendar.vue'
import About from './views/About.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/quizes',
      name: 'quizes',
      component: QuizList
    },
    {
      path: '/sign-up',
      name: 'sign-up',
      component: SignUp
    },
    {
      path: '/calendar',
      name: 'calendar',
      component: Calendar
    },
     {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('./views/About.vue')
    }
  ]
})
