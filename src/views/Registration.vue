<script setup>
import RegistrationBtn from '@/components/RegistrationBtn.vue'
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
      <div class="mx-auto max-w-xl text-center ltr:sm:text-left rtl:sm:text-right">
        <h2
          class="font-[Recharge] uppercase text-3xl font-bold text-white md:text-5xl dark:text-white"
        >
          Ready to <span>Join Us</span> ?
        </h2>

        <p
          class="font-[Avenir_Next_Roman] font-light text-gray-500 lg:mb-8 sm:text-xl dark:text-white"
        >
          Be part of the action by registering for the TAG Convention. Will you be an attendee,
          exhibitor, or sponsor, we have a place for everyone!
        </p>

        <div class="grid gap-4 mt-8">
          <RegistrationBtn message="Register as Attendee" />
          <RegistrationBtn message="Register as Exhibitor" />
          <RegistrationBtn message="Register as Sponsor" />
        </div>
      </div>
    </div>

    <img
      alt=""
      src="https://images.unsplash.com/photo-1484959014842-cd1d967a39cf?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770&q=80"
      class="h-full w-full object-cover sm:h-[calc(100%_-_2rem)] sm:self-end sm:rounded-ss-[30px] md:h-[calc(100%_-_4rem)] md:rounded-ss-[60px]"
    />
  </section>
</template>

<style scoped>
h2 span {
  color: #ff5722;
}
</style>
