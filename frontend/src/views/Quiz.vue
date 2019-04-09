<template>
  <v-container>
    <v-list>
      <template v-for="(ques, i) in questions">
        {{ ques.question }}
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

    <v-btn @click="submit">Submit</v-btn>

    <p>{{ questions[0].selectedChoice || 'null' }}</p>
    <p>{{ questions[1].selectedChoice || 'null' }}</p>
  </v-container>
</template>


<script>
export default {
  name: "Quiz",
  data() {
    return {
      radioGroup: "",
      questions: [
        {
          question: "Question 1",
          position: "0",
          posMarks: "4",
          negMarks: "2",
          choices: [
            { id: "1", text: "Option 1" },
            { id: "2", text: "Option 2" },
            { id: "3", text: "Option 3" },
            { id: "4", text: "Option 4" }
          ]
        },
        {
          question: "Question 2",
          position: "1",
          posMarks: "4",
          negMarks: "2",
          choices: [
            { id: "1", text: "Option 1" },
            { id: "2", text: "Option 2" },
            { id: "3", text: "Option 3" },
            { id: "4", text: "Option 4" }
          ]
        }
      ]
    };
  },
  methods: {
      submit () {
          this.questions.forEach(ques => {
              console.log(ques.selectedChoice)
          });
      }
  },
  created () {
    const quiz_id = this.$route.params.id;
    console.log(quiz_id);
    Axios.create()
      .get("/api/quizes/" + quiz_id)
      .then(response => {
        this.questions = response.data;
      })
      .catch(err => console.log(err));
  }
};
</script>