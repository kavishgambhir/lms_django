export default {
    'SET_COURSES'(state, data) {
        // Vue.set(state, 'courses', [...data]);
        state.courses = [];
        (data).forEach(element => {
            state.courses.push(element)
        })

    }
}