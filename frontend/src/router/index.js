import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/client/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    component: () => import('../views/client/AboutView.vue')
  },
  {
    path: '/news',
    component: () => import('../views/client/NewsView.vue')
  },
  {
    path: '/admin',
    component: () => import('../views/admin/HomeView.vue')
  },
  {
    path: '/admin/posts',
    component: () => import('../views/admin/Posts/list.vue')
  },
  {
    path: '/admin/posts/create',
    component: () => import('../views/admin/Posts/create.vue')
  },
  {
    path: '/admin/category',
    component: () => import('../views/admin/Category/list.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
