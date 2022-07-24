<template>
  <div>
    <img
      class="ease-in duration-500 h-[350px] w-full object-cover"
      :src="category.img"
      alt=""
    >
  </div>
  <div class="p-6">
    <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1">
      <path stroke-linecap="round" stroke-linejoin="round" d="M11 4a2 2 0 114 0v1a1 1 0 001 1h3a1 1 0 011 1v3a1 1 0 01-1 1h-1a2 2 0 100 4h1a1 1 0 011 1v3a1 1 0 01-1 1h-3a1 1 0 01-1-1v-1a2 2 0 10-4 0v1a1 1 0 01-1 1H7a1 1 0 01-1-1v-3a1 1 0 00-1-1H4a2 2 0 110-4h1a1 1 0 001-1V7a1 1 0 011-1h3a1 1 0 001-1V4z" />
    </svg>
    <div class="text-2xl font-bold py-4"> {{ category.name }} </div>
    <p class="text-gray-500"> {{ category.title }} </p>
  </div>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  props: {
    category: { type: Object, required: true }
  },
  setup() {
    return {}
  }
})

</script>

<style></style>