import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../src/App.vue';
import AOS from "aos";
import 'aos/dist/aos.css';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    }
  ]
});

router.beforeEach((to, from, next) => {
  AOS.init(
    {
      once: true,
      offset: 120,
      anchorPlacement: 'top-bottom',
      disableMutationObserver: false, // disables automatic mutations' detections 
  debounceDelay: 50, // the delay on debounce used while resizing window 
  throttleDelay: 99, // the delay on throttle used while scrolling the page 

    }); // Initialize AOS
  next();
});

export default router;