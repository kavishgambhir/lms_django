export default {
    'SET_COURSES'(state, data) {
        (data).forEach(element => {
            state.courses.push(element)
        })

    }
}