<template>
  <div>
    <Header/>
    <Banner class="mt-20" msg="This is banner"/>
    <div class="lg:flex justify-between px-4 md:px-[15%] mt-10 md:mt-16">
      <div class="font-bold lg:text-5xl text-center lg:text-start text-2xl pb-6">GIEO MẦM SÁNG TẠO - DẪN HƯỚNG ĐAM MÊ</div>
      <div class="lg:w-1/2">
        <p>
          Bk-star thành lập năm 2014 mới mục đích đinh hưỡng-hưỡng dẫn cho các sinh viên back khoa tham gia cuộc
          thi robocon. Sau này với tâm huyết định hướng nghề nghiệp sớm và truyền dạy những kiến thức khoa học cho
          những học sinh cấp 1, 2, 3,
          TS.Phạm Văn Khương đã mở rộng Bk-star thành công ty chuyên về giáo dục, giáo dục stem và du học
        </p>
        <router-link to="/about" class="flex justify-center lg:justify-start">
          <button class="px-6 py-2 rounded bg-[#011858] text-white hover:bg-blue-700 mt-6 lg:mt-4">Về chúng tôi</button>
        </router-link>
      </div>
    </div>
  </div>

  <div class="grid  xl:grid-cols-2 mt-12 bg-white  mx-4 md:mx-[15%]">
    <sub-category v-for="(category,index) in categories" :key="category.id" :category="category" :index-category="index"/>
  </div>
  <section
      class="container mt-14 flex items-center justify-center h-[300px] md:h-[400px] lg:h-[520px] m-auto w-full bg-fixed bg-center bg-cover custom-img"
  >
    <div class="p-5 text-2xl text-white bg-purple-300 bg-opacity-50 rounded-xl">
      Đến với Bk-star để tiếp thực chiến với lập trình từ sớm
    </div>
  </section>
  <div class=" bg-white px-[15%] ">
    <div class="text-4xl font-semibold text-gray-800 text-center pt-14 uppercase">Tin tức - Sự kiện</div>
    <hr class="h-2 w-[50px] mx-auto bg-[#011858] mt-8 rounded-full">
    <div class="py-10 grid lg:grid-cols-3 gap-6">
      <sub-post v-for="post in subPosts" :key="post.id" :post="post" />
    </div>
  </div>

  <Footer msg="This is footer"/>
</template>

<script>
// @ is an alias to /src
import {defineComponent, ref, onMounted} from "vue";
import {Header, Banner, Footer, SubCategory, SubPost} from '@/components'
import {endpoint} from '@/utils'
import {bk_axios} from "@/plugins";

export default defineComponent({
  name: 'HomeView',
  components: {
    Header,
    Banner,
    Footer,
    SubCategory,
    SubPost
  },
  setup() {
    const subPosts = ref([])

    const getData = async () => {
      try {
        const { data } = await bk_axios.get(endpoint.POST)
        subPosts.value = data
      } catch (e) {
        console.log(e)
      }
    }

    onMounted(() => {
      getData()
    })

    return {
      subPosts
    }
  }
})
</script>
<style>
.custom-img {
  background-image: url("https://images.unsplash.com/photo-1657524433787-a30cefc92661?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1171&q=80");
}
</style>
