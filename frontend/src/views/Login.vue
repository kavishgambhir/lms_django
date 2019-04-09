<template v-if="signUpVisible">
  <form v-on:submit.prevent="onSubmit">
    <input v-model="email" name="email" type="email">
    <input v-model="password" name="password" type="password">
    <input type="submit" value="Sign In">
  </form>
  <!-- <a href="#" v-on:click="hideSignUp">X</a> -->
</template>

<script>
</script>