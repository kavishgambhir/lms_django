export default {
    'SET_COURSES'(state, data) {
        // Vue.set(state, 'courses', [...data]);
        (data).forEach(element => {
            console.log("ho rha",element)
            state.courses.push(element)
        })

    }
}