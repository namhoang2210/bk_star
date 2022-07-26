<template>
<div class="relative antialiased bg-gradient-to-r from-pink-300 via-purple-300 to-indigo-400 min-h-screen">
    <Header msg="Welcome to Website"/>
   <div class="bg-white m-10 rounded-lg min-h-[450px] p-10">
        <div class="md:flex justify-between items-center">
            <div class="text-xl font-semibold text-purple-700">Danh sách bài đăng</div>
            <router-link to="/admin/posts/create">
                <button class="text-white mt-6 md:mt-0 px-4 py-2 bg-green-500 rounded hover:bg-green-600">Thêm bài viết</button>
            </router-link>
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
                            <tr class="whitespace-nowrap ">
                                <td class="px-6 py-4 text-sm text-gray-500 text-center">
                                    1
                                </td>
                                <td class="px-6 py-4 max-w-[300px] truncate">
                                    <button class="text-sm text-gray-900 font-medium text-blue-600">
                                        <a href="http://funtap-laravel.herokuapp.com/admin/posts/view/2">Hackathon 2022 - Đấu trường dành cho những cá nhân và đội phát triển sản phẩm</a>
                                    </button>
                                </td>
                                <td class="px-6 py-4 text-center">
                                    <div class="text-sm text-gray-500">
                                        10:30:24 - 06/24/2022
                                    </div>
                                </td>
                                <td class="px-6 py-4 text-sm text-gray-500 text-center">
                                    
                                </td>
                                <td class="px-6 py-4 flex justify-center">
                                    <a href="http://funtap-laravel.herokuapp.com/admin/posts/edit/2" class="px-4 py-1 text-sm text-white bg-blue-400 rounded">Edit</a>
                                </td>
                                <td class="px-6 py-4">
                                    <a href="http://funtap-laravel.herokuapp.com/admin/posts/delete/2" class="px-4 py-1 text-sm text-white bg-red-400 rounded">Delete</a>
                                </td>
                            </tr>
                                                    <tr class="whitespace-nowrap  bg-gray-100 ">
                                <td class="px-6 py-4 text-sm text-gray-500 text-center">
                                    2
                                </td>
                                <td class="px-6 py-4 max-w-[300px] truncate">
                                    <button class="text-sm text-gray-900 font-medium text-blue-600">
                                        <a href="http://funtap-laravel.herokuapp.com/admin/posts/view/1">Chương trình teambuilding One Team One Dream - Một đội ngũ, một giấc mơ</a>
                                    </button>
                                </td>
                                <td class="px-6 py-4 text-center">
                                    <div class="text-sm text-gray-500">
                                        16:27:50 - 06/22/2022
                                    </div>
                                </td>
                                <td class="px-6 py-4 text-sm text-gray-500 text-center">
                                    
                                </td>
                                <td class="px-6 py-4 flex justify-center">
                                    <a href="http://funtap-laravel.herokuapp.com/admin/posts/edit/1" class="px-4 py-1 text-sm text-white bg-blue-400 rounded">Edit</a>
                                </td>
                                <td class="px-6 py-4">
                                    <a href="" class="px-4 py-1 text-sm text-white bg-red-400 rounded">Delete</a>
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
import Header from '@/components/admin/Header.vue'

export default {
  components: {
    Header
  }
}
</script>

