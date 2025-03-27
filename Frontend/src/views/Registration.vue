<script setup>
import RegistrationBtn from '@/components/RegistrationBtn.vue'
import { ref } from 'vue'
const firstFormVisible = ref(false);
const secondFormVisible = ref(false);

const toggleForm = (form) => {
  if (form === "first") {
    firstFormVisible.value = !firstFormVisible.value;
    secondFormVisible.value = false; // Hide second form when first is shown
  } else if (form === "second") {
    secondFormVisible.value = !secondFormVisible.value;
    firstFormVisible.value = false; // Hide first form when second is shown
  }
};



//first form data handling

const formData = ref({
  name: '',
  email: '',
  companyName: '',
  phoneNumber:'',
  companyDescription: '',
  spaceNeeded:'',
});

const successMessage = ref('');
const errorMessage = ref('');

const submitForm = async () => {
  try {
    const response = await fetch('http://localhost:3000/api/submit-exhibitor-form', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData.value)
    });

    if (!response.ok) {
      throw new Error('Network response was not ok');
    }

    const data = await response.json();
    successMessage.value = 'Form submitted successfully!';
    errorMessage.value = '';
    formData.value = { name: '', email: '', companyName: '', phoneNumber:'', companyDescription:'',spaceNeeded:'' }; // Reset form
    
  } catch (error) {
    errorMessage.value = 'There was a problem submitting the form.';
    console.error('Error:', error);
  }
};

//second form handling
const volunteerForm = ref({
  name: '',
  email: '',
  phoneNumber:'',
  age: '',
  sex:'sex',
});

const successMessage2 = ref('');
const errorMessage2 = ref('');

const submitSecondForm = async () => {
  try {
    const response = await fetch('http://localhost:3000/api/submit-volunteer-form', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(volunteerForm.value)
    });

    if (!response.ok) {
      throw new Error('Network response was not ok');
    }

    const data = await response.json();
    successMessage2.value = 'Form submitted successfully!';
    errorMessage2.value = '';
    volunteerForm.value = { name: '', email: '', phoneNumber:'', age:'', sex:'sex' }; // Reset form
    
  } catch (error) {
    errorMessage.value = 'There was a problem submitting the form.';
    console.error('Error:', error);
  }
};

</script>

