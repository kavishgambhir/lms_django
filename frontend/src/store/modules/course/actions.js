import { httpClient } from '../../../plugins/httpClient'

export default{
    setCourses({commit})
    {
        
        httpClient.get('/api/course-offerings/').then(
            response=>{ commit('SET_COURSES', response.data)
            console.log(response.data)
            }
        )
    },
    setEnrolledCourses({commit,data})
    {
        commit('SET_ENROLLED_COURSES',data)
    }
}