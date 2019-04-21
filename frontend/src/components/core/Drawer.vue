<template>
  <v-navigation-drawer
    id="app-drawer"
    v-model="inputValue"
    app
    dark
    floating
    persistent
    mobile-break-point="991"
    width="260"
  >
    <v-img
      :src="image"
      height="100%"
    >
      <v-layout
        class="fill-height"
        tag="v-list"
        column
      >
        <v-list-tile avatar>
          <v-list-tile-avatar
            color="white"
          >
            <v-img
              :src="logo"
              height="34"
              contain
            />
          </v-list-tile-avatar>
          <v-list-tile-title class="title" value="">
            Welcome {{user.first_name}}
          </v-list-tile-title>
        </v-list-tile>
        <v-divider/>
        <v-list-tile
          v-if="responsive"
        >
          <v-text-field
            class="purple-input search-input"
            label="Search..."
            color="purple"
          />
        </v-list-tile>
        <v-list-tile
          v-for="(link, i) in links"
          :key="i"
          :to="link.to"
          :active-class="color"
          avatar
          class="v-list-item"
          v-if="link.profile === 'all' || profileType === link.profile"
        >
          <v-list-tile-action>
            <v-icon>{{ link.icon }}</v-icon>
          </v-list-tile-action>
          <v-list-tile-title
            v-text="link.text"
          />
        </v-list-tile>
      </v-layout>
    </v-img>
  </v-navigation-drawer>
</template>

<script>
// Utilities
import {
  mapMutations,
  mapState,
  mapGetters
} from 'vuex'
export default {
  data: () => ({
    logo: './img/vuetifylogo.png',
    links: [
      {
        to: '/dashboard',
        icon: 'mdi-view-dashboard',
        text: 'Dashboard',
        profile: 'all'
      },
      {
        to: '/user-profile',
        icon: 'mdi-account',
        text: 'User Profile',
        profile: 'student-profile'
      },
      {
        to: '/calendar',
        icon: 'mdi-calendar',
        text: 'Calendar',
        profile: 'all'
      },
      {
        to: '/courses',
        icon: 'collections_bookmark',
        text:'Courses Offered',
        profile: 'instructor-profile'
      },
      {
        to: '/studentList',
        icon: 'mdi-account',
        text: 'Student Statistics',
        profile: 'instructor-profile'
      },
      {
        to: '/QuizList',
        icon: 'mdi-file-question',
        text: 'QuizList',
        profile: 'instructor-profile'
      },
      {
        to: '/quiz',
        icon: 'mdi-file-question',
        text: 'Quiz'
      },
      {
        to: '/feedback',
        icon: 'mdi-message-alert',
        text: 'Feedback'
      },
      {
        to: '/maps',
        icon: 'mdi-map-marker',
        text: 'Maps',
        profile: 'student-profile'
      },
      {
        to: '/notifications',
        icon: 'mdi-bell',
        text: 'Notifications',
        profile: 'student-profile'
      }
    ],
    responsive: false
  }),
  computed: {
    ...mapState('app', ['image', 'color']),
    ...mapGetters("profile", ["profileType", "profile", "user", "first_name"]),
    inputValue: {
      get () {
        return this.$store.state.app.drawer
      },
      set (val) {
        this.setDrawer(val)
      }
    },
    items () {
      return this.$t('Layout.View.items')
    },
    isStudent(){
      const x = this.$store.state.type;
    }
  },
  mounted () {
    console.log(this.profileType)
    this.onResponsiveInverted()
    window.addEventListener('resize', this.onResponsiveInverted)
  },
  beforeDestroy () {
    window.removeEventListener('resize', this.onResponsiveInverted)
  },
  methods: {
    ...mapMutations('app', ['setDrawer', 'toggleDrawer']),
    onResponsiveInverted () {
      if (window.innerWidth < 991) {
        this.responsive = true
      } else {
        this.responsive = false
      }
    }
  }
}
</script>

<style lang="scss">
  #app-drawer {
    .v-list__tile {
      border-radius: 4px;
      &--buy {
        margin-top: auto;
        margin-bottom: 17px;
      }
    }
    .v-image__image--contain {
      top: 9px;
      height: 60%;
    }
    .search-input {
      margin-bottom: 30px !important;
      padding-left: 15px;
      padding-right: 15px;
    }
  }
</style>