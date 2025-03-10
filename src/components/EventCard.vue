<script setup>
import { ref } from 'vue'
const props = defineProps({
  eventType: String,
  description: String,
  url: String, // Explicitly declared prop for the image URL
})
const isTextVisible = ref(false)
</script>

<template>
  <div class="card">
    <a @click="isTextVisible = !isTextVisible" class="group relative block bg-black">
      <img
        alt=""
        :src="props.url"
        :class="{ 'opacity-50': isTextVisible }"
        class="absolute inset-0 w-full h-full object-cover opacity-75 transition-opacity group-hover:opacity-50"
      />

      <div class="relative p-4 sm:p-6 lg:p-8">
        <p class="font-[African_Culture] uppercase text-xl font-bold text-white sm:text-2xl">
          {{ props.eventType }}
        </p>

        <div class="mt-22 sm:mt-32 lg:mt-36">
          <div
            :class="{
              'translate-y-0': isTextVisible,
              'opacity-100': isTextVisible,
              'translate-y-8': !isTextVisible,
              'opacity-0': !isTextVisible,
            }"
            class="transform transition-all group-hover:translate-y-0 group-hover:opacity-100"
          >
            <p class="font-[Avenir_Next_Roman] text-xl text-white">
              {{ props.description }}
            </p>
          </div>
        </div>
      </div>
    </a>
  </div>
</template>

<style scope>
.card {
  padding: 2rem 0;
  border-top: 1px solid white;
}
</style>
