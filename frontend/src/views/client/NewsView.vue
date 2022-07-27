<template>
  <Header msg="Welcome to Website"/>

  <div class="bg-gray-100 py-16 lg:px-[13%] md:px-10 px-4 mt-20">
    <div class=" text-2xl text-blue-700 uppercase">
        <router-link to="/">Trang chủ</router-link> &gt; <a href="">Tin tức</a>
    </div>
    <div class="py-4 grid lg:grid-cols-3 md:grid-cols-2 gap-4">
      <sub-post v-for="post in subPosts" :key="post.id" :post="post" />
    </div>
  </div>
  <Footer msg="This is Footer"/>
</template>

<script>
// @ is an alias to /src
import { Header, Footer,SubPost } from '@/components'

export default {
  name: 'HomeView',
  components: {
    Header,
    Footer,
    SubPost
  },
  setup() {
    const subPosts =[
      {
        id: 1,
        title: 'Bài viết 1',
        image: 'https://images.unsplash.com/photo-1638153534717-fb17b6d19040?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=435&q=80',
        content: 'Kinh nghiệm phát hành game mobile với 5 ngôn ngữ chính: Tiếng Anh, Tiếng Việt, Tiếng Thái, Tiếng Trung Quốc và Tiếng Indonesia.',
        time: '22-10-2000'
      },
      {
        id: 2,
        title: 'Bài viết 2',
        image: 'https://images.unsplash.com/photo-1658527859107-66022662d851?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw3fHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60',
        content: 'Kinh nghiệm phát hành game mobile với 5 ngôn ngữ chính: Tiếng Anh, Tiếng Việt, Tiếng Thái, Tiếng Trung Quốc và Tiếng Indonesia.',
        time: '22-10-2000'
      },
    ]
    return {
      subPosts
    }
  }
}
</script>
