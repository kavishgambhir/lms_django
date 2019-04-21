<template>
  <v-form ref="form" lazy-validation>
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
    <v-btn color="blue" @click="submit">Go</v-btn>
    <v-alert :value="true" color="error" icon="warning" outline v-if="showError">{{errorMessage}}</v-alert>
  </v-form>
</template>
<script>
import Axios from "axios";
import { mapActions } from "vuex";

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
    checkbox: false,
    showError: false,
    errorMessage: 'Invalid Credentials'
  }),
  methods: {
    ...mapActions("profile", ["setProfile"], "auth", ["login"]),
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
        .then(resp => {
          this.setProfile(resp.data);
          localStorage.setItem("profile", JSON.stringify(resp.data));
          this.$store.dispatch("auth/login");
          this.$router.push({ name: "Dashboard" });
        })
        .catch( (err) => {console.log(err) , this.showError=true });
    }
  },
  watch: {
    model: {
      handler(val) {
        this.model.username = val.email;
      },
      deep: true
    }
  },
  mounted() {
  }
};
</script>
