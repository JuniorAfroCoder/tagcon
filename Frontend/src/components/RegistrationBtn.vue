<script setup>
defineProps(['message'])
</script>

<template>
  <div class="flex w-[28rem] md:w-[30rem]">
    <a
      class="group relative inline-grid w-1/2 items-center overflow-hidden rounded-sm border border-current bg-gradient-to-r from-pink-500 via-red-500 to-yellow-500 p-[2px] hover:text-white focus:ring-3 focus:outline-hidden"
    >
      <span class="absolute -end-full transition-all group-hover:end-4">
        <svg
          class="size-5 rtl:rotate-180"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M17 8l4 4m0 0l-4 4m4-4H3"
          />
        </svg>
      </span>
      <span
        class="font-[Avenir_Next_Roman] w-full rounded-xs bg-white px-10 py-3 text-sm group-hover:bg-transparent"
      >
        {{ message }}
      </span>
    </a>
  </div>
</template>
