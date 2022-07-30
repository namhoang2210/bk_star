<template>
    <div class="relative antialiased bg-gradient-to-r from-pink-300 via-purple-300 to-indigo-400 min-h-screen">
        <admin-header/>
        <div class="bg-white m-10 rounded-lg min-h-[450px] p-10">
            <div class="flex justify-between items-center">
                <div class="text-xl font-semibold text-purple-700">Tạo Danh Mục</div>
                <button class="text-white px-4 py-2 bg-green-500 rounded hover:bg-green-600" onclick="history.back()" type="submit">Quay về</button>
            </div>
            <div id="editor">
                <div class="mt-6">
                    <label for="default-input" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Tên Danh Mục</label>
                    <input
                        v-model="category.name"
                        type="text" id="default-input" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    >
                </div>
                <div class="mt-6">
                    <label for="default-input" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Mô Tả Danh Mục</label>
                    <input
                        v-model="category.description"
                        type="text" id="default-input" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    >
                </div>
                <div class="mt-6">
                    <label for="default-input" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Ảnh Danh Mục</label>
                    <input
                        v-model="category.image"
                        type="text" id="default-input" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    >
                </div>
                <button
                    @click="onSave()"
                    class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full mt-6"
                >
                    Save
                </button>
            </div>
        </div>
    </div>
</template>

<script>
import {defineComponent, onMounted, ref} from 'vue'
import { AdminHeader } from '@/components'
import { useRoute, useRouter } from 'vue-router'
import { bk_axios } from '@/plugins'
import { endpoint, urlPath } from '@/utils'

export default defineComponent({
  components: {
    AdminHeader
  },
  setup() {
    const route = useRoute()
    const router = useRouter()
    const { id } = route.query
    console.log(id, typeof(id))

    const category = ref({
      name: null,
      description: null,
      image: null
    })

    const onSave = async () => {
      if (category.value.name === null || category.value.description === null || category.value.image === null) {
        return
      }
      try {
        await bk_axios.post(endpoint.CATEGORY, category.value)
        alert('create successful')
        await router.push({
          path: urlPath.ADMIN_CATEGORY.path
        })
      } catch (e) {
        const error = e
      }
    }

    const getCategory = async () => {
      try {
        const response = await bk_axios.get(`${endpoint.CATEGORY}${id}`)
        category.value = response.data
      } catch (e) {
        const error = e
      }
    }

    onMounted(() => {
      if (id !== '0') {
        getCategory()
      }
    })

    return {
      category,
      onSave
    }
  }
})
</script>

