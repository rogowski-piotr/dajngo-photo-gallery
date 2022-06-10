<template>
    <nav class="navbar navbar-light sticky-top bg-primary flex-md-nowrap p-3 shadow">
        <a style="color: white" class="navbar-brand col-sm-3 col-md-2 mr-0 ml-5" href="#"><i class="fa fa-camera-retro" aria-hidden="true"></i> <b>Galeria zdjęć</b></a>
        <a class="navbar-text">
            <router-link to="/login" style="color: white" class="nav-link mr-5"><b><i class="fa fa-sign-out" aria-hidden="true"></i> <u>Wyloguj</u></b></router-link>
        </a>
    </nav>
</template>

<script>
export default {
    name: 'Navbar',
    data () {
        return {
            user: {}
        }
    },
    created () {
      this.user = JSON.parse(localStorage.getItem('user'));
    }
}
</script>