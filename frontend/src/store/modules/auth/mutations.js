export default {
    'SET_LOGGED_IN'(state) {
        state.isLoggedIn = true
    },
    'SET_LOGGED_OUT'(state) {
        state.isLoggedIn = false
    }
}