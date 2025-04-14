import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from '../router'
import AOS from 'aos'
import 'aos/dist/aos.css'
import VueLazyLoad from 'vue3-lazyload';

const app = createApp(App)
app.use(router)
app.use(AOS)

app.use(VueLazyLoad, {
  loading: '/images/loading-placeholder.jpg', // optional
  error: '/images/error.jpg', // optional
  // You can also add more config here
});

app.mount('#app')
