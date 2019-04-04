<template>
  <v-layout row>
    <v-flex xs12 sm8 offset-sm2>
      <v-card>
        <v-list three-line>
          <template v-for="(item, index) in items">
            <v-list-tile :key="item.name" ripple xs12 @click="route(item.url)">
              <v-layout row wrap>

                <v-flex xs11 mb-2>
                  <span class="display-1 font-weight-regular text-capitalize">{{ item.name }}</span>
                </v-flex>

                <v-flex xs1 text-xs-right>
                  <v-icon v-if="item.is_active" class="mdi mdi-circle" small color="green"></v-icon>
                  <v-icon v-else  class="mdi mdi-circle-outline" small></v-icon>
                </v-flex>

                <v-flex xs12>
                  <span>{{ item.description }}</span>
                </v-flex>

                <v-flex xs4>
                  <span>{{ item.start_time }}</span>
                </v-flex>

                <v-flex xs4>
                  <span>{{ item.end_time }}</span>
                </v-flex>

                <v-flex xs4 text-xs-right>
                  <span>{{ item.duration }}</span>
                </v-flex>

              </v-layout>
              
              <!-- <v-list-tile-content>
                <v-list-tile-title class="display-1">
                  {{ item.name }}
                </v-list-tile-title>
                <v-list-tile-sub-title class="text--primary">{{ item.start_time }}</v-list-tile-sub-title>
                <v-list-tile-sub-title>{{ item.duration }}</v-list-tile-sub-title>
                <span>Is Active: {{ item.is_active ? 'Yes' : 'No' }}</span>
              </v-list-tile-content> -->
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
  methods :{
    route(url){
      window.location.href = url;
    }
  },
  created () {
    Axios.create().get('/api/quizes/').then(response => {
        this.items = response.data
    }).catch(err => console.log(err))
  }
};
</script>
