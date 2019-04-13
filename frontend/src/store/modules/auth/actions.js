export default {
    login({commit,getters})
    {
        commit('SET_LOGGED_IN')
    },
    logout({commit,getters})
    {
        commit('SET_LOGGED_OUT')
    }
}