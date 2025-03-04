<script setup>
defineProps(['eventType', 'description', 'url'])
</script>

<template>
  <div class="card">
    <a href="#" class="group relative block bg-black">
      <img
        alt=""
        :src="url"
        class="absolute inset-0 w-full h-full object-cover opacity-75 transition-opacity group-hover:opacity-50"
      />

      <div class="relative p-4 sm:p-6 lg:p-8">
        <p class="font-[Avenir_Next] text-xl font-bold text-white sm:text-2xl">{{ eventType }}</p>

        <div class="mt-32 sm:mt-48 lg:mt-64">
          <div
            class="translate-y-8 transform opacity-0 transition-all group-hover:translate-y-0 group-hover:opacity-100"
          >
            <p class="font-[Monda] text-xl text-white">
              {{ description }}
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
