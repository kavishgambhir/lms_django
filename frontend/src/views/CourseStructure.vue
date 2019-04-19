<template>
  <v-container fluid grid-list-md>
      <v-card>
      <v-card-title class="subheading font-weight-bold">Resources</v-card-title>

      <v-divider></v-divider>

      <v-list two-line>
        <template v-for="(item, i) in items">
          <v-list-tile :key="i" @click="log">
            <v-list-tile-title>{{ item.type + ' ' + item.file }}</v-list-tile-title>
            <!-- <v-list-tile-sub-title>{{ student.roll_number + ' | ' + student.user.username + ' | ' + student.department.name }}</v-list-tile-sub-title> -->
          </v-list-tile>
        </template>
      </v-list>
    </v-card>
    <v-card>
      <v-card-title class="subheading font-weight-bold">Students Enrolled</v-card-title>

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
  </v-container>
</template>

<script>
import Axios from "axios";
import { mapActions, mapGetters } from "vuex";
export default {
  computed: {
    ...mapGetters("course", ["courses"]),
    students() {
      const self = this;
      const list = this.courses.filter(function(el) {
        return el.course.code === self.$route.params.id;
      });
      if(list.length > 0) return list[0].enrolled_students;
      else return [];
    }
  },
  data() {
    return {
      suthar: "",
      items: ''
    };
  },
  created() {
    console.log(this.$route.params.id);
    const self=this;
    Axios.create().get('/api/files/').then(response => {
        self.items = response.data
        console.log("saksham",self.items)
    }).catch(err => console.log(err))
    
  },
  beforeMount() {
    // this.setCourses();
    this.$store.dispatch("course/setCourses");
  },
  methods: {
    log() {
      console.log("suthar", this.students[0].enrolled_students);
    }
  }
};
</script>