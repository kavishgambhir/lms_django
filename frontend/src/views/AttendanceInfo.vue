<template>
  <v-container>

<span>Student: {{ $route.params.roll_number }} Course: {{ $route.params.course_id }}</span>

    <v-list>
      <v-list-tile v-for="(item, i) in items" :key="i">
        <v-list-tile-content>
          <v-list-tile-title>{{ item.date + ' April, 2019' }}</v-list-tile-title>
        </v-list-tile-content>
        <div>
          <v-switch v-model="item.present" :label="item.present ? 'Present' : 'Absent'"></v-switch>
        </div>
      </v-list-tile>
    </v-list>
    <v-flex class="text-xs-right">
      <v-btn color="success" @click="saveAttendance">Save Attendance</v-btn>
    </v-flex>
  </v-container>
</template>


<script>
export default {
  computed: {},
  data() {
    return {
      items: [
        { date: "1", present: false },
        { date: "2", present: false },
        { date: "3", present: false },
        { date: "4", present: false },
        { date: "5", present: false },
        { date: "6", present: false },
        { date: "7", present: false },
        { date: "8", present: false },
        { date: "9", present: false },
        { date: "10", present: false },
        { date: "11", present: false },
        { date: "12", present: false },
        { date: "13", present: false },
        { date: "14", present: false },
        { date: "15", present: false },
        { date: "16", present: false },
        { date: "17", present: false },
        { date: "18", present: false },
        { date: "19", present: false },
        { date: "20", present: false },
        { date: "21", present: false },
        { date: "22", present: false },
        { date: "23", present: false },
        { date: "24", present: false },
        { date: "25", present: false },
        { date: "26", present: false },
        { date: "27", present: false },
        { date: "28", present: false },
        { date: "29", present: false },
        { date: "30", present: false },
        { date: "31", present: false },
      ]
    };
  },
  created() {
    console.log(this.$route.params.course_id);
    console.log(this.$route.params.roll_number);
    const course_id = this.$route.params.course_id;
    const roll_number = this.$route.params.roll_number;
    const x = JSON.parse(localStorage.getItem(course_id + '-' + roll_number))
    if(x && x.length > 30) this.items = x;
  },
  beforeMount() {},
  methods: {
    log() {
      console.log("suthar");
    },
    saveAttendance() {
      const course_id = this.$route.params.course_id;
      const roll_number = this.$route.params.roll_number;
      localStorage.setItem(
        course_id + "-" + roll_number,
        JSON.stringify(this.items)
      );
    }
  }
};
</script>
