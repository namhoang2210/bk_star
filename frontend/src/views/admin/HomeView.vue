<template>
<div class="relative antialiased bg-gradient-to-r from-pink-300 via-purple-300 to-indigo-400 min-h-screen">
    <Header msg="Welcome to Website"/>
    <div class="px-10 min-h-[350px] mt-20">
        <div class="flex justify-center items-center bg-white mx-auto max-w-2xl rounded-lg p-16 md:my-32 lg:my-44">
            <h1 class="text-2xl font-medium uppercase text-center">Trang quản lí Admin BK-Star</h1>
        </div>
    </div>
</div>
</template>

<script>
// @ is an alias to /src
import Header from '@/components/admin/Header.vue'
import { bk_axios } from '@/plugins'

export default {
  name: 'HomeView',
  components: {
    Header
  },
  setup() {

    const getData = async () => {
      try {
        const response = await bk_axios.get('/test')
        console.log(response)
      } catch (e) {
        console.log(e)
      }
    }

    getData()
    return {}
  }
}
</script>

