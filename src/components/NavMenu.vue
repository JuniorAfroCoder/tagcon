<script setup>
import { ref } from 'vue'
import CtaBtn from './CtaBtn.vue'

// Reactive state for menu visibility
const isOpen = ref(false)

// Toggle menu function
const toggleMenu = () => {
  isOpen.value = !isOpen.value
}

// Close menu function
const closeMenu = () => {
  isOpen.value = false
}

// Click-outside directive
const vClickOutside = {
  mounted(el, binding) {
    el.clickOutsideEvent = function (event) {
      if (!(el === event.target || el.contains(event.target))) {
        binding.value(event)
      }
    }
    document.body.addEventListener('click', el.clickOutsideEvent)
  },
  unmounted(el) {
    document.body.removeEventListener('click', el.clickOutsideEvent)
  },
}
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
            <img
              src="../../public/images/logo.png"
              alt="Tag Con Logo"
              srcset=""
              width="100px"
              height="100px"
            />
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
                  Parternships
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
          <div class="sm:flex sm:gap-4">
            <CtaBtn url="#registration" btnMessage="Join Us" />
          </div>

          <div class="block md:hidden">
            <button
              @click="toggleMenu"
              class="rounded-sm p-2 text-white transition hover:text-gray-600/75 dark:bg-gray-800 dark:text-white dark:hover:text-white/75"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="size-5"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                stroke-width="2"
              >
                <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16" />
              </svg>
            </button>
          </div>
          <!-- Mobile dropdown menu -->
          <transition
            enter-active-class="transition ease-out duration-200"
            enter-from-class="opacity-0 -translate-y-2"
            enter-to-class="opacity-100 translate-y-0"
            leave-active-class="transition ease-in duration-150"
            leave-from-class="opacity-100 translate-y-0"
            leave-to-class="opacity-0 -translate-y-2"
          >
            <div
              v-show="isOpen"
              class="md:hidden absolute w-full bg-[#212121] dark:bg-gray-900"
              v-click-outside="closeMenu"
            >
              <nav aria-label="Mobile navigation">
                <ul class="px-4 py-2 space-y-4">
                  <li>
                    <a href="#about" class="block py-2 text-white hover:text-gray-400">About</a>
                  </li>
                  <li>
                    <a href="#about" class="block py-2 text-white hover:text-gray-400">Home</a>
                  </li>
                  <li>
                    <a href="#about" class="block py-2 text-white hover:text-gray-400">About</a>
                  </li>
                  <!-- Repeat for other menu items -->
                </ul>
              </nav>
            </div>
          </transition>
        </div>
      </div>
    </div>
  </header>
</template>

<style scoped>
header {
  font-family: 'Avenir Next Roman', sans-serif;
}

a {
  font-size: 1rem;
}

a:hover {
  color: #ff5722;
}
</style>
