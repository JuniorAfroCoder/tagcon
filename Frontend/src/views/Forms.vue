<script setup>
import { ref, onMounted } from 'vue';

const forms = ref([]);
const loading = ref(false);
const error = ref(null);
const pagination = ref({
  page: 1,
  limit: 10,
  total: 0
});

const fetchCombinedForms = async () => {
  try {
    loading.value = true;
    const response = await fetch(
      `http://localhost:3000/api/forms/combined?page=${pagination.value.page}&limit=${pagination.value.limit}`
    );
    
    if (!response.ok) throw new Error('Failed to fetch forms');
    
    const data = await response.json();
    forms.value = data.forms;
    pagination.value = {
      ...pagination.value,
      total: data.meta.total,
      pages: data.meta.pages
    };
  } catch (err) {
    error.value = err.message;
  } finally {
    loading.value = false;
  }
};

const changePage = (newPage) => {
  pagination.value.page = newPage;
  fetchCombinedForms();
};

onMounted(fetchCombinedForms);
</script>

<template>
  <div>
    <h2>All Form Submissions</h2>
    
    <div v-if="loading">Loading...</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    
    <table v-else>
      <thead>
        <tr>
          <th>Type</th>
          <th>Name</th>
          <th>Details</th>
          <th>Date</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="form in forms" :key="form._id">
          <td>{{ form.__t || 'Contact' }}</td> <!-- __t is the discriminator if using mongoose discriminators -->
          <td>{{ form.name || form.respondentName }}</td>
          <td>
            <span v-if="form.email">Email: {{ form.email }}</span>
            <span v-if="form.answers">Survey Responses: {{ form.answers.length }}</span>
          </td>
          <td>{{ new Date(form.createdAt).toLocaleString() }}</td>
        </tr>
      </tbody>
    </table>

    <div class="pagination">
      <button 
        v-for="page in pagination.pages" 
        :key="page"
        @click="changePage(page)"
        :class="{ active: pagination.page === page }"
      >
        {{ page }}
      </button>
    </div>
  </div>
</template>