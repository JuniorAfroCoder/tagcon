<script setup>
import { ref } from 'vue'
import CtaBtn from './CtaBtn.vue'
import Translation from './Translation.vue'

const isHidden = ref(true)
const hidden = !isHidden
const isOpen = ref(hidden)
</script>

<template>
  <header
    class="fixed w-full h-auto z-20 bg-[#212121] border-solid border-b border-gray-500 text-white dark:bg-gray-900"
  >
    <div class="mx-auto px-4 sm:px-6 lg:px-10">
      <div class="flex h-16 items-center justify-between">
        <div class="md:flex md:items-center md:gap-16">
          <a class="block text-orange dark:text-orange" href="#">
            <span class="sr-only">Home</span>
            <img src="/images/logo.png" alt="Tag Con Logo" srcset="" width="100px" height="100px" />
          </a>
        </div>

        <div class="hidden md:block max-w-dvh">
          <nav aria-label="Global">
            <ul class="flex items-center gap-10 text-sm">
              <li>
                <a
                  class="text-white transition dark:text-white dark:hover:text-white/75"
                  href="#about"
                >
                  About
                </a>
              </li>

              <li>
                <a
                  class="text-white transition hover:text-gray-500/75 dark:text-white dark:hover:text-white/75"
                  href="#eventsHighlights"
                >
                  Events
                </a>
              </li>

              <li>
                <a
                  class="text-white transition hover:text-gray-500/75 dark:text-white dark:hover:text-white/75"
                  href="#registration"
                >
                  Registration
                </a>
              </li>

              <li>
                <a
                  class="text-white transition hover:text-gray-500/75 dark:text-white dark:hover:text-white/75"
                  href="#sponsorships"
                >
                  Partnerships
                </a>
              </li>

              <li>
                <a
                  class="text-white transition hover:text-gray-500/75 dark:text-white dark:hover:text-white/75"
                  href="#team"
                >
                  Team
                </a>
              </li>

              <li>
                <a
                  class="text-white transition hover:text-gray-500/75 dark:text-white dark:hover:text-white/75"
                  href="#contact"
                >
                  Contact
                </a>
              </li>
            </ul>
          </nav>
        </div>

        <div class="flex items-center gap-4">
          <div class="sm:flex">
            <CtaBtn url="#registration" btnMessage="Join Us" />
          </div>
          <Translation />

          <div class="block md:hidden">
            <button
              @click="isHidden = !isHidden"
              class="rounded-sm p-2 text-white transition hover:text-gray-600/75 dark:bg-gray-800 dark:text-white dark:hover:text-white/75"
            >
              <svg
                :class="{ hidden: !isHidden }"
                xmlns="http://www.w3.org/2000/svg"
                class="size-5"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                stroke-width="2"
              >
                <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16" />
              </svg>

              <svg
                :class="{ hidden: isHidden }"
                class="size-5"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                aria-hidden="true"
                data-slot="icon"
              >
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18 18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Mobile menu -->
    <div :class="{ hidden: isHidden }" id="mobile-menu">
      <div class="space-y-1 px-2 pt-2 pb-3">
        <!-- Current: "bg-gray-900 text-white", Default: "text-gray-300 hover:bg-gray-700 hover:text-white" -->
        <a
          @click="isHidden = !isHidden"
          href="#"
          class="block font-[Avenir_Next_Roman] rounded-md bg-[#383838] px-3 py-2 text-base font-medium text-white"
          aria-current="page"
          >Home</a
        >
        <a
          @click="isHidden = !isHidden"
          href="#about"
          class="block font-[Avenir_Next_Roman] rounded-md px-3 py-2 text-base font-medium text-gray-300 hover:bg-gray-700 hover:text-white"
          >About</a
        >
        <a
          @click="isHidden = !isHidden"
          href="#eventsHighlights"
          class="block font-[Avenir_Next_Roman] rounded-md px-3 py-2 text-base font-medium text-gray-300 hover:bg-gray-700 hover:text-white"
          >Events</a
        >
        <a
          @click="isHidden = !isHidden"
          href="#registration"
          class="block font-[Avenir_Next_Roman] rounded-md px-3 py-2 text-base font-medium text-gray-300 hover:bg-gray-700 hover:text-white"
          >Registration</a
        >
        <a
          @click="isHidden = !isHidden"
          href="#sponsorships"
          class="block font-[Avenir_Next_Roman] rounded-md px-3 py-2 text-base font-medium text-gray-300 hover:bg-gray-700 hover:text-white"
          >Partnerships</a
        >
        <a
          @click="isHidden = !isHidden"
          href="#team"
          class="block font-[Avenir_Next_Roman] rounded-md px-3 py-2 text-base font-medium text-gray-300 hover:bg-gray-700 hover:text-white"
          >Team</a
        >
        <a
          @click="isHidden = !isHidden"
          href="#contact"
          class="block font-[Avenir_Next_Roman] rounded-md px-3 py-2 text-base font-medium text-gray-300 hover:bg-gray-700 hover:text-white"
          >Contact</a
        >
      </div>
    </div>
  </header>
</template>

<style scoped>
header {
  font-family: 'Avenir Next Roman', sans-serif;
  background-color: #212121;
}

a {
  font-size: 1rem;
}

a:hover {
  color: #a8000b;
}
</style>
