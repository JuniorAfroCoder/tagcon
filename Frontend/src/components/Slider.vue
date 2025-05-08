<script setup>
const imagesUrls = [
  'https://s3-us-west-2.amazonaws.com/s.cdpn.io/557257/1.png',
  'https://s3-us-west-2.amazonaws.com/s.cdpn.io/557257/2.png',
  'https://s3-us-west-2.amazonaws.com/s.cdpn.io/557257/3.png',
  'https://s3-us-west-2.amazonaws.com/s.cdpn.io/557257/4.png',
  'https://s3-us-west-2.amazonaws.com/s.cdpn.io/557257/5.png',
  'https://s3-us-west-2.amazonaws.com/s.cdpn.io/557257/6.png',
  'https://s3-us-west-2.amazonaws.com/s.cdpn.io/557257/7.png',
]
</script>
<template>
  <div class="slider">
    <div class="slide-track">
      <div v-for="img in imagesUrls" class="slide">
        <img :src="img" height="100" width="250" alt="" />
      </div>
      <div v-for="img in imagesUrls" class="slide">
        <img :src="img" height="100" width="250" alt="" />
      </div>
    </div>
  </div>
</template>

<style scoped>
@keyframes scroll {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(calc(-250px * 7));
  }
}

.slider {
  /* background: white; */
  box-shadow: 0 10px 20px -5px rgba(0, 0, 0, 0.125);
  height: 100px;
  margin: auto;
  overflow: visible;
  position: relative;
  width: 100%;
}

.slider::before,
.slider::after {
  /* background: linear-gradient(to right, rgba(255, 255, 255, 1) 0%, rgba(255, 255, 255, 0) 100%); */
  content: '';
  height: 100px;
  position: absolute;
  width: 200px;
  z-index: 2;
}

.slider::after {
  right: 0;
  top: 0;
  transform: rotateZ(180deg);
}

.slider::before {
  left: 0;
  top: 0;
}

.slide-track {
  animation: scroll 40s linear infinite;
  display: flex;
  width: calc(250px * 14);
}

.slide {
  height: 100px;
  width: 250px;
}
</style>
