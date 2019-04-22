<template>
  <v-container
    fluid
    grid-list-xl
    fill-height>
    <v-layout
      justify-center
      align-center
    >
      <v-flex xs12>
        <material-card
          color="green">
          <div
            slot="header"
          >
            <div class="title font-weight-light mb-2">Notifications</div>
            <div class="category">
              Smart ClassRoom
              <v-icon
                size="17"
              >
                mdi-heart
              </v-icon>
            </div>
          </div>

          <v-card-text>
            <v-layout
              row
              wrap>
              <v-flex
                md6
                sm12>
                <h2 class="title font-weight-light mb-3">Notifications</h2>

                <material-notification
                  class="mb-3"
                  color="info"
                >
                  CS321 Quiz to be held on Monday 31st August
                </material-notification>
                <material-notification
                  class="mb-3"
                  color="info"
                  dismissible
                >
                  CS221 Quiz to be held on Monday 25th August
                </material-notification>
                <material-notification
                  class="mb-3"
                  color="info"
                  dismissible
                  icon="mdi-bell-plus"
                >

                  Janmashtami Holiday on 26th.
                </material-notification>
                <material-notification
                  class="mb-3"
                  color="info"
                  dismissible
                  icon="mdi-bell-plus"
                >

                  MahaShivratri Holiday on 5th
                </material-notification>
              </v-flex>

              <v-flex
                md6
                sm12>
                <h2 class="title font-weight-light">Notifcation States</h2>


                <material-notification
                  class="mb-3"
                  color="warning"
                  dismissible
                >
                  <strong>WARNING</strong> - You have low attendance in Course CS321`
                </material-notification>

                <material-notification
                  class="mb-3"
                  color="error"
                  dismissible
                >
                  <strong>DANGER</strong> - Last Quiz Performance was below the class average`
                </material-notification>
              </v-flex>
            </v-layout>
            

            <v-snackbar
              :color="color"
              :bottom="bottom"
              :top="top"
              :left="left"
              :right="right"
              v-model="snackbar"
              dark
            >
              <v-icon
                color="white"
                class="mr-3"
              >
                mdi-bell-plus
              </v-icon>
              <div>Welcome to <b>ClassRoom Dashboard</b> - a beautiful dashboard for every Student.</div>
              <v-icon
                size="16"
                @click="snackbar = false"
              >
                mdi-close-circle
              </v-icon>
            </v-snackbar>
          </v-card-text>
        </material-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    color: null,
    colors: [
      'purple',
      'info',
      'success',
      'warning',
      'error'
    ],
    top: true,
    bottom: false,
    left: false,
    right: false,
    snackbar: false
  }),

  methods: {
    snack (...args) {
      this.top = false
      this.bottom = false
      this.left = false
      this.right = false

      for (const loc of args) {
        this[loc] = true
      }

      this.color = this.colors[Math.floor(Math.random() * this.colors.length)]

      this.snackbar = true
    }
  }
}
</script>
