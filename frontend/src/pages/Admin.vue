<template>
  <div class="container-fluid" style="padding: 0">
    <Navbar/>
    <div class="row">
      <div class="col-8 mx-sm-auto p-4">
        <h2 class="mb-3">Panel administratora</h2>
        <h5 class="mb-3">Użytkownicy systemu</h5>
        <hr>
        <UserTable/>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from '../components/Navbar';
import UserTable from '../components/UserTable';

export default {
  components: { Navbar, UserTable },
  name: 'Admin',
}
</script>