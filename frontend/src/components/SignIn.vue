<template>
  <v-form ref="form" v-model="valid" lazy-validation>
    <v-text-field v-model="model.email" :rules="emailRules" label="E-mail" required></v-text-field>
    <v-text-field
      v-model="model.password"
      :append-icon="show1 ? 'visibility' : 'visibility_off'"
      :rules="[rules.required, rules.min]"
      :type="show1 ? 'text' : 'password'"
      name="input-10-1"
      label="Enter Password"
      hint="At least 8 characters"
      counter
      @click:append="show1 = !show1"
    ></v-text-field>
    <v-btn @click="submit">Submit</v-btn>
</v-form>
</template>
<script>
import Axios from "axios";

export default {
  name: "SignIn",
  data: () => ({
    model: {
      
        email: "",
        password: "",
        username: ""
    },
    response: "",
    show1: false,
    rules: {
      required: value => !!value || "Required.",
      min: v => v.length >= 8 || "Min 8 characters",
      emailMatch: () => "The email and password you entered don't match"
    },
    emailRules: [
      v => !!v || "E-mail is required",
      v => /.+@.+/.test(v) || "E-mail must be valid"
    ],
    select: null,
    profileTypes: [
      { key: "Student", value: "student" },
      { key: "Instructor", value: "instructor" }
    ],
    checkbox: false
  }),
  methods: {
    save(date) {
      this.$refs.menu.save(date);
    },
    validate() {
      if (this.$refs.form.validate()) {
        this.snackbar = true;
      }
    },
    submit() {
      this.$httpClient
        .post("/api/sign-in/", this.model)
        .then(resp => console.log(resp))
        .catch(err => console.log(err.response));
    }
  },
    watch: {
      model: {
          handler (val) {
            this.model.username = val.email
          },
          deep: true
      }
  },
  mounted() {
    this.$httpClient
      .get("/api/departments/")
      .then(resp => (this.departments = resp.data))
      .catch(err => console.log(err));
  }
};
</script>
