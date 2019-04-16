<template>
  <v-app>
    <core-filter/>

    <v-app id="app">

      <!-- <v-navigation-drawer :clipped="$vuetify.breakpoint.lgAndUp" v-model="drawer" fixed app>
      <v-list>
        <v-list-tile v-for="(item,i) in items" :key="i" :to="item.path">
          <v-list-tile-action>
            <v-icon>{{item.icon}}</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>{{item.title}}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
      </v-navigation-drawer>-->

      <!-- <v-toolbar :clipped-left="$vuetify.breakpoint.lgAndUp" app fixed>
      <v-toolbar-title class="headline text-uppercase">
        <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
        <span>
          <router-link to="/home" tag="span" style="cursor: pointer">
            Smart Class
          </router-link>
        </span>
      </v-toolbar-title>
      <v-spacer></v-spacer>

      <v-btn flat to="/calendar">
        <v-icon>mdi mdi-calendar</v-icon>
      </v-btn>
      
      <v-btn flat href="https://github.com/vuetifyjs/vuetify/releases/latest" target="_blank">
        <span class="mr-2">Login</span>
        <v-icon>fa-external-link</v-icon>
      </v-btn>

      </v-toolbar>-->

     <!--  <core-toolbar/>

      <core-drawer/>

      <core-view/> -->

      <core-toolbar v-if="isLoggedIn"/>

      <core-drawer v-if="isLoggedIn"/>

      <core-view />
    </v-app>

  </v-app>
</template>


<style lang="scss">
@import "@/styles/index.scss";

/* Remove in 1.2 */
.v-datatable thead th.column.sortable i {
  vertical-align: unset;
}
</style>

<script>
import {mapGetters, mapActions} from 'vuex'

export default {

  name: "App",
  computed:
  {
    ...mapGetters('auth', ['isLoggedIn'])
  },
  data() {
    return {
      drawer: true,
      items: [
        { icon: "mdi mdi-account-circle", title: "Home", path: "/home" },
        { icon: "mdi mdi-calendar", title: "Calendar", path: "/calendar" },
        { icon: "mdi mdi-file", title: "Quiz", path: "/quizes" },
        { icon: "mdi mdi-file", title: "Feedback", path: "/feedback" }
      ]
      //
    };
  },
  methods: {
    ...mapActions('profile', [
      'setProfile'
    ],
    'auth',
    ['login']),
  },
  created() {
    const x = localStorage.getItem('profile')
    // console.log(x)
    this.setProfile(JSON.parse(x))
  }
};
</script>

