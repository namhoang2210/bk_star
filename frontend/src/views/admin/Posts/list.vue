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
                           <AdminSubPost v-for="post in subPosts" :key="post.id" :post="post"/>
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
import { defineComponent } from "vue";
import { AdminHeader, AdminSubPost } from '@/components'
import { useRouter } from 'vue-router'
import { urlPath } from '@/utils'

export default defineComponent({
  components: {
    AdminHeader,
    AdminSubPost
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

    const router = useRouter()
    const clickAddPosts = () => {
      router.push({
        path: urlPath.ADMIN_POST_DETAIL.path
      })
    }

    return {
      subPosts,
      clickAddPosts
    }
  }
})
</script>

