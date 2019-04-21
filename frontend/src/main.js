// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import 'vuetify/dist/vuetify.min.css'
// Components
import './components'

// Plugins
import './plugins'
import httpClientPlugin from './plugins/httpClient'
// Sync router with store
import { sync } from 'vuex-router-sync'

// Application imports
import App from './App'
import i18n from '@/i18n'
import router from '@/router'
import store from '@/store'
import Vuetify from 'vuetify/lib'
import Axios from 'axios';

Vue.use(httpClientPlugin)
// var auth_check : ""

const x = localStorage.getItem('profile')
if (x) {
  Axios.create()
    .get("/api/auth-check/")
    .then(resp => {if(resp.status==200)
      { 
        console.log(resp)
        store.dispatch('profile/setProfile', JSON.parse(x))
        store.dispatch('auth/login', true)
        router.push('Dashboard')
      }
    })
    .catch(err => 
      {
        store.dispatch('auth/logout')
      });

}

// Sync store with router
sync(store, router)

// Vue.config.productionTip = false



// Vue.use(DaySpanVuetify, {
//   methods: {
//     getDefaultEventColor: () => '#1976d2'
//   }
// })
Vue.use(Vuetify)
/* eslint-disable no-new */
new Vue({
  i18n,
  router,
  store,
  render: h => h(App)
}).$mount('#app')
