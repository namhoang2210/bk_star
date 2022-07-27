<template>
  <tr class="whitespace-nowrap ">
      <td class="px-6 py-4 text-sm text-gray-500 text-center">
          {{post.id}}
      </td>
      <td class="px-6 py-4 max-w-[300px] truncate">
          <button class="text-sm text-gray-900 font-medium text-blue-600">
              <a href="">{{post.title}}</a>
          </button>
      </td>
      <td class="px-6 py-4 text-center">
          <div class="text-sm text-gray-500">
              {{post.time}}
          </div>
      </td>
      <td class="px-6 py-4 text-sm text-gray-500 text-center">

      </td>
      <td class="px-6 py-4 flex justify-center">
          <a href="" class="px-4 py-1 text-sm text-white bg-blue-400 rounded">Edit</a>
      </td>
      <td class="px-6 py-4">
          <a href="" class="px-4 py-1 text-sm text-white bg-red-400 rounded">Delete</a>
      </td>
  </tr>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  props: {
    post: { type: Object, required: true }
  },
  setup() {
    return {}
  }
})

</script>

<style></style>