<script setup>
import HeroBanner from './views/HeroBanner.vue'
import AboutSection from './views/AboutSection.vue'
import EventsHighlights from './views/EventsHighlights.vue'
import Registration from './views/Registration.vue'
import MeetTheTeam from './views/MeetTheTeam.vue'
import Contact from './views/Contact.vue'
import Footer from './components/Footer.vue'
import Sponsorships from './views/Sponsorships.vue'
</script>

<template>
  <HeroBanner />
  <AboutSection />
  <EventsHighlights />
  <Registration />
  <Sponsorships />
  <MeetTheTeam />
  <Contact />
  <Footer />
</template>

<style scoped>
body{
  overflow: hidden;
}

</style>
