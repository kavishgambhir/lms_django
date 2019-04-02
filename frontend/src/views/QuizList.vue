<template>
  <v-layout row>
    <v-flex xs12 sm6 offset-sm3>
      <v-card>
        <v-list two-line>
          <template v-for="(item, index) in items">
            <v-list-tile :key="item.name" ripple>
              <v-list-tile-content>
                <v-list-tile-title>{{ item.name }}</v-list-tile-title>
                <v-list-tile-sub-title class="text--primary">{{ item.start_time }}</v-list-tile-sub-title>
                <v-list-tile-sub-title>{{ item.duration }}</v-list-tile-sub-title>
                <span>Is Active: {{ item.is_active ? 'Yes' : 'No' }}</span>
              </v-list-tile-content>
            </v-list-tile>
            <v-divider v-if="index + 1 < items.length" :key="index"></v-divider>
          </template>
        </v-list>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
import Axios from 'axios'

export default {
  name: "QuizListView",
  data() {
    return {
      items: []
    };
  },
  created () {
    Axios.create().get('/api/quizes/').then(response => {
        this.items = response.data
    }).catch(err => console.log(err))
  }
};
</script>
