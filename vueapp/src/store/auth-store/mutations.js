export const mutations = {
    setIsSignInPanelActive(state, newVal) {
        state.isSignInPanelActive = newVal;
    },
    setCurrentSignUpStep(state, newVal) {
        state.currentSignUpStep = newVal;
    },
    setFormData(state, newVal) {
        state.formData = {...state.formData, ...newVal };
    },

};