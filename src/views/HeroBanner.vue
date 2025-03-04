<script setup>
import NavMenu from '../components/NavMenu.vue'
import CtaBtn from '@/components/CtaBtn.vue'
</script>

<template>
  <NavMenu />

  <div class="py-13 px-4 mx-auto max-w-screen-xl lg:py-16 lg:px-6">
    <div class="child-container">
      <div class="title-container">
        <span class="animate__slideInDown" id="title">TAG CON 2025</span>
        <img src="../../public/images/Hero-image.webp" alt="A guy wearing a VR Headset" srcset="" />
      </div>
      <div class="cta-container">
        <div class="top">
          <p>
            The Technology, Animation, and Gaming
            <span>Convention </span>!
          </p>
        </div>
        <div class="bottom">
          <div class="text">
            <p>June 6, 2025</p>
            <p>we are rocking Burundi with a unique of its kind event!"</p>
          </div>

          <div class="buttons">
            <CtaBtn btnMessage="Register Now" />
            <CtaBtn btnMessage="Sponsor Us" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.child-container {
  height: 100%;
  display: flex;
  flex-direction: column;
  margin-top: clamp(1rem, 2vh, 3rem);
  margin-inline: clamp(1rem, 3vw, 4rem);
  gap: 3rem;
}
.title-container,
.cta-container {
  display: flex;
  flex-direction: column;
  flex: 2;
  color: white;
}

.title-container {
  align-items: center;
}

.top {
  display: flex;
  font-family: 'Azo Sans', 'Muller', sans-serif;
  font-size: 2rem;
  text-transform: uppercase;
  line-height: normal;
  align-items: center;
}

.bottom {
  font-family: 'Monda', sans-serif;
  font-size: clamp(1rem, 1.5vw, 1.375rem);
}

.buttons {
  display: flex;
  justify-content: center;
  margin-top: 2rem;
  gap: 4rem;
}

#title {
  position: absolute;
  font-family: 'Muller', sans-serif;
  font-size: clamp(2.5rem, 6vw, 5rem);
  font-weight: bold;
  line-height: normal;
}
span {
  color: #ff5722;
}

@media screen and (min-width: 770px) {
  .hero-container {
    min-height: 100vh;
  }
  .child-container {
    flex-direction: row;
  }

  .top {
    margin-top: 2vh;
    flex: 3;
    font-size: 3.75rem;
  }
}
</style>
