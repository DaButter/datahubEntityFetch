<template>
  <div class="container padding-v-2">
    <div class="row">
      <div class="col">
        <h1 class="d3">VueJS + Flask Fullstack Example</h1>
      </div>
    </div>

    <div class="row row--gutters">
      <div
        class="col-lg-6"
        v-for="(entity, index) in entities"
        :key="entity.urn"
      >
        <sdx-card
          layout="interaction"
          :label="entity.name"
          label-aria-level="4"
          :href-label="entity.description"
          href="javascript:;"
          href-aria-label="Open new website."
        ></sdx-card>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data() {
    return {
      entities: []
    };
  },
  mounted() {
    axios.get('/api')
      .then(response => {
        console.log('Fetched entities: ', response.data)
        this.entities = response.data;
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }
};
</script>
