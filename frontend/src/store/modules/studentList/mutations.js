export default {
    'SET_STUDENT_LIST'(state, data) {
        (data).forEach(element => {
            state.studentList.push(element)
        })
    }
}