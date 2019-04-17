<template>
<v-flex md8 offset-md2>
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

    <template v-if="model.type ==='student'">
      <v-menu
        ref="menu"
        v-model="menu"
        :close-on-content-click="false"
        :nudge-right="40"
        lazy
        transition="scale-transition"
        offset-y
        full-width
        min-width="290px"
      >
        <template v-slot:activator="{ on }">
          <v-text-field
            v-model="model.dob"
            label="Date of Birth"
            prepend-icon="event"
            readonly
            v-on="on"
          ></v-text-field>
        </template>
        <v-date-picker
          ref="picker"
          v-model="model.dob"
          :max="new Date().toISOString().substr(0, 10)"
          min="1950-01-01"
          @change="save"
        ></v-date-picker>
      </v-menu>
      
    </template>

    <v-checkbox
      v-model="checkbox"
      :rules="[v => !!v || 'You must agree to continue!']"
      label="Do you agree?"
      required
    ></v-checkbox>

    <v-btn :disabled="!valid" color="success" @click="validate">Validate</v-btn>

    <v-btn :disabled="!valid" color="info" @click="sendRequest">Send</v-btn>

    <v-btn color="error" @click="reset">Reset Form</v-btn>
  </v-form>
  </v-flex>
</template>
<script>
import Axios from "axios";

export default {
  name: "SignUp",
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
        .then(resp => {if(resp.status == 201) window.location.replace("http://localhost:8080") })
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