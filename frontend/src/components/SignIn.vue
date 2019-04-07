<template>
  <v-form ref="form" v-model="valid" lazy-validation>
    <v-text-field v-model="model.user.email" :rules="emailRules" label="E-mail" required></v-text-field>
    <v-text-field
      v-model="model.user.password"
      :append-icon="show1 ? 'visibility' : 'visibility_off'"
      :rules="[rules.required, rules.min]"
      :type="show1 ? 'text' : 'password'"
      name="input-10-1"
      label="Enter Password"
      hint="At least 8 characters"
      counter
      @click:append="show1 = !show1"
    ></v-text-field>
</v-form>
</template>
<script>
import Axios from "axios";

export default {
  name: "SignIn",
  data: () => ({
    model: {
      user: {
        username: "",
        first_name: "",
        last_name: "",
        email: "",
        password: ""
      },
      type: "student",
      dob: "",
      roll_number: "",
      department: "",
      avatar: null,
      dob: null
    },
    response: "",
    show1: false,
    rules: {
      required: value => !!value || "Required.",
      min: v => v.length >= 8 || "Min 8 characters",
      emailMatch: () => "The email and password you entered don't match"
    },
    menu: false,
    valid: true,
    nameRules: [
      v => !!v || "Name is required",
      v => (v && v.length <= 10) || "Name must be less than 10 characters"
    ],
    emailRules: [
      v => !!v || "E-mail is required",
      v => /.+@.+/.test(v) || "E-mail must be valid"
    ],
    select: null,
    profileTypes: [
      { key: "Student", value: "student" },
      { key: "Instructor", value: "instructor" }
    ],
    departments: [],
    checkbox: false
  }),
  watch: {
    menu(val) {
      val && setTimeout(() => (this.$refs.picker.activePicker = "YEAR"));
    }
  },
  methods: {
    save(date) {
      this.$refs.menu.save(date);
    },
    validate() {
      if (this.$refs.form.validate()) {
        this.snackbar = true;
      }
    },
    reset() {
      this.$refs.form.reset();
    },
    sendRequest() {
      this.$httpClient
        .post("/api/sign-up/", this.model)
        .then(resp => console.log(resp))
        .catch(err => console.log(err.response));
    }
  },
  mounted() {
    this.$httpClient
      .get("/api/departments/")
      .then(resp => (this.departments = resp.data))
      .catch(err => console.log(err));
  },
  watch: {
      model: {
          handler (val) {
            this.model.user.username = val.user.email
          },
          deep: true
      }
  }
};
</script>
