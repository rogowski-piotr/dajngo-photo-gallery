<template>
  <div class="container-fluid" style="padding: 0">
    <Navbar/>
    <div class="row">
      <div class="col-8 mx-sm-auto p-4">

        <a href="/"><i class="fa fa-arrow-left" aria-hidden="true"></i> powrót do strony głównej</a>
        <hr/>
        <h3>Formularz dodawania zdjęć</h3>
        <hr/>

        <div v-if="addStatus == false" class="alert alert-warning text-center" role="alert" id="alert-invalid-data">
            <h4 class="alert-heading">Wypełnij wszystkie pola w formularzu oraz dodaj zdjęcie!</h4>
        </div>

        <div v-if="addStatus == true" class="alert alert-success text-center" role="alert" id="alert-valid-data">
            <h4 class="alert-heading">Poprawnie dodano zdjęcie!</h4>
        </div>

        <div class="col-lg-6 offset-lg-2">

            <table class="table table-hover text-left">
                <tr>
                    <td></td>
                    <th scope="row">Tytuł</th>
                    <td></td>
                    <td>
                        <input type="text" id="name" class="form-control" v-model="payload.title">
                    </td>
                </tr>
                <tr>
                    <td></td>
                    <th scope="row">Opis zdjęcia</th>
                    <td></td>
                    <td>
                        <textarea class="form-control" v-model="payload.description"></textarea>
                    </td>
                </tr>
                <tr>
                    <td></td>
                    <th scope="row">Załaduj zdjęcie</th>
                    <td></td>
                    <td>
                        <input type="file" @change="previewImage" accept="image/*">
                        <div class="image-preview pt-3" v-if="payload.image?.length > 0">
                          <img style="width: 100%; height: 100%" class="preview" :src="payload.image">
                        </div>
                    </td>
                </tr>
            </table>

            <br/>
            <div class="text-center">
                <button @click="add" type="button" class="btn btn-primary">Dodaj zdjęcie</button>
            </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { taskService } from '../services';
import Navbar from '../components/Navbar';

export default {
  name: 'AddTaks',
  components: { Navbar },
  data () {
        return {
            addStatus: null,
            payload: {
                title: null,
                description: null,
                user: JSON.parse(localStorage.getItem('user')).id,
                image: null
            },
        }
    },
  methods: {
    previewImage: function(event) {
    var input = event.target;
    if (input.files && input.files[0]) {
      var reader = new FileReader();
      reader.onload = (e) => {
        this.payload.image = e.target.result;
      }
      reader.readAsDataURL(input.files[0]);
    }
    },
    add() {
      if (! this.validatePayload()) {
        this.addStatus = false;
        return;
      }
      taskService.addTask(this.payload)
        .then(response => {
          console.log(response);
          this.addStatus = response.status == 201 ? true : false;
      }).catch(() => this.addStatus = false);
    },
    validatePayload() {
      return (this.payload.title != null && this.payload.title.length > 0)
        && (this.payload.description != null && this.payload.description != '')
        && (this.payload.image != null && this.payload.image?.length > 0)
    },
  }
}
</script>