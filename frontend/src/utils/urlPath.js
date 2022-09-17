const HOME = { path: '/', name: 'Home' }
const ABOUT = { path: '/about', name: 'About' }
const COURSES = { path: '/courses', name: 'Courses' }
const LIST_POSTS = {  path: '/news', name: 'ListPosts' }
const POSTS_DETAIL = {  path: '/posts/:postsId', name: 'PostsDetail' }
const ADMIN = {  path: '/admin', name: 'Admin' }
const ADMIN_POST = {  path: '/admin/posts', name: 'AdminPost' }
const ADMIN_POST_DETAIL = {  path: '/admin/posts/detail', name: 'AdminPostCreate' }
const ADMIN_CATEGORY = {  path: '/admin/category', name: 'AdminCategory' }
const ADMIN_CATEGORY_DETAIL = {  path: '/admin/category/detail', name: 'AdminCategory' }

export {
    HOME,
    ABOUT,
    COURSES,
    LIST_POSTS,
    ADMIN,
    ADMIN_POST,
    ADMIN_POST_DETAIL,
    ADMIN_CATEGORY,
    ADMIN_CATEGORY_DETAIL,
    POSTS_DETAIL
}