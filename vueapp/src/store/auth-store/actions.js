import axios from 'axios'
import router from '../../router/index'

export const actions = {
    loginAndSaveToken(formData) {
        // this is just an example on how to save the JWT Token, PS AUTH API is fake
        axios.post('https://fake-url.com/api/auth', formData).then((response) => {
            localStorage.setItem('auth_token', response.datatoken);
            router.push('/profile');
        }).catch((error) => {
            //will always redirect to profile 
            router.push('/profile');
        });
    },
};