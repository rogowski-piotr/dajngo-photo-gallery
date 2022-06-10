<template>
<div>
    <div class="row">
        <div class="col-6 mt-3 mx-auto border border-dark rounded alert alert-success" v-if="createdUser" role="alert" id="alert-incorrect-data">
            <h4 class="alert-heading">Dodano użytkownika</h4>
        </div>

        <div class="col-6 mt-3 mx-auto border border-dark rounded alert alert-warning" v-show="errorMessage != null" role="alert" id="alert-incorrect-data">
            <h4 class="alert-heading">Niepoprawne dane logowania!</h4>
        </div>
    </div>

    <section class="vh-50 gradient-custom">
    <div class="container py-5 h-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-12 col-md-8 col-lg-6 col-xl-5">
            <div class="card bg-primary text-white" style="border-radius: 1rem;">
            <div class="card-body p-5 text-center">

                <div class="mb-md-5 mt-md-4 pb-5">

                <h2 class="fw-bold mb-2">Formularz logowania</h2>
                <p class="text-white-50-bold mb-5">Wprowadź nazwę użytkownika oraz hasło</p>

                <div class="form-outline form-white mb-4">
                    <input type="text" id="typeEmailX" class="form-control form-control-lg" placeholder="Nazwa użytkownika" v-model="name"/>
                </div>

                <div class="form-outline form-white mb-4">
                    <input type="password" id="typePasswordX" class="form-control form-control-lg" placeholder="Hasło" v-model="password"/>
                </div>

                <button class="btn btn-outline-light btn-lg px-5" type="submit" @click="validateAuth">Zaloguj</button>

                </div>

                <div>
                <p class="mb-0">Jeśli nie masz konta <b><a href="/rejestracja" class="text-black-50 fw-bold">zarejestruj się</a></b>
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

export default {
    name: 'Login',
    data() {
        return {
            name: null,
            password: null,
            errorMessage: null,
            createdUser: false,
        }
    },
    created () {
        userService.logout()
        this.createdUser = this.$route.query.createdUser;
    },
    methods: {
        validateAuth() {
            userService.login(this.name, this.password)
                .then(() => console.log('redirecting'))
                .then(router.push({path: "/"}))
                .then(() => window.location.href = '/')
                .catch(() => {
                    this.errorMessage = ' ';
                    this.createdUser = false;
                });
        },
    }
}
</script>