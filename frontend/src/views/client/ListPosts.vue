<template>
  <Header/>
  <div class="bg-gray-100 py-16 lg:px-[13%] md:px-10 px-4 mt-20">
    <div class=" text-2xl text-blue-700 uppercase">
      <router-link to="/">Trang chủ</router-link> &gt; <a href="">Tin tức</a>
    </div>
    <div class="py-4 grid lg:grid-cols-3 md:grid-cols-2 gap-4">
      <sub-post v-for="post in posts" :key="post.id" :post="post"/>
    </div>
  </div>
  <Footer msg="This is Footer"/>
</template>

<script>
// @ is an alias to /src
import {Header, Footer, SubPost} from '@/components'
import { onMounted, ref } from 'vue'
import { bk_axios } from '@/plugins'
import {endpoint, urlPath} from '@/utils'
import { useRoute, useRouter } from 'vue-router'

export default {
  name: 'HomeView',
  components: {
    Header,
    Footer,
    SubPost
  },
  setup() {
    const route = useRoute()
    const { categoryId } = route.params

    const posts = ref([])
    const getPosts = async () => {
      try {
        const response = await bk_axios.get(`${endpoint.POST}category/${categoryId}`)
        posts.value = response.data
      } catch (e) {
        const error = e
      }
    }

    onMounted(async () => {
      await getPosts()
    })

    return {
      posts
    }
  }
}
</script>
