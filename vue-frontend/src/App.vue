<template>
  <div class="container padding-v-2">
    <div class="row">
      <div class="col">
        <h1 class="d3">VueJS + Flask Fullstack app by Austris</h1>
      </div>
    </div>

    <!-- Error Notification -->
    <div v-if="error" class="row margin-bottom-3">
      <div class="col">
        <sdx-card
          layout="inline-notification"
          notification-type="warning"
          :label="error"
          label-aria-level="3">
          Failed to load entity data. Please try again.
        </sdx-card>
      </div>
    </div>

    <div class="row" v-if="!entities.length">
      <div class="col">
        <sdx-button-group layout="fixed">
          <sdx-button
            theme="confirm"
            :label="isLoading ? 'Loading...' : 'Load Entities'"
            @click="fetchEntities"
            icon-name="icon-download"
            :disabled="isLoading"
          ></sdx-button>
        </sdx-button-group>
      </div>
    </div>

    <div v-if="entities.length" class="row row--gutters">
      <div
        class="col-lg-6 col-xl-4"
        v-for="entity in entities"
        :key="entity.urn"
      >
        <sdx-card :label="entity.name" label-aria-level="2">
          <p>{{entity.description}}</p>
          <sdx-tag :label="entity.platform" icon-name="icon-database"></sdx-tag>
        </sdx-card>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'App',
  data() {
    return {
      entities: [],
      error: null,
      isLoading: false
    };
  },
  methods: {
    async fetchEntities() {
      try {
        this.isLoading = true;
        this.error = null;
        const { data } = await axios.get('/api/fetch_entities');
        this.entities = data;
      } catch (error) {
        console.error('Error fetching data: ', error);
        this.error = error.response?.data?.error || error.message || 'Failed to load entity data!';
      } finally {
        this.isLoading = false;
      }
    }
  },
});
</script>