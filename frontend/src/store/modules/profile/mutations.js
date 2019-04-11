export default {
    'SET_PROFILE_TYPE'(state, type) {
        state.type = type
    },
    'SET_PROFILE'(state, profile) {
        state.profile = profile
    },
    'ADD_ERROR'(state, error) {
        state.errors.push(error)
    },
    'RESET_ERRORS'(state) {
        state.errors = []
    },
    'SET_FIRST_NAME'(state, firstName) {
        state.profile.user.first_name = firstName
    },
    'SET_LAST_NAME'(state, lastName) {
        state.profile.user.last_name = lastName
    },
    'SET_DEPARTMENT'(state, department) {
        state.profile.department = department
    },
    'SET_DOB'(state, dob) {
        state.profile.dob = dob
    },
    'SET_EMAIL'(state, email) {
        state.profile.user.email = email
    }
}