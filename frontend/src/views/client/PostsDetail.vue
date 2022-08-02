<template>
  <Header/>
  <div class="bg-gray-100 py-16 lg:px-[13%] md:px-10 px-4 mt-16">
    <h1>{{ posts.title }}</h1>
<!--    <img style="margin: 0 auto" :src="posts.image"/>-->
    <div v-html="posts.content"></div>
  </div>
  <Footer msg="This is Footer"/>
</template>

<script>
import { defineComponent, onMounted, ref } from "vue";
import { endpoint } from '@/utils'
import { bk_axios } from '@/plugins'
import { useRoute } from "vue-router";
import { Footer, Header, SubPost } from "@/components";

export default defineComponent({
  components: {
    Header,
    Footer,
    SubPost
  },
  setup() {
    const route = useRoute()
    const { postsId } = route.params
    const posts = ref({})

    const getData = async () => {
      try {
        const { data } = await bk_axios.get(`${endpoint.POST}${postsId}`)
        posts.value = data
      } catch (e) {
        const error = e
      }
    }

    onMounted(() => {
      getData()
    })
    return {
      posts
    }
  }
})
</script>
