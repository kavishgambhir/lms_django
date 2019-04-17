<template>
  <v-layout row>
    <v-flex xs12 sm10 offset-sm1>
      <v-toolbar color="cyan" dark>
        <v-toolbar-side-icon></v-toolbar-side-icon>

        <v-toolbar-title>Student Database</v-toolbar-title>

        <v-spacer></v-spacer>
      </v-toolbar>

      <v-list two-line>
        <v-list-group v-for="(student, i) in studentList" :key="i" v-model="student.active" no-action>
          <template v-slot:activator>
            <v-list-tile avatar> 
              <v-list-tile-avatar>
                <img :src="student.avatar">
              </v-list-tile-avatar>
              <v-list-tile-content>
                <v-list-tile-title > {{ student.user.first_name+' '+student.user.last_name }} </v-list-tile-title>
                <v-list-tile-sub-title>{{ student.roll_number + ' | ' + student.user.username }}</v-list-tile-sub-title>
              </v-list-tile-content>
            </v-list-tile>
          </template>

          <span>{{ student }}</span>
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
    ...mapActions("studentList", ["setStudentList"], "course", ["setCourses"]),
    ...mapGetters("studentList", ["studentList"], "course", ["courses"]),
  },
  data() {
    return {
    };
  },
  beforeMount() {
    // this.setStudentList();
    this.$store.dispatch("studentList/setStudentList");
    this.$store.dispatch("course/setCourses");
  },
  methods: {
    log() {
      console.log("suthar", this.courses);
      console.log("test", this.studentList);
    }
  }
};
</script>
