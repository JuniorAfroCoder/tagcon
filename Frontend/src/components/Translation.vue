<template>
  <div class="translate-wrapper">
    <!-- Custom Trigger Button -->
    <button @click="toggleMenu" class="translate-button">
      🌍 {{ selectedLanguage }}
    </button>

    <!-- Custom Language Dropdown -->
    <div v-if="showMenu" class="language-menu">
      <button 
        v-for="lang in languages" 
        :key="lang.code"
        @click="changeLanguage(lang.code)"
        class="language-option"
      >
        {{ lang.name }}
      </button>
    </div>

    <!-- Hidden Google Translate Element -->
    <div id="google_translate_element" style="display: none ;"></div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showMenu: false,
      selectedLanguage: 'English',
      languages: [
        { code: 'fr', name: 'Français' }
      ],
    };
  },
  methods: {
    toggleMenu() {
      this.showMenu = !this.showMenu;
    },
    changeLanguage(langCode) {
    // Only handle 'fr' (French) since that's the only option
    const googleTranslateSelect = document.querySelector('.goog-te-combo');
    
    if (googleTranslateSelect && langCode === 'fr') {
      googleTranslateSelect.value = 'fr';  // Set language to French
      googleTranslateSelect.dispatchEvent(new Event('change'));
      
      // Update UI to reflect French selection
      this.selectedLanguage = 'Français';
      this.showMenu = false;
    }
  },
  },
//   mounted() {
//   if (!window.google || !window.google.translate) {
//     const script = document.createElement('script');
//     script.src = '//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit';
//     document.head.appendChild(script);

//     window.googleTranslateElementInit = () => {
//       new window.google.translate.TranslateElement({
//         pageLanguage: 'en',
//         autoDisplay: false,
//       }, 'google_translate_element');
//     };
//   }
// }

};
</script>

<style scoped>
.translate-wrapper {
  position: relative;
  display: inline-block;
}

.translate-button {
  padding: 8px 16px;
 background-image: linear-gradient(to right, #a8000b, #f91622);
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.language-menu {
  position: absolute;
  top: 100%;
  left: 0;
  background: #212121;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  z-index: 1000;
}

.language-option {
  display: block;
  width: 100%;
  padding: 8px 16px;
  text-align: left;
  background: none;
  border: none;
  cursor: pointer;
}

.language-option:hover {
color: white;
  background-image: linear-gradient(to right, #a8000b, #f91622);
}
</style>