<template>
  <div class="container-fluid" style="padding: 0">
    <Navbar/>
    <div class="row">
      <div class="col-8 mx-sm-auto p-4">
        <a href="/"><i class="fa fa-chevron-left" aria-hidden="true"></i> powrót</a>
        <hr/>
        <h3>Podgląd zdjęcia: <i>{{ this.task.title }}</i></h3>
        <p v-if="resolution.height != null"><b>Rozdzielczość: </b>{{ this.resolution.width }}x{{ this.resolution.height }}</p>
        <hr/>
        <img id="img-preview" style="width: 100%;" src=""/>
        <div v-if="task.id === null" class="col-md-12 text-center">
          <br>
          <h3>brak danych 😥</h3>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { taskService } from '../services';
import Navbar from '../components/Navbar';

export default {
  name: 'ShowTask',
  components: { Navbar },
  data () {
      return {
          noDataLabel: '',
          taskId: null,
          task: {
            id: null,
            title: null,
            description: null,
            user: null,
            image: null
          },
          resolution: {
            width: null,
            height: null,
          }
      }
  },
  created () {
      this.taskId = this.$route.params.id;
      taskService.fetchTask(this.taskId)
        .then(response => {
          this.task = response;
          var image = document.getElementById("img-preview");
          var self = this; 
          image.onload = function() {
            self.resolution.width = this.naturalWidth;
            self.resolution.height = this.naturalHeight;
          };
          image.src = this.task.image;
        })
  },
  methods: {
  }
}
</script>