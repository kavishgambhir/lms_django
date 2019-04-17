import { httpClient } from '../../../plugins/httpClient'

export default {
    setStudentList({ commit }) {

        httpClient.get('/api/student-profiles/').then(
            response => {
                commit('SET_STUDENT_LIST', response.data)
                console.log(response.data)
            }
        )
    }
}