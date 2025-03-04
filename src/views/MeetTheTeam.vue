<script setup>
import TeamMemberCard from '@/components/TeamMemberCard.vue'

const imageUrls = [
  '../../public/images/exhibition.jpg',
  'https://flowbite.s3.amazonaws.com/blocks/marketing-ui/avatars/jese-leos.png',
  'https://flowbite.s3.amazonaws.com/blocks/marketing-ui/avatars/michael-gouch.png',
  'https://flowbite.s3.amazonaws.com/blocks/marketing-ui/avatars/sofia-mcguire.png',
]
</script>

<template>
  <section class="bg-black dark:bg-gray-900">
    <div class="py-8 px-4 mx-auto max-w-screen-xl lg:py-16 lg:px-6">
      <div class="mx-auto max-w-screen-sm text-center mb-8 lg:mb-16">
        <h2
          class="font-[Muller] uppercase mb-4 text-3xl tracking-tight font-extrabold sm:text-5xl text-white dark:text-white"
        >
          Meet the <span>Team</span> Behind TAG Convention
        </h2>
        <p class="font-[Monda] font-light text-gray-500 lg:mb-16 sm:text-xl dark:text-gray-400">
          Meet the unique talents behind the preparation of this amazing event
        </p>
      </div>
      <div class="grid gap-8 mb-6 lg:mb-16 md:grid-cols-2">
        <TeamMemberCard
          imageUrl="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/avatars/bonnie-green.png"
          name="Bonnie Green"
          role="CEO & Web Developer"
          bio="Bonnie drives the technical strategy of the flowbite platform and brand"
        />
        <TeamMemberCard
          imageUrl="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/avatars/jese-leos.png"
          name="Jese Leos"
          role="CTO"
          bio="Jese drives the technical strategy of the flowbite platform and brand."
        />
        <TeamMemberCard
          imageUrl="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/avatars/michael-gouch.png"
          name="Michael Gough"
          role="Senior Front-end Developer"
          bio="Bonnie drives the technical strategy of the flowbite platform and brand"
        />
        <TeamMemberCard
          imageUrl="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/avatars/sofia-mcguire.png"
          name="Lana Byrd"
          role="Marketing & Sale"
          bio="Bonnie drives the technical strategy of the flowbite platform and brand"
        />
      </div>
    </div>
  </section>
</template>

<style scoped>
h2 span {
  color: #ff5722;
}
</style>
