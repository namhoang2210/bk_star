<template>
  <div class="relative antialiased bg-gradient-to-r from-pink-300 via-purple-300 to-indigo-400 min-h-screen">
    <AdminHeader msg="Welcome to Website"/>
    <div class="bg-white m-10 rounded-lg min-h-[450px] p-10">
      <div class="md:flex justify-between items-center">
        <div class="text-xl font-semibold text-purple-700">Danh sách danh mục</div>
        <button
            class="text-white mt-6 md:mt-0 px-4 py-2 bg-green-500 rounded hover:bg-green-600"
            @click="clickAddCategory()"
        >
          Thêm Danh Mục
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
                Tên danh mục
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
            <tr v-for="category in categories" :key="category.id" class="whitespace-nowrap ">
              <td class="px-6 py-4 text-sm text-gray-500 text-center">
                1
              </td>
              <td class="px-6 py-4 max-w-[300px] truncate">
                <button class="text-sm text-gray-900 font-medium text-blue-600">
                  <span>{{ category.name }}</span>
                </button>
              </td>
              <td class="px-6 py-4 text-center">
                <div class="text-sm text-gray-500">{{ category.time }}</div>
              </td>
              <td class="px-6 py-4 text-sm text-gray-500 text-center">

              </td>
              <td class="px-6 py-4 flex justify-center">
                <button class="px-4 py-1 text-sm text-white bg-blue-400 rounded">Edit</button>
              </td>
              <td class="px-6 py-4">
                <button class="px-4 py-1 text-sm text-white bg-red-400 rounded">Delete</button>
              </td>
            </tr>
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
import {defineComponent} from "vue";
import {urlPath} from '@/utils'
import {AdminHeader} from '@/components'
import {useRouter} from 'vue-router'

export default defineComponent({
  components: {
    AdminHeader
  },
  setup() {
    const router = useRouter()

    const categories = [
      { id: 1, name: 'Dang Muc 1', time: '10:30:24 - 06/24/2022' },
      { id: 1, name: 'Dang Muc 2', time: '10:30:24 - 06/24/2022' },
    ]

    const clickAddCategory = () => {
      router.push({
        path: urlPath.ADMIN_CATEGORY_DETAIL.path
      })
    }
    return {
      clickAddCategory,
      categories
    }
  }
})
</script>

