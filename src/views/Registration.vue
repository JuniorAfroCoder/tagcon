<script setup>
import RegistrationBtn from '@/components/RegistrationBtn.vue'
import { ref } from 'vue'
const formVisible = ref(true)
</script>

<template>
  <!--
    Heads up! 
  
    This component comes with some `rtl` classes. Please remove them if they are not needed.
  -->

  <section
    id="registration"
    class="bg-[#212121] py-8 px-4 mx-auto max-w-screen-xl lg:py-16 lg:px-6 overflow-hidden sm:grid sm:grid-cols-2 sm:items-center"
  >
    <div class="p-8 md:p-12 lg:px-16 lg:py-24">
      <div class="flex flex-col justify-center align-center text-center lg:text-start">
        <h2
          class="font-[Recharge] uppercase text-3xl font-bold text-white md:text-5xl dark:text-white"
        >
          Ready to <span class="text-[#ff5722]">Join Us</span> ?
        </h2>

        <p
          class="font-[Avenir_Next_Roman] font-light mt-4 text-gray-500 lg:mb-8 sm:text-xl dark:text-white"
        >
          Be part of the action by registering for the TAG Convention. Will you be an attendee,
          exhibitor, or sponsor, we have a place for everyone!
        </p>

        <div class="grid grid-cols-1 gap-4 mt-8 content-center max-w-screen">
          <div id="accordion-collapse" data-accordion="collapse">
            <h2 id="accordion-collapse-heading-1">
              <button
                @click="formVisible = !formVisible"
                type="button"
                class="flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-b-0 border-gray-200 rounded-t-xl focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3"
                data-accordion-target="#accordion-collapse-body-1"
                aria-expanded="true"
                aria-controls="accordion-collapse-body-1"
              >
                <span class="text-white">Register as Exhibitor</span>
                <svg
                  data-accordion-icon
                  class="w-3 h-3 rotate-180 shrink-0"
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 10 6"
                >
                  <path
                    stroke="currentColor"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M9 5 5 1 1 5"
                  />
                </svg>
              </button>
            </h2>
            <div id="accordion-collapse-body-1" aria-labelledby="accordion-collapse-heading-1">
              <div
                :class="{ hidden: formVisible }"
                class="p-5 border border-b-0 border-gray-200 dark:border-gray-700 dark:bg-gray-900"
              >
                <form class="max-w-md mx-auto">
                  <div class="relative z-0 w-full mb-5 group">
                    <input
                      type="name"
                      name="floating_name"
                      id="floating_name"
                      class="block py-2.5 px-0 w-full text-sm text-white bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-orange-500 peer"
                      placeholder=" "
                      required
                    />
                    <label
                      for="floating_name"
                      class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto peer-focus:text-orange-500 peer-focus:dark:text-orange-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                      >Contact Name</label
                    >
                  </div>
                  <div class="relative z-0 w-full mb-5 group">
                    <input
                      type="email"
                      name="floating_email"
                      id="floating_email"
                      class="block py-2.5 px-0 w-full text-sm text-white bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-orange-500 focus:outline-none focus:ring-0 focus:border-orange-500 peer"
                      placeholder=" "
                      required
                    />
                    <label
                      for="floating_email"
                      class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-orange-500 peer-focus:dark:text-orange-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                      >Email Address</label
                    >
                  </div>

                  <div class="grid md:grid-cols-2 md:gap-6">
                    <div class="relative z-0 w-full mb-5 group">
                      <input
                        type="text"
                        name="floating_company"
                        id="floating_company"
                        class="block py-2.5 px-0 w-full text-sm text-white bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-orange-500 focus:outline-none focus:ring-0 focus:border-orange-500 peer"
                        placeholder=" "
                        required
                      />
                      <label
                        for="floating_company"
                        class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-orange-600 peer-focus:dark:text-orange-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                        >Company</label
                      >
                    </div>
                    <div class="relative z-0 w-full mb-5 group">
                      <input
                        type="tel"
                        name="floating_tel"
                        id="floating_tel"
                        class="block py-2.5 px-0 w-full text-sm text-white bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-orange-500 focus:outline-none focus:ring-0 focus:border-orange-500 peer"
                        placeholder=" "
                        required
                      />
                      <label
                        for="floating_tel"
                        class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-orange-500 peer-focus:dark:text-orange-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                        >Phone Number</label
                      >
                    </div>
                  </div>
                  <div class="relative z-0 w-full mb-5 group">
                    <input
                      type="text"
                      pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}"
                      name="floating_description"
                      id="floating_description"
                      class="block py-2.5 px-0 w-full text-sm text-white bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-orange-500 focus:outline-none focus:ring-0 focus:border-orange-500 peer"
                      placeholder=" "
                      required
                    />
                    <label
                      for="floating_description"
                      class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-orange-500 peer-focus:dark:text-orange-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                      >Company Description</label
                    >
                  </div>
                  <div class="relative z-0 w-full mb-5 group">
                    <input
                      type="text"
                      name="floating_space_needed"
                      id="floating_space_needed"
                      class="block py-2.5 px-0 w-full text-sm text-white bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-orange-500 focus:outline-none focus:ring-0 focus:border-orange-500 peer"
                      placeholder=" "
                      required
                    />
                    <label
                      for="floating_space_needed"
                      class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-orange-500 peer-focus:dark:text-orange-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                      >Space Needed</label
                    >
                  </div>

                  <button
                    type="submit"
                    class="text-white bg-orange-500 hover:bg-orange-600 focus:ring-4 focus:outline-none focus:ring-orange-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-orange-500 dark:hover:bg-orange-600 dark:focus:ring-orange-700"
                  >
                    Submit
                  </button>
                </form>
              </div>
            </div>
            <h2 id="accordion-collapse-heading-2">
              <button
                type="button"
                class="flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-b-0 border-gray-200 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3"
                data-accordion-target="#accordion-collapse-body-2"
                aria-expanded="false"
                aria-controls="accordion-collapse-body-2"
              >
                <span class="text-white">Register as Sponsor</span>
                <svg
                  data-accordion-icon
                  class="w-3 h-3 rotate-90 shrink-0"
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 10 6"
                >
                  <path
                    stroke="currentColor"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M9 5 5 1 1 5"
                  />
                </svg>
              </button>
            </h2>
            <h2 id="accordion-collapse-heading-3">
              <button
                type="button"
                class="flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-gray-200 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3"
                data-accordion-target="#accordion-collapse-body-3"
                aria-expanded="false"
                aria-controls="accordion-collapse-body-3"
              >
                <span class="text-white">Register as Exhibitor</span>
                <svg
                  data-accordion-icon
                  class="w-3 h-3 rotate-90 shrink-0"
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 10 6"
                >
                  <path
                    stroke="currentColor"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M9 5 5 1 1 5"
                  />
                </svg>
              </button>
            </h2>
          </div>
        </div>
      </div>
    </div>

    <img
      alt=""
      src="/public/images/1.jpg"
      class="h-full w-full object-cover sm:h-[calc(100%_-_2rem)] sm:self-end sm:rounded-ss-[30px] md:h-[calc(100%_-_4rem)] md:rounded-ss-[60px]"
    />
  </section>
</template>

<style scoped></style>
