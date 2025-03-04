<script setup>
import EventCard from '@/components/EventCard.vue'
const urls = [
  '../../public/images/exhibition.webp',
  '../../public/images/bigscreen-anime.webp',
  '../../public/images/food-and-beverage.webp',
  '../../public/images/gaming-tournament.webp',
  '../../public/images/panel-discussion.webp',
]
</script>

<template>
  <div class="container py-8 px-4 mx-auto max-w-screen-xl lg:pb-16 lg:pt-40 lg:px-6">
    <div class="grid grid-cols-1 gap-4 lg:grid-cols-4 lg:gap-8">
      <div class="grid grid-rows-2 rounded-lg bg-dark">
        <EventCard
          :url="urls[0]"
          eventType="Interactive Exhibitions"
          description="Explore cutting-edge technologies and innovative solutions by Burundian startups."
        />
        <EventCard
          :url="urls[1]"
          eventType="Anime Screenings"
          description="Explore popular Japanese animations through dedicated movie-moments"
        />
      </div>
      <div class="grid grid-rows-2 order-first justify-items-end rounded-lg bg-dark lg:col-span-2">
        <div class="text grid justify-items-end">
          <h2>What’s <span>Happening</span> at TAG Convention 2025?</h2>
          <img style="width: 10%" src="../components/icons/Icons.png" alt="" srcset="" />
        </div>
        <div class="image-container lg:w-1/2 h-full">
          <EventCard
            :url="urls[2]"
            eventType="Food and drink stalls"
            description="Come taste the variety of food from different cultures and drinks of all kinds"
          />
        </div>
      </div>
      <div class="grid grid-rows-2 rounded-lg bg-dark">
        <EventCard
          :url="urls[3]"
          eventType="Gaming Tournaments"
          description="Participate in competitive gaming events for amateurs and pros alike"
        />
        <EventCard
          :url="urls[4]"
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
  font-family: 'Azo Sans', 'Muller', sans-serif;
  text-transform: uppercase;
  font-size: 3rem;
  line-height: normal;
}

span {
  color: #ff5722;
}
</style>
