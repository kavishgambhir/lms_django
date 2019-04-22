<template>
  <v-container>
    <span>Quiz Name : {{ quiz.name }}</span>
    <br>
    <!-- <span>{{ quiz.url }}</span>
    <br> -->
    <span>Start Time of quiz : {{ quiz.start_time }}</span>
    <br>
    <span>Duration of the quiz : {{ quiz.duration }}</span>
    <br>
    <span>End time of the quiz : {{ quiz.end_time }}</span>
    <br>
    <span>Is quiz active? : {{ quiz.is_active }}</span>
    <br>
    <span>Description of the quiz : {{ quiz.description }}</span>
    <br>

    <v-list>
      <template v-for="(ques, i) in quiz.questions">
        {{ ques.text }}
        <v-radio-group v-model="ques.selectedChoice" :key="i+1">
          <v-radio
            v-for="(choice, n) in ques.choices"
            :key="n"
            :label="`${choice.text}`"
            :value="n+1"
          ></v-radio>
        </v-radio-group>
      </template>
    </v-list>

    <v-btn @click="submit" color="info">Submit</v-btn>
    <br>
    <span v-if="marks">Marks Obtained: {{ marks }}</span>
  </v-container>
</template>


<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "Quiz",
  data() {
    return {
      radioGroup: "",
      marks: false
    };
  },
  methods: {
    submit() {
      var marks = 0;
      this.quiz.questions.forEach(ques => {
        if(ques.selectedChoice === ques.correct_choice) {
          marks += ques.positive_marks
        }else {
          marks += ques.negative_marks
        }
      });
      console.log(marks);
      this.marks = marks;
      
    }
  },
  computed: {
    ...mapActions("quizes", ["setQuizes"]),
    ...mapGetters("quizes", ["quizes"]),
    quiz() {
      const self = this;
      const list = this.quizes.filter(function(el) {
        return el.name === self.$route.params.id;
      });
      if (list.length > 0) return list[0];
      else return [];
    }
  },
  created() {
    console.log("suthar");

    const quiz_id = this.$route.params.id;
    console.log(quiz_id);
  }
};
</script>