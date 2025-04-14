<script setup>
</script>

<template>
  <section id="team" class="bg-[#212121] dark:bg-gray-900">
    <div class="py-8 px-4 mx-auto max-w-screen-xl lg:py-16 lg:px-6">
      <div class="mx-auto max-w-screen-sm text-center mb-8 lg:mb-16">
        <h2
          class="font-[Recharge] uppercase mb-4 text-3xl tracking-tight font-extrabold sm:text-5xl text-white dark:text-white"
          data-aos="fade-up" data-aos-duration="1000" 
        >
          Meet the <span>Team</span> Behind TAG Convention
        </h2>
        <p
          class="font-[Avenir_Next_Roman] font-light text-gray-500 lg:mb-16 sm:text-xl dark:text-white"
          data-aos="fade-up" data-aos-duration="1000" data-aos-delay="300"
        >
          Meet the unique talents behind the preparation of this amazing event
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div class="col-span-4 ">
          <img class="h-auto max-w-full rounded-lg" v-lazy="'https://ik.imagekit.io/tagcon/images/team/Tag_Con_2025_1_.jpg?updatedAt=1744623957925'" alt="">
        </div>
        <div class="grid gap-4">
          <div>
            <img
              v-lazy=" 'https://ik.imagekit.io/tagcon/images/team/TAG%20CON-1-min.jpg?updatedAt=1744623934032' "
              class="h-auto max-w-full rounded-lg"
              
              alt="Image"
            />
          </div>
          <div>
            <img class="h-auto max-w-full rounded-lg" v-lazy=" 'https://ik.imagekit.io/tagcon/images/team/TAG%20CON-2-min.jpg?updatedAt=1744623940229' " alt="" />
          </div>
          <div>
            <img class="h-auto max-w-full rounded-lg" v-lazy=" 'https://ik.imagekit.io/tagcon/images/team/TAG%20CON-3-min.jpg?updatedAt=1744623945121' " alt="" />
          </div>
        </div>
        <div class="grid gap-4">
          <div>
            <img class="h-auto max-w-full rounded-lg" v-lazy="'https://ik.imagekit.io/tagcon/images/team/TAG%20CON-4-min.jpg?updatedAt=1744623946682'" alt="" />
          </div>
          <div>
            <img class="h-auto max-w-full rounded-lg" v-lazy="'https://ik.imagekit.io/tagcon/images/team/TAG%20CON%2012-min.jpg?updatedAt=1744623929925'" alt="" />
          </div>
          <div>
            <img
              class="h-auto max-w-full rounded-lg"
              v-lazy="'https://ik.imagekit.io/tagcon/images/team/TAG%20CON-10-min.jpg?updatedAt=1744623933968'"
              alt=""
            />
          </div>
        </div>
        <div class="grid gap-4">
          <div>
            <img
              class="h-auto max-w-full rounded-lg"
              v-lazy="'https://ik.imagekit.io/tagcon/images/team/TAG%20CON-17-min.jpg?updatedAt=1744623937060'"
              alt=""
            />
          </div>
          <div>
            <img
              class="h-auto max-w-full rounded-lg"
              v-lazy="'https://ik.imagekit.io/tagcon/images/team/TAG%20CON-18-min.jpg?updatedAt=1744623936249'"
              alt=""
            />
          </div>
          <div>
            <img
              class="h-auto max-w-full rounded-lg"
              v-lazy="'https://ik.imagekit.io/tagcon/images/team/TAG%20CON-20-min.jpg?updatedAt=1744623942169'"
              alt=""
            />
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
h2 span {
  color: #ff5722;
}
</style>
