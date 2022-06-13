<template>
  <div class="container-fluid" style="padding: 0">
    <Navbar/>
    <div class="row">
      <div class="col-8 mx-sm-auto p-4">

        <div v-if="addStatus" class="alert alert-success text-center" role="alert" id="alert-valid-data">
            <h4 class="alert-heading">Poprawnie dodano zdjęcie!</h4>
        </div>

        <div class="col-md-12 text-center">
            <a class="btn btn-success text-black mb-4 p-3 my-2" v-bind:href="'/dodaj'">Dodaj nowe zdjęcie</a>
        </div>

        <TaskTable v-if="this.todos.length > 0" v-bind:todos="todos"/>
        <div v-else class="col-md-12 text-center">
          <hr>
          <h2>Nie posiadasz żadnych zdjęć 😥</h2>
          <br>
          <h5>Wciśnij przycisk powyżej, aby dodać pierwsze zdjęcie!</h5>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { taskService } from '../services';
import TaskTable from '../components/TaskTable';
import Navbar from '../components/Navbar';

export default {
  components: { TaskTable, Navbar },
  name: 'Dashboard',
  data () {
    return { 
      todos: [],
      addStatus: false,
    }
  },
  created() {
    this.addStatus = this.$route.query.addStatus;
    taskService.fetchTasks()
      .then(response => {
        console.log(response);
        this.todos = response;
      })
  },
}
</script>
