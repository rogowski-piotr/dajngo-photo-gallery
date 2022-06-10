<template>

<div>
    <div class="row">
        <div class="col-6 mt-3 mx-auto border border-danger rounded alert alert-warning" v-show="errorMessage != null" role="alert" id="alert-incorrect-data">
            <h4 class="alert-heading">Nie udało się zarejestrować!</h4>
            <hr>
            {{ errorMessage }}
        </div>
    </div>

    <section class="vh-50 gradient-custom">
    <div class="container py-5 h-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-12 col-md-8 col-lg-6 col-xl-5">
            <div class="card bg-primary text-white" style="border-radius: 1rem;">
            <div class="card-body p-5 text-center">

                <div class="mb-md-5 mt-md-4 pb-5">

                <h2 class="fw-bold mb-2">Formularz rejestracji</h2>
                <p class="text-white-50-bold mb-5">Wprowadź wszystkie poniższe pola</p>

                <div class="form-outline form-white mb-4">
                    <input type="text" id="typeEmailX" class="form-control form-control-lg" placeholder="Nazwa użytkownika" v-model="payload.username"/>
                </div>

                <div class="form-outline form-white mb-4">
                    <input type="password" id="typePasswordX" class="form-control form-control-lg" placeholder="Hasło" v-model="payload.password"/>
                </div>

                <div class="form-outline form-white mb-4">
                    <input type="password" id="typeRepeatedPasswordX" class="form-control form-control-lg" placeholder="Powtórz hasło" v-model="repeatedPassword"/>
                </div>

                <button class="btn btn-outline-light btn-lg px-5" type="submit" @click="tryRegister">Zarejestruj</button>

                </div>

                <div>
                <p class="mb-0">Jeśli masz już konto <b><a href="/login" class="text-black-50 fw-bold">zaloguj się</a></b>
                </p>
                </div>

            </div>
            </div>
        </div>
        </div>
    </div>
    </section>

</div>
</template>

<script>
import router from '../helpers/router';
import { userService } from '../services';
// import Login from '../pages/Login.vue';

export default {
  name: 'Login',
  data() {
    return {
        name: null,
        password: null,
        errorMessage: null,
        payload: {
            username: null,
            password: null,
        },
        repeatedPassword: null,
    }
  },
  created () {
        userService.logout()
    },
  methods: {
    tryRegister() {
        console.log('trying to register');
        if (this.validateRepeatedPassword()) {
            console.log('pass corected');
            userService.register(this.payload)
                .then(response => {
                    console.log(response);
                    if (response.status === 201) {
                        router.push({path: "/login?createdUser=true"});
                        window.location.href = '/login?createdUser=true';
                    } else {
                        this.errorMessage = ' ';
                    }
                })
                .catch(() => this.errorMessage = ' ')
        }
    },
    validateRepeatedPassword() {
        if (this.payload.username
            && this.payload.password
            && this.repeatedPassword
            && this.payload.password === this.repeatedPassword) {
            return true;
        }
        this.errorMessage = 'Wszystkie pola muszą być wypełnione a hasła identyczne';
        return false;
    }
  }
}
</script>