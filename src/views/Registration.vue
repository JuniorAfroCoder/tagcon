<script setup>
import RegistrationBtn from '@/components/RegistrationBtn.vue'
import { ref } from 'vue'
const formHidden = ref(true)
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
          Ready to <span>Join Us</span> ?
        </h2>

        <p
          class="font-[Avenir_Next_Roman] font-light mt-4 text-gray-500 lg:mb-8 sm:text-xl dark:text-white"
        >
          Be part of the action by registering for the TAG Convention. Will you be an attendee,
          exhibitor, or sponsor, we have a place for everyone!
        </p>

        <div class="grid grid-cols-1 gap-4 mt-8 content-center max-w-screen">
          <RegistrationBtn message="Register as Attendee" />
          <RegistrationBtn message="Register as Exhibitor" @click="formHidden = !formHidden" />

          <form :class="{ hidden: formHidden }" class="font-[Avenir_Next_Roman]">
            <div class="relative z-0 mb-5 group">
              <input
                type="text"
                name="floating_contact_name"
                id="floating_contact_name"
                class="block py-2.5 px-0 w-full text-sm text-white bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 focus:outline-none focus:ring-0 focus:border-[#d34202] peer"
                placeholder=" "
                required
              />
              <label
                for="floating_contact_name"
                class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-2 left-2 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-[#d34202] peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                >Contact name</label
              >
            </div>
            <div class="relative z-0 w-full mb-5 group">
              <input
                type="email"
                name="floating_email"
                id="floating_email"
                class="block py-2.5 px-0 w-full text-sm text-white bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 focus:outline-none focus:ring-0 focus:border-[#d34202] peer"
                placeholder=" "
                required
              />
              <label
                for="floating_email"
                class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 left-2 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto peer-focus:text-[#d34202] peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                >Email address</label
              >
            </div>

            <div class="relative z-0 w-full mb-5 group">
              <input
                type="text"
                name="floating_company"
                id="floating_company"
                class="block py-2.5 px-0 w-full text-sm text-white bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 focus:outline-none focus:ring-0 focus:border-[#d34202] peer"
                placeholder=" "
                required
              />
              <label
                for="floating_company"
                class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 left-2 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-[#d34202] peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                >Company (Ex. Nuyu Agency)</label
              >
            </div>
            <div class="relative z-0 w-full mb-5 group">
              <input
                type="tel"
                name="floating_phone"
                id="floating_phone"
                class="block py-2.5 px-0 w-full text-sm text-white bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:border-gray-600 focus:outline-none focus:ring-0 focus:border-[#d34202] peer"
                placeholder=" "
                required
              />
              <label
                for="floating_phone"
                class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 left-2 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-[#d34202] peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                >Phone number (+257 66 666 666)</label
              >
            </div>
            <div class="relative z-0 w-full mb-5 group">
              <textarea
                type="text"
                name="floating_company_info"
                id="floating_company_info"
                rows="4"
                class="block py-2.5 px-0 w-full text-sm text-white bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 focus:outline-none focus:ring-0 focus:border-[#d34202] peer"
                placeholder=" "
                required
              ></textarea>
              <label
                for="floating_company_info"
                class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 left-2 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-[#d34202] peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                >What is your company about ?</label
              >
            </div>
            <div class="relative z-0 w-full mb-5 group">
              <textarea
                type="text"
                name="floating_space_need"
                id="floating_space_need"
                rows="4"
                class="block py-2.5 px-0 w-full text-sm text-white bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:border-gray-600 focus:outline-none focus:ring-0 focus:border-[#d34202] peer"
                placeholder=" "
                required
              ></textarea>
              <label
                for="floating_space_need"
                class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 left-2 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-[#d34202] peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                >How much space will your business need?</label
              >
            </div>
            <button
              type="submit"
              class="text-white bg-[#ff5722] hover:bg-[#ff3c22e0] focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center"
            >
              Submit
            </button>
          </form>

          <RegistrationBtn message="Register as Sponsor" />
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

<style scoped>
h2 span {
  color: #ff5722;
}
</style>
