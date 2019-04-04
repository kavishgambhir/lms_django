import Vue from 'vue'
import './plugins/vuetify'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import App from './App.vue'
import router from './router'
import store from './store'
import httpClientPlugin from './plugins/httpClient'

Vue.config.productionTip = false

Vue.use(httpClientPlugin)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
