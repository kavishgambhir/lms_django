export default {
    'SET_COURSES'(state, data) {
        state.courses = [],
        (data).forEach(element => {
            state.courses.push(element)
        })

    },
    'SET_ENROLLED_COURSES'(state,data)
    {
        console.log("gh",data)
        state.current_enrolled_courses=[]
        state.current_enrolled_courses=data
    }
}