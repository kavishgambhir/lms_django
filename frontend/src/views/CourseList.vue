<template>
  <v-layout row>
    <v-flex xs12 sm10 offset-sm1>
      <v-toolbar color="cyan" dark>
        <v-toolbar-side-icon></v-toolbar-side-icon>

        <v-toolbar-title>Your Course Offerings</v-toolbar-title>

        <v-spacer></v-spacer>
      </v-toolbar>

      <v-list two-line>
        <v-list-group v-for="(course, i) in courses" :key="i" v-model="course.active" no-action>
          <template v-slot:activator>
            <v-list-tile>
              <v-list-tile-content>
                <v-list-tile-title v-html="course.course.name"></v-list-tile-title>
                <v-list-tile-sub-title>{{ course.course.code + ' | ' + course.instructor.user.username }}</v-list-tile-sub-title>
              </v-list-tile-content>
            </v-list-tile>
          </template>

          <v-list-tile v-for="(student, k) in course.enrolled_students" :key="k" @click>
            <v-list-tile-content>
              <v-list-tile-title>{{ student.user.username }}</v-list-tile-title>
              <v-list-tile-sub-title>{{ student.roll_number + ' | ' + student.department.name }}</v-list-tile-sub-title>
            </v-list-tile-content>

            <v-list-tile-action>
              <v-icon>{{ student.action }}</v-icon>
            </v-list-tile-action>
          </v-list-tile>
        </v-list-group>
      </v-list>
    </v-flex>
  </v-layout>
</template>
<script>
import Axios from "axios";
import { mapActions, mapGetters } from "vuex";

export default {
  computed: {
    ...mapActions("course", ["setCourses"]),
    ...mapGetters("course", ["courses"])
  },
  data() {
    return {
      suthar: ""
    };
  },
  beforeMount() {
    // this.setCourses();
    this.$store.dispatch("course/setCourses");
  },
  methods: {
    log() {
      console.log("suthar", this.courses);
    }
  }
};
</script>
