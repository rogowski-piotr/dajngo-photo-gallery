<template>
    <div>
        <table class="table text-center table-bordered table-striped">
            <thead>
            <tr>
                <th scope="col" style="width: 33%">Miniaturka</th>
                <th scope="col" style="width: 33%">Tytuł</th>
                <th scope="col" style="width: 33%">Podgląd</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="todo in todos" :key="todo.id">
                <td style="width: 33%">
                    <img style="width: 100%; height: 100%" v-bind:src="todo.image"/>
                </td>
                <td style="width: 33%">{{ todo.title }}</td>
                <td style="width: 33%">
                    <a class="btn btn-primary text-white mx-1" v-bind:href="'/zdjecie/' + todo.id"><i class="fa fa-picture-o"></i></a>
                </td>
            </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    name: 'TaskTable',
    props: {
        todos: Array,
    },
    methods: {
        makeImage(base64) {
            console.log(base64);
            var image = new Image();
            console.log(image);
            image.src = base64;
            return image;
        }
    }
}
</script>