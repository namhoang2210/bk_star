<template>
  <div class="fixed w-full top-0 z-50">
    <div class="bg-white">
      <nav class="container px-6 md:px-[10%] py-6 mx-auto md:flex md:justify-between md:items-center">
        <div class="flex items-center justify-between">
          <router-link to="/" class=" text-xl font-bold text-[#0d2f4b] md:text-2xl lg:text-3xl flex items-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 md:h-8 md:w-8 text-yellow-500" fill="none"
                 viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round"
                    d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"/>
            </svg>
            <h1>BK-Star</h1>
          </router-link>
          <!-- Mobile menu button -->
          <div @click="showMenu = !showMenu" class="flex md:hidden">
            <button
                type="button"
                class="
                text-gray-800
                hover:text-gray-400
                focus:outline-none focus:text-gray-400
              "
            >
              <svg viewBox="0 0 24 24" class="w-6 h-6 fill-current">
                <path
                    fill-rule="evenodd"
                    d="M4 5h16a1 1 0 0 1 0 2H4a1 1 0 1 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2z"
                ></path>
              </svg>
            </button>
          </div>
        </div>


        <!-- Mobile Menu open: "block", Menu closed: "hidden" -->
        <ul :class="showMenu ? 'flex' : 'hidden'" class="
            flex-col
            mt-8
            space-y-4
            md:flex
            md:space-y-0
            md:flex-row
            md:items-center
            md:space-x-10
            md:mt-0
          "
        >
          <li v-for="category in Categories" :key="category.id"
              class="text-sm lg:text-[16px] uppercase font-semibold text-gray-800 hover:text-blue-500"
          >
            <router-link :to="category.route">{{category.name}}</router-link>
          </li>
        </ul>
      </nav>
    </div>
  </div>
</template>
<script>
import { defineComponent, onMounted, ref } from "vue";
import { useRouter } from 'vue-router'
import { endpoint, urlPath } from '@/utils'
import { bk_axios } from '@/plugins'

export default defineComponent({
  // setup() {
  //   const categories = ref([])
  //   const showMenu = ref(true)
  //   const router = useRouter()
  //   const onClickCategory = (path) => {
  //     console.log('ss')
  //     router.push({
  //       name: urlPath.LIST_POSTS.name,
  //       params: {
  //         categoryId: path.id
  //       }
  //     })
  //   }
  //
  //   const onClickAbout = () => {
  //     router.push({
  //       path: urlPath.ABOUT.path,
  //     })
  //   }
  //
  //   const getData = async () => {
  //     try {
  //       const response = await bk_axios.get(endpoint.CATEGORY)
  //       categories.value = response.data
  //     } catch (e) {
  //       const error = e
  //     }
  //   }
  //
  //   onMounted(getData)
  //   return {
  //     onClickCategory,
  //     onClickAbout,
  //     showMenu,
  //     categories
  //   }
  // }
   setup() {
      const Categories = [
      {
        id: 1,
        name: 'Về chúng tôi',
        route: '/about'
      },
      {
        id: 2,
        name: 'Tin tức',
        route: '/news'
      },
      {
        id: 3,
        name: 'Giáo dục steam',
        route: '/courses'
      },
      {
        id: 4,
        name: 'Liên hệ',
        route: '/about'
      }
    ]

      return {
        Categories
      }
   }
})
</script>
