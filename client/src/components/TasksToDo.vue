<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col-sm-10">
          <h1>Tasks</h1>
          <hr><br><br>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.Task-modal>Add task</button>
          <br><br>
          <table class="table table-hover">
            <thead>
              <tr>
                <th scope="col">Description</th>
                <th scope="col">To be done at</th>
                <th scope="col">Completed</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(todo, index) in ToDos" :key="index">
                <td>{{ todo.description }}</td>
                <td>{{ todo.done_at }}</td>
                <td>
                  <span v-if="todo.done">Yes</span>
                  <span v-else>No</span>
                </td>
                <td>
                  <div class="btn-group" role="group">
                    <button type="button" class="btn btn-warning btn-sm">Update</button>
                    <button type="button" class="btn btn-danger btn-sm">Delete</button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
        <b-modal ref="addTaskModal"
             id="Task-modal"
             title="Add a new task"
             hide-footer>
        <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-description-group"
                      label="Description:"
                      label-for="form-title-input">
            <b-form-input id="form-description-input"
                          type="text"
                          v-model="addToDosForm.description"
                          required
                          placeholder="Enter description">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-date-completed-group"
                        label="To complete at:"
                        label-for="form-date-completed-input">
              <b-form-input id="form-date-completed-input"
                            type="text"
                            v-model="addToDosForm.date_completed"
                            required
                            placeholder="Enter date at which task should be completed">
              </b-form-input>
            </b-form-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-form>
      </b-modal>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'TasksToDo',
  data() {
    return {
      Tasks: [],
      addTaskForm: {
        description: '',
        date_completed: '',
      },
    };
  },
  methods: {
    getTasks() {
      const path = 'http://localhost:5000/to_dos';
      axios.get(path)
        .then((res) => {
          this.Tasks = res.data.Tasks;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addTasks(payload) {
      const path = 'http://localhost:5000/to_dos';
      axios.post(path, payload)
        .then(() => {
          this.getTasks();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getTasks();
        });
    },
    initForm() {
      this.addTaskForm.description = '';
      this.addTaskForm.date_completed = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addTaskModal.hide();
      // const today = new Date();
      // const date = `${today.getFullYear()}-${(today.getMonth() + 1)}-${today.getDate()}`;
      // if (this.addToDosForm.date_completed < date) {
      const payload = {
        description: this.addToDosForm.description,
        author: this.addToDosForm.date_completed,
      };
      this.addToDos(payload);
      this.initForm();
      // } else {
      //  this.flashMessage.show({ status: 'error', title: '',
      // message: 'Oh, you broke my heart! Shame on you!' });
      // }
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addToDosModal.hide();
      this.initForm();
    },
  },
  created() {
    this.getToDos();
  },
};
</script>
