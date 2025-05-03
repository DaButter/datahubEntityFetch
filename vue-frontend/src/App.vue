<template>
  <div class="container padding-v-2">
    <div class="row">
      <div class="col">
        <h1 class="d3">VueJS+Flask Fullstack Example</h1>
        <table>
          <thead>
            <tr>
              <th>Name</th>
              <th>Description</th>
              <th>Platform</th>
              <th>Type</th>
              <th>URN</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(entity, index) in entities" :key="index">
              <td>{{ entity.name }}</td>
              <td>{{ entity.description }}</td>
              <td>{{ entity.platform }}</td>
              <td>{{ entity.type }}</td>
              <td>{{ entity.urn }}</td>
            </tr>
          </tbody>
        </table>
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
        console.log("AUSTRIS LOX")
        console.log(response.data)
        this.entities = response.data;
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }
};
</script>
