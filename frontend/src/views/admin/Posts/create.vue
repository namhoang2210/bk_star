<template>
    <div class="relative antialiased bg-gradient-to-r from-pink-300 via-purple-300 to-indigo-400 min-h-screen">
        <admin-header/>
        <div class="bg-white m-10 rounded-lg min-h-[450px] p-10">
            <div class="flex justify-between items-center">
                <div class="text-xl font-semibold text-purple-700">Tạo bài đăng</div>
                <button class="text-white px-4 py-2 bg-green-500 rounded hover:bg-green-600" onclick="history.back()" type="submit">Quay về</button>
            </div>
            <div id="editor"></div>

        </div>
    </div>
</template>

<script>
// @ is an alias to /src
import { defineComponent } from 'vue'
import { AdminHeader } from '@/components'

export default defineComponent({
  components: {
    AdminHeader
  }
})
</script>

