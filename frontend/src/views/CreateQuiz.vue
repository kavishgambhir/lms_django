<template>
  <div id="quiz-form" class="quiz-form">
    <h1 class="quiz-form_title">Create Quiz</h1>
    <div class="separator"></div>

    <span>Quiz Name : {{ quiz.name }}</span>
    <br>
    <!-- <span>{{ quiz.url }}</span>
    <br>-->
    <span>Start Time of quiz : {{ quiz.start_time }}</span>
    <br>
    <span>Duration of the quiz : {{ quiz.duration }}</span>
    <br>
    <span>End time of the quiz : {{ quiz.end_time }}</span>
    <br>
    <span>Is quiz active? : {{ quiz.is_active }}</span>
    <br>
    <span>Description of the quiz : {{ quiz.description }} </span>
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

    <v-layout wrap>
      <v-flex sm6 class="pa-2">
        <v-text-field v-model="quiz.name" label="Name"></v-text-field>
      </v-flex>
      <v-flex sm6 class="pa-2">
        <v-text-field v-model="quiz.start_time" label="Start Time"></v-text-field>
      </v-flex>
      <v-flex sm6 class="pa-2">
        <v-text-field v-model="quiz.duration" label="Duration"></v-text-field>
      </v-flex>
      <v-flex sm6 class="pa-2">
        <v-text-field v-model="quiz.end_time" label="End Time"></v-text-field>
      </v-flex>
      <v-flex sm6 class="pa-2">
        <v-text-field v-model="quiz.is_actiove" label="Is Active"></v-text-field>
      </v-flex>
      <v-flex sm6 class="pa-2">
        <v-text-field v-model="quiz.description" label="Description"></v-text-field>
      </v-flex>

      <v-flex sm12 class="pa-2">
        <v-text-field v-model="question.text" label="Enter Question"></v-text-field>
      </v-flex>

      <v-flex sm3 class="pa-2">
        <v-text-field v-model="question.choice_ii" label="New Choice"></v-text-field>
      </v-flex>
      <v-flex sm3 class="pa-2">
        <v-text-field v-model="question.choice_ij" label="ID"></v-text-field>
      </v-flex>
      <v-flex sm3 class="pa-2">
        <v-btn @click="addChoice" color="info">Add New Choice</v-btn>
      </v-flex>
      <v-flex sm3 class="pa-2" offset-sm1>
        <v-text-field v-model="question.correct_choice" label="Correct Choice"></v-text-field>
      </v-flex>
      <v-flex sm3 class="pa-2">
        <v-text-field v-model="question.positive_marks" label="Positive Marks"></v-text-field>
      </v-flex>
      <v-flex sm3 class="pa-2">
        <v-text-field v-model="question.negative_marks" label="Negative Marks"></v-text-field>
      </v-flex>

      <v-flex sm12 class="pa-2 text-xs-right">
        <v-btn @click="addQuestion" color="success">Add New Question</v-btn>
      </v-flex>

      <span>{{ question.text }}</span>

      <v-radio-group>
        <v-radio
          v-for="(choice, n) in question.choices"
          :key="n"
          :label="`${choice.text}`"
          :value="n+1"
        ></v-radio>
      </v-radio-group>
    </v-layout>

    <!-- <div v-if="isSending" class="loading">Sendig...</div> -->

    <v-btn color="success" @click="createQuiz">Create Quiz</v-btn>
  </div>
</template>


<script>
import Axios from "axios";
import { httpClient } from "../plugins/httpClient";
export default {
  data: () => ({
    question: {
      choices: []
    },
    quiz: {
      questions: []
    },

    isSending: false
  }),
  methods: {
    clearForm() {
      for (let field in this.quiz) {
        this.quiz[field] = "";
      }
    },
    addChoice() {
      const self = this;
      this.question.choices.push({ text: self.question.choice_ii, id: self.question.choice_ij });
    },
    addQuestion() {
      const self = this;
      this.quiz.questions.push(self.question);
    },
    createQuiz() {
      const self = this;
      //   httpClient
      //     .post("http://localhost:8000/api/quizes/", self.quiz)
      //     .then(response => {
      //       console.log(response.data);
      //     });
      this.$httpClient
        .post("/api/quizes/", self.quiz)
        .then(resp => {
          if (resp.status == 201)
            window.location.replace("http://localhost:8080");
          console.log(resp);
        })
        .catch(err => console.log(err.response));
      //   const request = Axios.post(
      //     "http://localhost:8000/api/quizes/",
      //     self.quiz
      //   );
    },

    /**
     * Handler for submit
     */

    onSubmit(evt) {
      evt.preventDefault();

      this.isSending = true;

      setTimeout(() => {
        // Build for data
        let form = new FormData();
        for (let field in this.quiz) {
          form.append(field, this.quiz[field]);
        }

        // Send form to server
        this.$http
          .post("/app.php", form)
          .then(response => {
            console.log(response);
            this.clearForm();
            this.isSending = false;
          })
          .catch(e => {
            console.log(e);
          });
      }, 1000);
    }
  }
};
</script>