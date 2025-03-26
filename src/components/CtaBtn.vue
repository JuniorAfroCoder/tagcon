<script setup>
defineProps(['btnMessage', 'url'])
</script>

<template>
  <a
    class="group block rounded-full bg-gradient-to-r from-[#a8000b] to-[#f91622] p-[2px] hover:text-white focus:ring-3 focus:outline-hidden"
    :href="url"
  >
    <span
      class="flex flex-row justify-between rounded-full text-white bg-black px-3 py-3 text-sm font-medium hover:text-white group-hover:bg-transparent"
    >
      {{ btnMessage }}
      <svg
        width="15px"
        height="15px"
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 128 128"
        style="enable-background: new 0 0 128 128"
        xml:space="preserve"
      >
        <path
          style="fill: #ffffff"
          d="M105.038 16.173H22.964L0 49.47l64 62.357 64-62.358-22.962-33.296zm-39.151 6.519 18.721 23.103h-39.75l19.253-23.103h1.776zm5.594 0h28.003L89.51 44.94 71.481 22.692zM86.1 52.314 64.053 98.875 43.159 52.314H86.1zm-46.316-7.216L28.711 22.692h29.744L39.784 45.098zm-4.503.698H10.454l14.464-20.971 10.363 20.971zm3.116 6.518L58.7 97.562 12.263 52.314h26.134zm52.135.791.052.064.383-.855h24.77L69.64 97.23l20.892-44.125zm3.357-7.31 9.32-20.79 14.338 20.79H93.889z"
        />
      </svg>
    </span>
  </a>
</template>

<style scoped>
a {
  background: linear-gradient(to right, #a8000b, #f91622);
}
a:hover {
  background: rgb(168, 0, 11);
  background: linear-gradient(90deg, rgba(168, 0, 11, 1) 0%, rgba(249, 22, 34, 1) 100%);
}

span {
  display: flex;
  gap: 4px;
  align-items: center;
}
</style>
