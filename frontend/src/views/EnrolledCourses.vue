<template>
  <v-layout row>
    <v-flex xs12 sm10 offset-sm1>
      <v-toolbar color="cyan" dark>
        <v-toolbar-side-icon></v-toolbar-side-icon>

        <v-toolbar-title>Courses Being Offerings</v-toolbar-title>

        <v-spacer></v-spacer>
      </v-toolbar>

      <v-list three-line>
        <template v-for="(course, i) in courses" no-action>
          <v-list-tile :to="'/course-structure/' + course.course.code" :key="i">
            <v-list-tile-content>
              <v-list-tile-title v-html="course.course.name"></v-list-tile-title>
              <v-list-tile-sub-title>{{ course.course.code + ' | ' + course.instructor.user.username }}</v-list-tile-sub-title>
            </v-list-tile-content>
            <v-list-action>
              <v-flex class="text-sm-right">
                <v-btn color="info" :key="i" @click='pushFeedback' > Request Enrollment </v-btn>
              </v-flex>
            </v-list-action>
          </v-list-tile>
        </template>
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
      pushFeedback()
      {
          console.log("fgh")
          this.$router.push('Feedback')
      },
    log() {
      console.log("suthar", this.courses);
    }
  }
};
</script>
