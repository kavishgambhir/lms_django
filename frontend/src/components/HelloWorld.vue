<template>
  <v-container>
    <v-layout text-xs-center wrap>
      <v-flex xs12>
        <v-img :src="require('../assets/logo.svg')" class="my-3" contain height="200"></v-img>
      </v-flex>

      <v-flex mb-4>
        <h1 class="display-2 font-weight-bold mb-3">Welcome to Smartclass</h1>
      </v-flex>

      <v-flex mb-5 xs12>
        <v-btn>Sign-Up</v-btn>
        <v-btn>Sign-In</v-btn>
      </v-flex>
    </v-layout>
  </v-container>
</template>
