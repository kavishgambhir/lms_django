import { httpClient } from '../../../plugins/httpClient'

export default {
    setQuizes({ commit }) {
        httpClient.get('/api/quizes/').then(response => {
            commit('SET_QUIZES', response.data)
            console.log(response.data)
        }
        ).catch(err => {
            commit('ADD_ERROR', err)
        })
    }
}