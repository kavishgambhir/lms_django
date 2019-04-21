<template>
  <v-layout row>
    <v-flex xs12 sm6 offset-xs1>
   <v-card>
      <v-card-title class="subheading font-weight-bold">Your Courses</v-card-title>

      <v-divider></v-divider>

      <v-list two-line>
        <template v-for="(student, i) in students">
          <v-list-tile :key="i" @click="log">
            <v-list-tile-title>{{ student.user.first_name + ' ' + student.user.last_name }}</v-list-tile-title>
            <v-list-tile-sub-title>{{ student.roll_number + ' | ' + student.user.username + ' | ' + student.department.name }}</v-list-tile-sub-title>
          </v-list-tile>
        </template>
      </v-list>
    </v-card>
    </v-flex>
    <v-flex xs12 sm2 offset-xs1>
   <v-card>
      <v-card-title class="subheading font-weight-bold">More Courses</v-card-title>

      <v-divider></v-divider>

      <v-list two-line>
        <template v-for="(student, i) in students">
          <v-list-tile :key="i" @click="log">
            <v-list-tile-title>{{ student.user.first_name + ' ' + student.user.last_name }}</v-list-tile-title>
            <v-list-tile-sub-title>{{ student.roll_number + ' | ' + student.user.username + ' | ' + student.department.name }}</v-list-tile-sub-title>
          </v-list-tile>
        </template>
      </v-list>
    </v-card>
    </v-flex>
  </v-layout>
</template>
<script>
import Axios from "axios";
import { mapActions, mapGetters } from "vuex";

export default {
  computed: {
    ...mapActions("course", ["setCourses"]),
    ...mapGetters("course", ["courses"]),
    ...mapGetters("profile", ["profile"])
  },
  data() {
    return {
      suthar: ""
    };
  },
  beforeMount() {
    // this.setCourses();
    this.$httpClient.get('/'+this.profile.url.replace (/^[a-z]{4,5}\:\/{2}[a-z]{1,}\:[0-9]{1,4}.(.*)/, '$1')+'enrolled_courses/')
    .then(resp => {console.log("courses",resp), this.$store.dispatch("course/setEnrolledCourses",resp.data);})
    .catch(err=>{})
  },
  methods: {
    log() {
      console.log("suthar", this.courses);
    }
  }
};
</script>
