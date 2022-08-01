import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/client/HomeView.vue'
import { urlPath } from '@/utils/index'

const routes = [
  {
    path: urlPath.HOME.path,
    component: HomeView
  },
  {
    path: urlPath.ABOUT.path,
    component: () => import('../views/client/AboutView.vue')
  },
  {
    path: urlPath.LIST_POSTS.path,
    component: () => import('../views/client/ListPosts.vue')
  },
  {
    path: urlPath.ADMIN.path,
    component: () => import('../views/admin/HomeView.vue')
  },
  {
    path: urlPath.ADMIN_POST.path,
    component: () => import('../views/admin/Posts/list.vue')
  },
  {
    path: urlPath.ADMIN_POST_DETAIL.path,
    component: () => import('../views/admin/Posts/form.vue')
  },
  {
    path: urlPath.ADMIN_CATEGORY.path,
    component: () => import('../views/admin/Category/list.vue')
  },
  {
    path: urlPath.ADMIN_CATEGORY_DETAIL.path,
    component: () => import('../views/admin/Category/form.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
