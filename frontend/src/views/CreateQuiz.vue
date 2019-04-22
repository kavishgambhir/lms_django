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

      <v-flex sm6 class="pa-2">
        <v-text-field v-model="question.text" label="Enter Question"></v-text-field>
      </v-flex>

      <v-flex sm6 class="pa-2">
        <v-text-field v-model="queston.choice_ii" label="New Choice"></v-text-field>
      </v-flex>
      <v-flex sm6 class="pa-2">
        <v-btn @click="addChoice">Add New Choice</v-btn>
      </v-flex>

      <v-radio-group :key="i+1">
        <v-radio
          v-for="(choice, n) in question.choices"
          :key="n"
          :label="`${choice.text}`"
          :value="n+1"
        ></v-radio>
      </v-radio-group>
      
    </v-layout>

    <!-- <div v-if="isSending" class="loading">Sendig...</div> -->

    <form class="form" @submit="onSubmit">
      <button class="button">Create</button>
    </form>
  </div>
</template>


<script>
export default {
  data: () => ({
    quiz: {
      question: {},
      quiz: {},
      email: "",
      message: ""
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
      this.question.choices.push(this.question.choice_ii);
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