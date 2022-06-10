<template>
    <div>
        <table class="table text-center table-bordered table-striped">
            <thead class="thead" style="background-color: slategray">
            <tr>
                <th scope="col" style="width: 33%">Nazwa</th>
                <th scope="col" style="width: 33%">Rola</th>
                <th scope="col" style="width: 33%">Usuń</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="user in users" :key="user.id">
                <td style="width: 33%">{{ user.username }}</td>
                <td style="width: 33%">
                    <div v-if="user.is_admin" style="font-size: 20px">Administrator</div>
                    <div v-else style="font-size: 20px">Użytkownik</div>
                </td>
                <td style="width: 33%">
                    <button v-if="user.is_admin" class="btn btn-danger text-white disabled" disabled>usuń</button>
                    <button v-else class="btn btn-danger text-white" @click="deleteOne(user.id)">usuń</button>
                </td>
            </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import { userService } from '../services';

export default {
    name: 'UserTable',
    data () {
        return { users: [] }
    },
    mounted () {
        userService.fetchUsers()
            .then(response => this.users = response);
    },
    methods: {
        deleteOne(id) {
            userService.deleteOne(id)
            this.$router.go(0);
        }
    }
}
</script>