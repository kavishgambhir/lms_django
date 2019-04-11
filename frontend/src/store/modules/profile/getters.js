export default {
    profileType: state => state.type,
    profile: state => state.profile,
    user: state => state.profile.user,
    errors: state => state.errors
}