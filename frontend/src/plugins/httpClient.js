import axios from 'axios'

const httpClient = axios.create({
  xsrfCookieName: 'csrftoken',
  xsrfHeaderName: 'X-CSRFToken'
})

export { httpClient }

export default {
  install (Vue, options) {
    Vue.prototype.$httpClient = httpClient
  }
}
