<script setup>
import Slider from '@/components/Slider.vue'
</script>

<template>
  <section id="sponsorships" class="overflow-visible bg-[#212121] text-white pb-4">
    <div class="py-8 px-4 mx-auto max-w-screen-xl lg:py-16 lg:px-6 lg:flex-rows-1 lg:items-center">
      <div class="mx-auto max-w-3xl text-center">
        <h1 data-aos="fade-up"
     data-aos-duration="1000" class="font-[Recharge] uppercase bg-clip-text text-3xl font-extrabold sm:text-5xl">
          Be a Part of TAG Convention’s Success
        </h1>

        <p data-aos="fade-up"
     data-aos-easing="linear"
     data-aos-duration="1000" data-aos-delay="500" class="font-[Avenir_Next_Roman] mx-auto mt-4 max-w-xl sm:text-xl/relaxed">
          We’re looking for partners and sponsors to help bring this event to life. Sponsoring us at
          the TAG CON 2025 comes with a lot of perks:
          <span class="underline underline-offset-3 decoration-2 decoration-[#d34202]">
            you will enjoy unparalleled visibility across our different communication tools:
            website, social media, flyers, banner, and rollup and will have a unique opportunity to
            engage with a diverse audience.
          </span>
        </p>

        <div class="mt-8 flex flex-wrap justify-center gap-4">
          <a
            class="group inline-block rounded-sm bg-gradient-to-r from-[#a8000b] to-[#f91622] p-[2px] hover:text-white focus:ring-3 focus:outline-hidden"
            href="/Catégorie de Sponsor.pdf" data-aos="zoom-in" data-aos-delay="800" data-aos-duration="500" data-aos-easing="ease-in-back" download
          > 
            <span
              class="font-[Avenir_Next_Roman] block rounded-xs px-8 py-3 text-sm font-medium group-hover:bg-transparent"
            >
              Download Sponsorship Package
            </span>
          </a>

          <a
            class="group inline-block rounded-sm bg-gradient-to-r from-[#a8000b] to-[#f91622] p-[2px] hover:text-white focus:ring-3 focus:outline-hidden"
            href="mailto:tagconvention@gmail.com" data-aos="zoom-in" data-aos-delay="1400" data-aos-duration="500" data-aos-easing="ease-in-back"
          >
            <span
              class="font-[Avenir_Next_Roman] block rounded-xs bg-[#28282B] px-8 py-3 text-sm font-medium group-hover:bg-transparent"
            >
              Contact Us For Opportunities
            </span>
          </a>
        </div>
      </div>
      <div class="mt-20">
        <h3 class="font-[African_Culture] uppercase text-center text-3xl mb-5">
          already sponsoring us
        </h3>
        <Slider />
        <h3 class="font-[African_Culture] uppercase text-center text-3xl mt-8 mb-5 lg:mt-20">
          already our partners
        </h3>
        <Slider />
      </div>
    </div>
  </section>
</template>

<style scoped>
a {
  background: linear-gradient(to right, #a8000b, #f91622);
}
h1 {
  color: #ff5722;
}


</style>
