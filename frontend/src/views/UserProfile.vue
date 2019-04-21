<template>
  <v-container fill-height fluid grid-list-xl>
    <v-layout justify-center wrap>
      <v-flex xs12 md8>
        <material-card color="green" title="Your Profile" text="Your profile">
          <v-form>
            <v-container py-0>
              <v-layout wrap>
                <v-flex xs12 md6>
                  <v-text-field
                    class="purple-input"
                    label="Username"
                    hint="This field cannot be modified"
                    :value="user.username"
                    readonly
                  />
                </v-flex>
                <v-flex xs12 md6>
                  <v-text-field
                    label="Email Address"
                    class="purple-input"
                    hint="This field cannot be modified"
                    :value="user.email"
                    readonly
                  />
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
                  <v-text-field
                    label="Roll Number"
                    class="purple-input"
                    :value="profile.roll_number"
                  />
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field class="purple-input" label="Department" :value="this.department" readonly hint="This field cannot be modified"/>
                </v-flex>
                <v-flex xs12>
                  <v-textarea
                    class="purple-input"
                    label="About Me"
                    :value="[profile.about==null ? 'Write Something about yourself!' :profile.about]"
                  />
                </v-flex>
                <v-flex xs12 text-xs-right>
                  <v-btn class="mx-0 font-weight-light" color="success" @click="updateProfile">Update Profile</v-btn>
                </v-flex>
              </v-layout>
            </v-container>
          </v-form>
        </material-card>
      </v-flex>
      <v-flex xs12 md4>
        <material-card class="v-card-profile">
          <v-avatar slot="offset" class="mx-auto d-block" size="130">
            <img :src="profile.avatar">
          </v-avatar>
          <v-card-text class="text-xs-center">
            <h6 class="category text-gray font-weight-thin mb-3">{{profileType}}</h6>
            <h4 class="card-title font-weight-light">{{user.first_name+' '+user.last_name}}</h4>
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
  data() {
    return {
      department: ""
    };
  },
  computed: {
    ...mapGetters("profile", ["profileType", "profile", "user", "first_name"])
  },
  mounted() {
    this.$httpClient
      .get('/'+this.profile.department.replace (/^[a-z]{4,5}\:\/{2}[a-z]{1,}\:[0-9]{1,4}.(.*)/, '$1'))
      .then(resp => {
        (this.department = resp.data.name), console.log(resp);
      })
      .catch(err => console.log(err));
  }
};
</script>
