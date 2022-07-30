<template>
    <div class="relative antialiased bg-gradient-to-r from-pink-300 via-purple-300 to-indigo-400 min-h-screen">
        <admin-header/>
        <div class="bg-white m-10 rounded-lg min-h-[450px] p-10">
            <div class="flex justify-between items-center">
                <div class="text-xl font-semibold text-purple-700">Tạo bài đăng</div>
                <button class="text-white px-4 py-2 bg-green-500 rounded hover:bg-green-600" onclick="history.back()" type="submit">Quay về</button>
            </div>
            <div id="editor" class="mt-2">
                <label for="default" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-400">Default select</label>
                <select
                    v-model="posts.category"
                    id="default"
                    class="bg-gray-50 border border-gray-300 text-gray-900 mb-6 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                >
                    <option
                        v-for="category in categories" :key="category.id"
                        :value="category.id"
                        :selected="posts.category === category.id"
                    >
                        {{ category.name }}
                    </option>
                </select>
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
      category: 3,
      content: null
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

    const onSave = () => {
      console.log(posts.value)
    }

    onMounted(async () => {
      await getCategory()
      // if (id !== '0') getPosts()
    })

    return {
      categories,
      onSave,
      posts
    }
  }
})
</script>

