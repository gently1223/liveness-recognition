export const getters = {
    getIsSignInPanelActive: (state) => {
        return state.isSignInPanelActive;
    },
    getCurrentSignUpStep: (state) => {
        return state.currentSignUpStep;
    },
    getFormData: (state) => {
        return state.formData;
    },

};