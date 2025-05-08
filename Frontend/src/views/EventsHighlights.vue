<script setup>
import EventCard from '@/components/EventCard.vue'
</script>

<template>
  <div
    id="eventsHighlights"
    class="container bg-[#212121] py-8 px-4 mx-auto max-w-screen-xl lg:pb-16 lg:pt-40 lg:px-6"
  >
    <div class="grid grid-cols-1 gap-4 lg:grid-cols-4 lg:gap-8">
      <div class="grid grid-rows-2 order-first justify-items-end rounded-lg bg-dark lg:col-span-2">
        <div class="grid justify-items-end">
          <h2
            data-aos="fade-up"
            data-aos-duration="1000"
            data-aos-anchor-placement="top-center"
            class="font-[Recharge] uppercase leading-15 text-[2rem] lg:text-[3rem]"
          >
            What’s <span>Happening</span> at TAG Convention 2025?
          </h2>
          <img style="width: 10%" src="../components/icons/Icons.png" alt="" srcset="" />
        </div>
        <div class="image-container lg:w-1/2 h-full">
          <EventCard
            data-aos="fade-up"
            data-aos-duration="1000"
            data-aos-delay="1500"
            data-aos-disable="tablet"
            imageurl="/images/food-stands.webp"
            eventType="Food and drink stalls"
            description="Come taste the variety of food from different cultures and drinks of all kinds"
          />
        </div>
      </div>
      <div class="grid grid-rows-2 rounded-lg bg-dark">
        <EventCard
          data-aos="fade-up"
          data-aos-duration="1000"
          data-aos-delay="700"
          data-aos-disable="tablet"
          imageurl="/images/interactive-exhibitions.webp"
          eventType="Interactive Exhibitions"
          description="Explore cutting-edge technologies and innovative solutions by Burundian startups."
        />
        <EventCard
          data-aos="fade-up"
          data-aos-duration="1000"
          data-aos-delay="2000"
          data-aos-disable="tablet"
          imageurl="/images/anime-screenings.webp"
          eventType="Anime Screenings"
          description="Explore popular Japanese animations through dedicated movie-moments"
        />
      </div>

      <div class="grid grid-rows-2 rounded-lg bg-dark">
        <EventCard
          data-aos="fade-up"
          data-aos-duration="1000"
          data-aos-delay="1200"
          data-aos-disable="tablet"
          imageurl="/images/gaming-tournaments.webp"
          eventType="Gaming Tournaments"
          description="Participate in competitive gaming events for amateurs and pros alike"
        />
        <EventCard
          data-aos="fade-up"
          data-aos-duration="1000"
          data-aos-delay="2500"
          data-aos-disable="tablet"
          imageurl="/images/panel-discussions.webp"
          eventType="Panel Discussions"
          description="Hear from industry experts in technology, gaming, and animation worldwide"
        />
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  color: white;
}

.text {
  font-family: 'Recharge', 'Muller', sans-serif;
  text-transform: uppercase;
  font-size: 3rem;
  line-height: normal;
}

span {
  color: #ff5722;
}
</style>
