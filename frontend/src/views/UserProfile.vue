<template>
  <v-container fill-height fluid grid-list-xl>
    <v-layout justify-center wrap>
      <v-flex xs12 md8>
        <material-card color="green" title="Your Profile" text="Complete your profile">
          <v-form>
            <v-container py-0>
              <v-layout wrap>
                <v-flex xs12 md6>
                  <v-text-field class="purple-input" label="username" :value="user.username"/>
                </v-flex>
                <v-flex xs12 md6>
                  <v-text-field label="Email Address" class="purple-input" :value="user.email"/>
                </v-flex>
                <v-flex xs12 md6>
                  <v-text-field label="First Name" class="purple-input" :value="user.first_name"/>
                </v-flex>
                <v-flex xs12 md6>
                  <v-text-field label="Last Name" class="purple-input" :value="user.last_name"/>
                </v-flex>
                <v-flex xs12 md12>
                  <v-text-field label="Date of Birth" class="purple-input" :value="profile.dob"/>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field label="City" class="purple-input"/>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field label="Country" class="purple-input"/>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field class="purple-input" label="Postal Code" type="number"/>
                </v-flex>
                <v-flex xs12>
                  <v-textarea
                    class="purple-input"
                    label="About Me"
                    :value='[ profile.about==null ? "Write Something about yourself!"  : profile.about]'
                  />
                </v-flex>
                <v-flex xs12 text-xs-right>
                  <v-btn class="mx-0 font-weight-light" color="success">Update Profile</v-btn>
                </v-flex>
              </v-layout>
            </v-container>
          </v-form>
        </material-card>
      </v-flex>
      <v-flex xs12 md4>
        <material-card class="v-card-profile">
          <v-avatar slot="offset" class="mx-auto d-block" size="130">
            <img src="https://demos.creative-tim.com/vue-material-dashboard/img/marc.aba54d65.jpg">
          </v-avatar>
          <v-card-text class="text-xs-center">
            <h6 class="category text-gray font-weight-thin mb-3">{{profileType}}</h6>
            <h4 class="card-title font-weight-light">{{user.first_name+' '+user.last_name}}</h4>
            <p
              class="card-description font-weight-light"
            >Saksham Gupta</p>
            <v-btn color="success" round class="font-weight-light">Follow</v-btn>
          </v-card-text>
        </material-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  computed: {
    ...mapGetters("profile", ["profileType", "profile", "user", "first_name"])
  },
  mounted()
  {
    console.log(this.profileType)
  }
}
</script>
