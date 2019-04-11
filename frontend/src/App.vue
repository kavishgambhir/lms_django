<template>
  <v-app id="app">

    <v-navigation-drawer :clipped="$vuetify.breakpoint.lgAndUp" v-model="drawer" fixed app>
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
    </v-navigation-drawer>

    <v-toolbar :clipped-left="$vuetify.breakpoint.lgAndUp" app fixed>
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

    </v-toolbar>

    <v-content>
      <v-container>
        <router-view/>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      drawer: true,
      items: [
          {icon: 'mdi mdi-account-circle', title: 'Home', path: '/home'},
          {icon: 'mdi mdi-calendar', title: 'Calendar', path: '/calendar'},
          {icon: 'mdi mdi-file', title: 'Quiz', path: '/quizes'}
      ]
      //

    };
  }
};
</script>
