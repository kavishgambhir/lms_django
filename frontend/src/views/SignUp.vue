<template>
  <v-form ref="form" v-model="valid" lazy-validation>
    <h1>Sign Up</h1>
    <v-text-field
      v-model="model.user.first_name"
      :counter="10"
      :rules="nameRules"
      label="First Name"
      required
    ></v-text-field>
    <v-text-field
      v-model="model.user.last_name"
      :counter="10"
      :rules="nameRules"
      label="Last Name"
      required
    ></v-text-field>

    <v-text-field v-model="model.user.email" :rules="emailRules" label="E-mail" required></v-text-field>
    <v-radio-group v-model="model.type" label="Role" required>
      <v-radio v-for="item in profileTypes" :key="item.value" :label="item.key" :value="item.value"></v-radio>
    </v-radio-group>

    <v-select
      v-model="model.department"
      :items="departments"
      item-text="name"
      item-value="url"
      label="Department"
    ></v-select>

    <v-text-field
      v-if="model.type === 'student'"
      v-model="model.roll_number"
      label="Roll Number"
      required
    ></v-text-field>

    <v-checkbox
      v-model="checkbox"
      :rules="[v => !!v || 'You must agree to continue!']"
      label="Do you agree?"
      required
    ></v-checkbox>

    <v-btn :disabled="!valid" color="success" @click="validate">Validate</v-btn>

    <v-btn :disabled="!valid" color="info" @click="sendRequest">Send</v-btn>

    <v-btn color="error" @click="reset">Reset Form</v-btn>

    <v-btn color="warning" @click="resetValidation">Reset Validation</v-btn>
  </v-form>
</template>
<script>
import Axios from "axios";

export default {
    name: 'SignUp',
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
      avatar: null
    },
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

  methods: {
    validate() {
      if (this.$refs.form.validate()) {
        this.snackbar = true;
      }
      console.log(data);
    },
    reset() {
      this.$refs.form.reset();
    },
    resetValidation() {
      this.$refs.form.resetValidation();
    },
    sendRequest() {
      Axios.create().post("/api/sign-up", data);
    }
  },
  mounted() {
    Axios.create()
      .get("/api/departments/")
      .then(resp => (this.departments = resp.data))
      .catch(err => console.log(err));
  }
};
</script>