<script setup>
import { Countdown } from 'vue3-flip-countdown'
import NavMenu from '../components/NavMenu.vue'
import CtaBtn from '@/components/CtaBtn.vue'
</script>

<template>
  <NavMenu data-aos="zoom-in" data-aos-duration="2000" data-aos-easing="ease-in-out" />

  <div id="heroBanner" class="py-13 px-4 mx-auto max-w-screen-xl lg:py-16 lg:px-6">
    <div class="child-container">
      <div class="title-container">
        <span class="title" data-aos="fade-down" data-aos-duration="1500">TAG CON 2025</span>
        <img src="../../public/images/Hero-image.webp" data-aos="zoom-in" data-aos-duration="1000" alt="A guy wearing a VR Headset" srcset="" />
      </div>
      <div class="cta-container text-white">
        <div class="top" data-aos="fade-down" data-aos-delay="100" data-aos-duration="1000">
          <p>
            The Technology, Animation, and Gaming
            <span class="text-[#ff5722]">Convention </span>!
          </p>
        </div>
        <div class="bottom" >
          <div class="font-[Avenir_Next_Roman]" data-aos="fade-down" data-aos-duration="1000" data-aos-delay="1500">
            <p class="text-center">In</p>
            <div class="py-4">
              <Countdown labelColor="white" deadline="2025-08-01 00:00:00" />
            </div>
            <p>we are rocking Burundi with a unique of its kind event!</p>
          </div>

          <div class="buttons">
            <CtaBtn data-aos="fade-down" data-aos-delay="2200" data-aos-easing="ease-in" btnMessage="Register Now" url="#registration" />
            <CtaBtn data-aos="fade-down" data-aos-delay="2600" data-aos-easing="ease-in" btnMessage="Sponsor Us" url="#registration" />
            <CtaBtn data-aos="fade-down" data-aos-delay="3000" data-aos-easing="ease-in" btnMessage="Volunteer" url="#registration" />
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="down-arrow show hidden lg:block"></div>
</template>

<style scoped>

.heroBanner{
  background-image: url(/Frontend/public/images/background.jpg);
}

.down-arrow {
  opacity: 0;
  color: white;
  position: absolute;
  top: calc(100vh - 80px);
  left: calc(50% - 14px);
  width: 0;
  height: 30px;
  border: 2px solid;
  border-radius: 2px;
  animation: jumpInfinite 1.5s infinite;
}
.down-arrow .show{
    opacity: 1;
    transition: opacity 3s ease-in-out;
    -webkit-transition: opacity 3s ease-in-out;
    -moz-transition: opacity 3s ease-in-out;
    -ms-transition: opacity 3s ease-in-out;
    -o-transition: opacity 3s ease-in-out;
}

.down-arrow:after {
  content: ' ';
  position: absolute;
  color: white;
  top: 12px;
  left: -8px;
  width: 16px;
  height: 16px;
  border-bottom: 4px solid;
  border-right: 4px solid;
  border-radius: 4px;
  transform: rotateZ(45deg);
}

@keyframes jumpInfinite {
  0% {
    margin-top: 0;
  }
  50% {
    margin-top: 20px;
  }
  100% {
    margin-top: 0;
  }
}

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
}

.title-container {
  display: flex;
  flex-direction: column;
  align-content: center;
  justify-content: space-between;
}

.top p {
  font-size: clamp(2rem, 2.5vw, 3.5rem);
  font-family: 'Recharge', sans-serif;
  text-transform: uppercase;
  line-height: normal;
  text-align: center;
}

.bottom {
  padding-top: 1rem;
  font-family: 'Recharge', sans-serif;
  font-size: clamp(1rem, 1.5vw, 1.375rem);
  text-align: center;
}

.buttons {
  font-family: 'Avenir Next Roman', sans-serif;
  display: grid;
  justify-content: center;
  margin-top: 2rem;
  gap: 1rem;
}

.title {
  /* position: absolute; */
  padding-top: 1rem;
  font-family: 'Recharge', sans-serif;
  font-size: clamp(1rem, 50vw, 3rem);
  font-weight: bold;
  line-height: normal;
  text-align: center;
  background: linear-gradient(to top, #f91622, #a8000b);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

@media screen and (min-width: 770px) {
  .hero-container {
    min-height: 100vh;
  }
  .child-container {
    flex-direction: row;
  }
  .cta-container {
    margin-top: 2.2rem;
  }
  .top {
    margin-top: 3rem;
    flex: 3;
    font-size: 3.75rem;
  }
  .bottom {
    padding-top: 1rem;
  }
  .buttons {
    display: flex;
    flex-direction: row;
    gap: 4rem;
  }
}
</style>
