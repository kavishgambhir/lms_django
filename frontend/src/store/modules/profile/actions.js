import { httpClient } from '../../../plugins/httpClient'

export default {
    setProfile({ commit, getters }, payload) {
        httpClient.get('/api/sign-in/').then(response => {
            commit('SET_PROFILE_TYPE', response.data.data.type)
            commit('SET_PROFILE', response.data.data.profile)
        }
        ).catch(err => {
            commit('ADD_ERROR', err)
        })
    }
}