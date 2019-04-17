export default {
    profileType: state => state.type,
    profile: state => state.profile,
    user: state => state.profile.user,
    errors: state => state.errors,
    first_name: state => state.profile.user.first_name,
    isInstructor: state => state.type == 'instructor-profile'
}