<template>
    <div class="relative antialiased bg-gradient-to-r from-pink-300 via-purple-300 to-indigo-400 min-h-screen">
        <admin-header/>
        <div class="bg-white m-10 rounded-lg min-h-[450px] p-10">
            <div class="flex justify-between items-center">
                <div class="text-xl font-semibold text-purple-700">Tạo bài đăng</div>
                <button class="text-white px-4 py-2 bg-green-500 rounded hover:bg-green-600" onclick="history.back()" type="submit">Quay về</button>
            </div>

            <div id="editor" class="mt-2">
                <div class="mt-6">
                    <label for="default-input" class="block mb-2 text-sm font-medium text-gray-900 ">Tiêu đề bài đăng</label>
                    <input
                        v-model="posts.title"
                        type="text" id="default-input" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 "
                    >
                </div>
                <label for="default" class="block mt-6 mb-2 text-sm font-medium text-gray-900 ">Danh mục bải đăng</label>
                <select
                    v-model="posts.category"
                    id="default"
                    class="bg-gray-50 border border-gray-300 text-gray-900 mb-6 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 "
                >
                    <option
                        v-for="category in categories" :key="category.id"
                        :value="category.id"
                        :selected="posts.category === category.id"
                    >
                        {{ category.name }}
                    </option>
                </select>
                <div class="my-6">
                    <label for="default-input" class="block mb-2 text-sm font-medium text-gray-900 ">Ảnh bài đăng</label>
                    <input
                        v-model="posts.image"
                        type="text" id="default-input" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 "
                    >
                </div>
                <div class="mt-6 mb-6">
                    <label for="default-input" class="block mb-2 text-sm font-medium text-gray-900 ">Sub content</label>
                    <input
                        v-model="posts.sub_content"
                        type="text" id="default-input" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 "
                    >
                </div>
                <vue-editor v-model="posts.content"/>
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
// @ is an alias to /src
import { defineComponent, onMounted, ref } from 'vue'
import { AdminHeader } from '@/components'
import { VueEditor } from 'vue3-editor'
import { endpoint, urlPath } from '@/utils'
import { bk_axios } from '@/plugins'
import { useRouter, useRoute } from 'vue-router'


export default defineComponent({
  components: {
    AdminHeader,
    VueEditor
  },
  setup() {
    const router = useRouter()
    const route = useRoute()
    const { id } = route.query

    const posts = ref({
      category: null,
      content: null,
      title: null,
      image: null
    })

    const categories = ref([])

    const getCategory = async () => {
      try {
        const response = await bk_axios.get(endpoint.CATEGORY)
        categories.value = response.data
      } catch (e) {
        const error = e
      }
    }

    const create = async () => {
      try {
        await bk_axios.post(endpoint.POST, posts.value)
        alert('create successful')
        await router.push({
          path: urlPath.ADMIN_POST.path
        })
      } catch (e) {
        const error = e
      }
    }

     const update = async () => {
      try {
        await bk_axios.put(endpoint.POST, posts.value)
        alert('update successful')
        await router.push({
          path: urlPath.ADMIN_POST.path
        })
      } catch (e) {
        const error = e
      }
    }

    const onSave = async () => {
      if (posts.value.title === null || posts.value.content === null || posts.value.category === null) {
        return
      }
      console.log(id === '0', id)
      if (id === '0') await create()
      if (id !== '0') await update()
    }

    const getPosts = async () => {
      try {
        const response = await bk_axios.get(`${endpoint.POST}${id}`)
        posts.value = response.data
      } catch (e) {
        const error = e
      }
    }
    onMounted(async () => {
      await getCategory()
      if (id !== '0')
        getPosts()
    })

    return {
      categories,
      onSave,
      posts
    }
  }
})
</script>

