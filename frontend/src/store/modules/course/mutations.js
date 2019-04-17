export default {
    'SET_COURSES'(state, data) {
        state.courses = [];
        (data).forEach(element => {
            state.courses.push(element)
        })

    }
}