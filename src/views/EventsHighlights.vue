<script setup>
import EventCard from '@/components/EventCard.vue'
</script>

<template>
  <div
    id="eventsHighlights"
    class="container bg-[#212121] py-8 px-4 mx-auto max-w-screen-xl lg:pb-16 lg:pt-40 lg:px-6"
  >
    <div class="grid grid-cols-1 gap-4 lg:grid-cols-4 lg:gap-8">
      <div class="grid grid-rows-2 rounded-lg bg-dark">
        <EventCard
          imageurl="/public/images/exhibition.webp"
          eventType="Interactive Exhibitions"
          description="Explore cutting-edge technologies and innovative solutions by Burundian startups."
        />
        <EventCard
          imageurl="/public/images/bigscreen-anime.webp"
          eventType="Anime Screenings"
          description="Explore popular Japanese animations through dedicated movie-moments"
        />
      </div>
      <div class="grid grid-rows-2 order-first justify-items-end rounded-lg bg-dark lg:col-span-2">
        <div class="grid justify-items-end">
          <h2 class="font-[Recharge] uppercase leading-15 text-[2rem] lg:text-[3rem]">
            What’s <span>Happening</span> at TAG Convention 2025?
          </h2>
          <img style="width: 10%" src="../components/icons/Icons.png" alt="" srcset="" />
        </div>
        <div class="image-container lg:w-1/2 h-full">
          <EventCard
            imageurl="/public/images/food-and-beverage.webp"
            eventType="Food and drink stalls"
            description="Come taste the variety of food from different cultures and drinks of all kinds"
          />
        </div>
      </div>
      <div class="grid grid-rows-2 rounded-lg bg-dark">
        <EventCard
          imageurl="/public/images/gaming-tournament.webp"
          eventType="Gaming Tournaments"
          description="Participate in competitive gaming events for amateurs and pros alike"
        />
        <EventCard
          imageurl="/public/images/panel-discussion.webp"
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