<template>

  <section
    id="registration"
    class="bg-[#212121] py-8 px-4 mx-auto max-w-screen-xl lg:py-16 lg:px-6 overflow-hidden sm:grid sm:grid-cols-2 sm:items-center"
  >
    <div class="p-8 md:p-12 lg:px-16 lg:py-24">
      <div class="flex flex-col justify-center align-center text-center lg:text-start">
        <h2
          class="font-[Recharge] uppercase text-3xl font-bold text-white md:text-5xl dark:text-white"
        >
          Ready to <span class="text-[#ff5722]">Join Us</span> ?
        </h2>

        <p
          class="font-[Avenir_Next_Roman] font-light mt-4 text-gray-400 lg:mb-8 sm:text-xl dark:text-white"
        >
          Be part of the action by registering for the TAG Convention. Will you be an attendee,
          exhibitor, or sponsor, we have a place for everyone!
        </p>

        <div class="grid grid-cols-1 gap-4 mt-8 content-center max-w-screen">
          <div id="accordion-collapse" data-accordion="collapse">
            <h2 id="accordion-collapse-heading-1">
              <button
                 @click="toggleForm('first')"
                type="button"
                class="flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-b-0 border-gray-200 rounded-t-xl focus:ring-3 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-800 gap-3"
                data-accordion-target="#accordion-collapse-body-1"
                aria-expanded="true"
                aria-controls="accordion-collapse-body-1"
              >
                <span class="text-white">Register as Exhibitor</span>
                <svg
                  data-accordion-icon
                  :class="{'rotate-180' : !firstFormVisible }"
                  class="text-white w-3 h-3 shrink-0"
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 10 6"
                >
                  <path
                    stroke="currentColor"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M9 5 5 1 1 5"
                  />
                </svg>
              </button>
            </h2>
            <div id="accordion-collapse-body-1" aria-labelledby="accordion-collapse-heading-1">
              <div
                v-if="firstFormVisible"
                class="p-5 border border-b-0 border-gray-200 dark:border-gray-700 dark:bg-gray-900"
              >
                <form @submit.prevent="submitForm" class="max-w-md mx-auto">
                  <div class="relative z-0 w-full mb-5 group">
                    <input
                      type="name"
                      name="floating_name"
                      id="floating_name"
                      class="block py-2.5 px-0 w-full text-sm text-white bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-orange-500 peer"
                      placeholder="Contact Full Name"
                      v-model="formData.name"
                      required
                    />
                  </div>
                  <div class="relative z-0 w-full mb-5 group">
                    <input
                      type="email"
                      name="floating_email"
                      id="floating_email"
                      class="block py-2.5 px-0 w-full text-sm text-white bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-orange-500 focus:outline-none focus:ring-0 focus:border-orange-500 peer"
                      placeholder="Email"
                      v-model="formData.email"
                      required
                    />
                  </div>

                  <div class="grid md:grid-cols-2 md:gap-6">
                    <div class="relative z-0 w-full mb-5 group">
                      <input
                        type="text"
                        name="floating_company"
                        id="floating_company"
                        class="block py-2.5 px-0 w-full text-sm text-white bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-orange-500 focus:outline-none focus:ring-0 focus:border-orange-500 peer"
                        placeholder="Company Name"
                        v-model="formData.companyName"
                        required
                      />
                    </div>
                    <div class="relative z-0 w-full mb-5 group">
                      <input
                        type="tel"
                        name="floating_tel"
                        id="floating_tel"
                        class="block py-2.5 px-0 w-full text-sm text-white bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-orange-500 focus:outline-none focus:ring-0 focus:border-orange-500 peer"
                        placeholder="Phone Number"
                        v-model="formData.phoneNumber"
                        required
                      />
                    </div>
                  </div>
                  <div class="relative z-0 w-full mb-5 group">
                    <textarea
                      type="text"
                      name="floating_description"
                      id="floating_description"
                      class="block py-2.5 px-0 w-full text-sm text-white bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-orange-500 focus:outline-none focus:ring-0 focus:border-orange-500 peer"
                      placeholder="What is your business about ?"
                      rows="3"
                      v-model="formData.companyDescription"
                      required
                    ></textarea>
                  </div>
                  <div class="relative z-0 w-full mb-5 group">
                    <textarea
                      type="text"
                      name="floating_space_needed"
                      id="floating_space_needed"
                      class="block py-2.5 px-0 w-full text-sm text-white bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-orange-500 focus:outline-none focus:ring-0 focus:border-orange-500 peer"
                      placeholder="How much space will your business need ?"
                      rows="3"
                      v-model="formData.spaceNeeded"
                      required
                    ></textarea>
                  </div>

                  <button
                  
                    type="submit"
                    class="text-white bg-orange-500 hover:bg-orange-600 focus:ring-4 focus:outline-none focus:ring-orange-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-orange-500 dark:hover:bg-orange-600 dark:focus:ring-orange-700"
                  >
                    Submit
                  </button>
                  <p v-if="successMessage" class="success">{{ successMessage }}</p>
                  <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
                </form>
              </div>
            </div>
            <h2 id="accordion-collapse-heading-2">
              <button
             @click="toggleForm('second')"
                type="button"
                class="flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-b-0 border-gray-200 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-800 gap-3"
                data-accordion-target="#accordion-collapse-body-2"
                aria-expanded="false"
                aria-controls="accordion-collapse-body-2"
              >
                <span class="text-white">Register as Volunteer</span>
                <svg
                  data-accordion-icon
                  :class="{'rotate-180' : !secondFormVisible }"
                  class="text-white w-3 h-3  shrink-0"
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 10 6"
                >
                  <path
                    stroke="currentColor"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M9 5 5 1 1 5"
                  />
                </svg>
              </button>
            </h2>
            <div id="accordion-collapse-body-1" aria-labelledby="accordion-collapse-heading-1">
              <div
                v-if="secondFormVisible"
                class="p-5 border border-b-0 border-gray-200 dark:border-gray-700 dark:bg-gray-900"
              >
                <form @submit.prevent="submitSecondForm" class="max-w-md mx-auto">
                  <div class="relative z-0 w-full mb-5 group">
                    <input
                      type="name"
                      name="floating_volunteer_name"
                      id="floating_volunteer_name"
                      class="block py-2.5 px-0 w-full text-sm text-white bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-orange-500 peer"
                      placeholder="Full Name"
                      v-model="volunteerForm.name"
                      required
                    />
                  </div>
                  <div class="relative z-0 w-full mb-5 group">
                    <input
                      type="email"
                      name="floating_volunteer_email"
                      id="floating_volunteer_email"
                      class="block py-2.5 px-0 w-full text-sm text-white bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-orange-500 focus:outline-none focus:ring-0 focus:border-orange-500 peer"
                      placeholder="Email"
                      v-model="volunteerForm.email"
                      required
                    />
                  </div>
                  <div class="relative z-0 w-full mb-5 group">
                      <input
                        type="tel"
                        name="floating_tel"
                        id="floating_tel"
                        class="block py-2.5 px-0 w-full text-sm text-white bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-orange-500 focus:outline-none focus:ring-0 focus:border-orange-500 peer"
                        placeholder="Phone Number"
                        v-model="volunteerForm.phoneNumber"
                        required
                      />
                    </div>
                    <div class="relative z-0 w-full mb-5 group">
                      <input
                        type="number"
                        name="floating_volunteer_age"
                        id="floating_volunteer_age"
                        class="block py-2.5 px-0 w-full text-sm text-white bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-orange-500 focus:outline-none focus:ring-0 focus:border-orange-500 peer"
                        placeholder="Age"
                        min="0"
                        max="100"
                        v-model="volunteerForm.age"
                        required
                      />
                    </div>
                    <!-- <div class="relative z-0 w-full mb-5 group">
                      <select class="block py-2.5 px-0 w-full text-sm text-white border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-orange-500 focus:outline-none focus:ring-0 focus:border-orange-500 peer" id="age-range" name="age-range">
                        <option value="" disabled selected>Age Range</option>
                        <option value="18-20">18-20 years</option>
                        <option value="21-25">21-25 years</option>
                        <option value="26-30">26-30 years</option>
                        <option value="31-35">31-35 years</option>
                        <option value="36-40">36-40 years</option>
                        <option value="41-50">41-50 years</option>
                        <option value="51+">51+ years</option>
                      </select>
                    </div>
                   -->
                   <div class="relative z-0 w-full mb-5 group">
                      <select class="block py-2.5 px-0 w-full text-sm bg-[#212121] text-white border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-orange-500 focus:outline-none focus:ring-0 focus:border-orange-500 peer" id="age-range" name="age-range" v-model="volunteerForm.sex" required>
                        <option value="" disabled selected>Sex</option>
                        <option value="male">Male</option>
                        <option value="female">Female</option>
                      </select>
                    </div>
                  
                  <button
                    type="submit"
                    class="text-white bg-orange-500 hover:bg-orange-600 focus:ring-4 focus:outline-none focus:ring-orange-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-orange-500 dark:hover:bg-orange-600 dark:focus:ring-orange-700"
                  >
                    Submit
                  </button>
                  <p v-if="successMessage2" class="success">{{ successMessage2 }}</p>
                  <p v-if="errorMessage2" class="error">{{ errorMessage2 }}</p>
                </form>
              </div>
            </div>
            <h2 id="accordion-collapse-heading-3">
              <button
                type="button"
                class="flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-gray-200 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-800 gap-3"
                data-accordion-target="#accordion-collapse-body-3"
                aria-expanded="false"
                aria-controls="accordion-collapse-body-3"
              >
                <span class="text-white">Register as Sponsor</span>
                <svg
                  data-accordion-icon
                  class="text-white w-3 h-3 rotate-90 shrink-0"
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 10 6"
                >
                  <path
                    stroke="currentColor"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M9 5 5 1 1 5"
                  />
                </svg>
              </button>
            </h2>
          </div>
        </div>
      </div>
    </div>

    <img
      alt=""
      src="/images/1-min.jpg"
      class="h-full w-full object-cover sm:h-[calc(100%_-_2rem)] sm:self-end sm:rounded-ss-[30px] md:h-[calc(100%_-_4rem)] md:rounded-ss-[60px]"
    />
  </section>
</template>

<style scoped>
.success, .error{
  padding-top: 1rem;
  text-align: center;
}
.success{
  color: green;
}
.error{
  color: red;
}
</style>
