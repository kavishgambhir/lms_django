<template>
<div>
  <v-container v-if="!signUpForm">
    <v-layout text-xs-center wrap>
      <v-flex xs12>
        <v-img :src="require('../assets/logo.svg')" class="my-3" contain height="200"></v-img>
      </v-flex>

      <v-flex mb-4>
        <h1 class="display-2 font-weight-bold mb-3">Welcome to Smartclass</h1>
      </v-flex>

      <v-flex mb-5 xs12>
        <v-btn  color="red" v-on:click="signUp">Sign-Up</v-btn>
        <v-btn color="green" v-on:click="signIn">Sign-In</v-btn>
      </v-flex>
    </v-layout>
  </v-container>
  <SignIn v-if="signInForm"/>
  <SignUp v-if="signUpForm"/>
</div>
</template>
<script>
import SignIn from '../components/core/SignIn'
import SignUp from '../components/core/SignUp'
export default {
  
data: () => ({
  signInForm: false,
  signUpForm: false
}),
components:
{
  'SignIn': SignIn,
  'SignUp': SignUp
},
  methods: {
    signIn() {
      this.signInForm=true;
      this.signUpForm=false;

    },
    signUp() {
      this.signUpForm=true;
      this.signInForm=false;
      

    }
  }
}
</script>


