import Vue from 'vue'
import Router from 'vue-router'

import Login from '@/components/Login'
import Users from '@/components/Users'
import Posts from '@/components/Posts'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'login',
      component: Login
    },
    {
      path: '/users/',
      name: 'users',
      component: Users
    },
    {
      path: '/posts/',
      name: 'posts',
      component: Posts
    }
  ]
})
