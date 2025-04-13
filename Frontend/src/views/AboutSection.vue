<template>
  <div id="about" class="container py-8 px-4 mx-auto max-w-screen-xl lg:py-16 lg:px-6">
    <div class="image-container" data-aos="zoom-out-up" data-aos-duration="1200">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="#ffffff"
        width="50px"
        height="50px"
        viewBox="0 0 1024 1024"
      >
        <path
          d="M743.216 75.552c-25.6-12.016-49.806-23.328-71.838-34.384C614.914 12.88 563.714-.864 514.914-.864c-98.288 0-166.304 56.704-208.96 99.36L99.106 305.568c-110.688 110.8-128.368 223.6-57.265 365.808 11.025 22.08 22.369 46.336 34.369 72.033 64.704 138.384 131.584 281.487 241.056 281.487 3.072 0 6.112-.096 9.216-.336 112.976-8.848 145.023-154.288 173.312-282.592 4.496-20.32 8.751-39.809 13.12-57.28 7.6-30.209 22.56-48.976 63.551-90.064l5.632-5.664 3.472-3.472 9.12-9.088c41.088-41.088 59.856-56.032 90.096-63.664 17.311-4.351 36.752-8.64 57.024-13.088 128.224-28.303 273.6-60.368 282.4-173.52 8.879-114.833-138.465-183.84-280.993-250.576zm215.25 244.783c-6.224 79.776-184.813 103.324-291.102 129.98-47.008 11.872-75.616 36.752-118.784 79.936-3.008 3.007-6.032 6.015-9.088 9.07-3.024 3.025-6.032 6.097-9.057 9.09-43.168 43.215-68 71.807-79.824 118.88-26.672 106.384-50.191 285.168-129.87 291.44a55.54 55.54 0 0 1-4.322.144c-84.544 0-155.68-192.24-218.447-317.664-63.744-127.504-36.433-210.224 45.36-292.096 15.696-15.727 35.215-35.247 59.135-59.182 24.432-24.464 53.487-53.552 87.919-88 23.904-23.936 43.408-43.424 59.12-59.184 50.8-50.848 101.936-80.64 163.92-80.64 37.808 0 79.632 11.056 127.872 35.248 127.456 63.905 323.888 136.48 317.168 222.978zm-479.678 30.94h64v-64h-64v64zm0-96h64v-64h-64v64zm96 0h64v-64h-64v64zm0 96h64v-64h-64v64zM329.893 543.436l24.336-24.336c12-12 12-31.472 0-43.456-12-12-31.44-12-43.44 0l-24.352 24.352-24.352-24.352c-12-12-31.44-12-43.44 0s-12 31.456 0 43.456l24.351 24.352-24.351 24.351c-12 11.985-12 31.44 0 43.44s31.456 12 43.44 0l24.352-24.335 25.056 25.055c12 12 31.44 12 43.44 0s12-31.471 0-43.471z"
        />
      </svg>
      <img id="image" src="/images/About-section.webp" alt="" srcset="" />
    </div>
    <div class="text-container">
      <div class="title-container">
        <p id="title" data-aos="fade-right"
        data-aos-duration="800"
     data-aos-offset="200"
     data-aos-easing="ease-in-sine" >What is TAG Convention ?</p>
      </div>
      <div class="svg-container">
        <p id="info-text" data-aos="fade-right"
     data-aos-offset="200"
     data-aos-duration="1000"
     data-aos-delay="300"
     data-aos-easing="ease-in-sine">
          The TAG Convention (Tech-Animation-Gaming Convention) is
          <span>Burundi's premier event </span>bringing together enthusiasts, creators, and industry
          leaders in technology, gaming, and animation. It's a platform for <span>innovation</span>,
          cultural exchange, and <span>community building</span>.
        </p>
        <svg xmlns="http://www.w3.org/2000/svg" width="50px" height="50px" viewBox="0 0 24 24">
          <path
            fill="none"
            stroke="#ffffff"
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M16.5,19 C17.8807119,19 19,17.8807119 19,16.5 C19,15.1192881 17.8807119,14 16.5,14 C15.1192881,14 14,15.1192881 14,16.5 C14,17.8807119 15.1192881,19 16.5,19 Z M10,5 L12,3 M7.5,10 C8.88071187,10 10,8.88071187 10,7.5 C10,6.11928813 8.88071187,5 7.5,5 C6.11928813,5 5,6.11928813 5,7.5 C5,8.88071187 6.11928813,10 7.5,10 Z M8,16 L16,8 M5.5,21 C6.88071187,21 8,19.8807119 8,18.5 C8,17.1192881 6.88071187,16 5.5,16 C4.11928813,16 3,17.1192881 3,18.5 C3,19.8807119 4.11928813,21 5.5,21 Z M18.5,8 C19.8807119,8 21,6.88071187 21,5.5 C21,4.11928813 19.8807119,3 18.5,3 C17.1192881,3 16,4.11928813 16,5.5 C16,6.88071187 17.1192881,8 18.5,8 Z M12,21 L14,19"
          />
        </svg>
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  gap: 4rem;
  background-color: #212121;
  color: white;
  position: relative;
  z-index: -20;
  overflow: hidden;
}

#image {
  max-width: 100%;
  height: auto;
}
.text-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: end;
  gap: 2rem;
}
#title {
  font-family: 'Recharge', 'Muller', sans-serif;
  font-size: 2rem;
  text-transform: uppercase;
  line-height: normal;
}

#info-text {
  font-family: 'Avenir Next Roman', sans-serif;
  font-size: clamp(1rem, 1.5vw, 1.375rem);
  text-align: start;
}
svg {
  position: relative;
  top: 2rem;
  left: 80%;
}

span {
  color: #ff5722;
}

@media screen and (min-width: 770px) {
  .container {
    flex-direction: row-reverse;
    gap: 0;
  }
  .title-container {
    display: flex;
    justify-content: center;
  }

  #title {
    font-size: 3rem;
  }
  #image {
    position: static;
  }
}
</style>
