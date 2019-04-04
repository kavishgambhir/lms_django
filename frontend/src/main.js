import Vue from 'vue'
import Vuetify from 'vuetify'
import './plugins/vuetify'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import 'vuetify/dist/vuetify.min.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import 'dayspan-vuetify/dist/lib/dayspan-vuetify.min.css'
import DaySpanVuetify from 'dayspan-vuetify'
import App from './App.vue'
import router from './router'
import store from './store'
import httpClientPlugin from './plugins/httpClient'

Vue.config.productionTip = false


Vue.use(httpClientPlugin)

Vue.use(DaySpanVuetify, {
  methods: {
    getDefaultEventColor: () => '#1976d2'
  }
});

Vue.use(Vuetify);


new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
