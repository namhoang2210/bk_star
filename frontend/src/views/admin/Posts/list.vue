<template>
<div class="relative antialiased bg-gradient-to-r from-pink-300 via-purple-300 to-indigo-400 min-h-screen">
    <AdminHeader msg="Welcome to Website"/>
   <div class="bg-white m-10 rounded-lg min-h-[450px] p-10">
        <div class="md:flex justify-between items-center">
            <div class="text-xl font-semibold text-purple-700">Danh sách bài đăng</div>
            <button
                class="text-white mt-6 md:mt-0 px-4 py-2 bg-green-500 rounded hover:bg-green-600" to="/admin/posts/detail"
                @click="clickAddPosts()"
            >
              Thêm bài viết
            </button>
        </div>

        <div class="w-full">
            <div class="border-b m-10 border-gray-200 shadow">
                     <table class="w-full table-auto">
                        <thead class="bg-gray-100 whitespace-nowrap">
                        <tr>
                            <th class="px-6 py-4 text-xs text-gray-500 w-24">
                                ID
                            </th>
                            <th class="px-6 py-2 text-xs text-gray-500 max-w-[130px]">
                                Tiêu đề
                            </th>
                            <th class="px-6 py-2 text-xs text-gray-500">
                                Thời gian tạo
                            </th>
                            <th class="px-6 py-2 text-xs text-gray-500">
                                Thời gian sửa
                            </th>
                            <th class="px-6 py-2 text-xs text-gray-500 w-24">
                                Chỉnh sửa
                            </th>
                            <th class="px-6 py-2 text-xs text-gray-500 w-24">
                                Xóa
                            </th>
                        </tr>
                        </thead>
                        <tbody class="bg-white">
                           <AdminSubPost v-for="post in posts" :key="post.id" :post="post"/>
                        </tbody>
                    </table>
                </div>
                <div class="mx-10"></div>
        </div>
    </div>
</div>
</template>

<script>
// @ is an alias to /src
import { defineComponent, ref} from "vue";
import { AdminHeader, AdminSubPost } from '@/components'
import { useRouter } from 'vue-router'
import { endpoint, urlPath } from '@/utils'
import {bk_axios} from "@/plugins";

export default defineComponent({
  components: {
    AdminHeader,
    AdminSubPost
  },
  setup() {

    const posts = ref([])
    const getPost = async () => {
      try {
        const response = await bk_axios.get(endpoint.POST)
        posts.value = response.data
      } catch (e) {
        const error = e
      }
    }

    getPost()

    const router = useRouter()
    const clickAddPosts = () => {
      router.push({
        path: urlPath.ADMIN_POST_DETAIL.path
      })
    }

    return {
      posts,
      clickAddPosts
    }
  }
})
</script>

