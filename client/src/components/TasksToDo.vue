<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col-sm-10">
          <h1>Tasks</h1>
          <hr><br><br>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.addTask-modal>
        Add task
        </button>
        <br><br>
          <TaskCreationAlert :message="message" v-if="showMessage"></TaskCreationAlert>
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
              <tr v-for="(task, index) in Tasks" :key="index">
                <td>{{ task.description }}</td>
                <td>{{ task.done_at }}</td>
                <td>
                  <span v-if="task.done">Yes</span>
                  <span v-else>No</span>
                </td>
                <td>
                  <div class="btn-group" role="group">
                    <button type="button"
                      class="btn btn-warning btn-sm"
                      @click="editTask(task)"
                    >
                      <span v-if="task.done">Undo</span>
                      <span v-else>Do</span>
                    </button>
                    <button type="button"
                      class="btn btn-danger btn-sm"
                      @click="deleteTaskClick(task)"
                    >
                      Delete
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      <div>
      <b-modal ref="addTaskModal"
         id="addTask-modal"
         title="Add a new book"
         hide-footer>
          <b-form @submit="onSubmit" @reset="onReset" class="w-100">
          <b-form-group id="form-description-group"
                        label="Description:"
                        label-for="form-description-input">
              <b-form-input id="form-description-input"
                            type="text"
                            v-model="addTaskForm.description"
                            name='description'
                            required
                            placeholder="Enter task description">
              </b-form-input>
            </b-form-group>
            <b-form-group id="form-date_completed-group"
                          label="Author:"
                          label-for="form-date_completed-input">
                <b-form-input id="form-date_completed-input"
                              type="text"
                              v-model="addTaskForm.date_completed"
                              required
                              name='date_completed'
                              placeholder="Enter date, at which task should be completed">
                </b-form-input>
            </b-form-group>
            <b-button type="submit" variant="primary">Submit</b-button>
            <b-button type="reset" variant="danger">Reset</b-button>
          </b-form>
        </b-modal>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import TaskCreationAlert from './TaskCreationAlert.vue';

export default {
  name: 'TasksToDo',
  data() {
    return {
      Tasks: [],
      addTaskForm: {
        description: '',
        date_completed: '',
      },
      message: '',
      showMessage: false,
    };
  },
  components: {
    TaskCreationAlert,
  },
  computed: {
    TaskState(task) {
      if (task.done) return 'Undo';
      return 'Do';
    },
  },
  methods: {
    getTasks() {
      const path = 'http://localhost:5000/to_dos/';
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
      const path = 'http://localhost:5000/to_dos/';
      axios.post(path, payload)
        .then((res) => {
          this.getTasks();
          this.message = res.data.message;
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getTasks();
        });
    },
    updateTask(payload) {
      const path = 'http://localhost:5000/to_dos/';
      axios.put(path, payload)
        .then((res) => {
          this.message = res.data.message;
          this.showMessage = true;
          this.getTasks();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getTasks();
        });
    },
    deleteTask(payload) {
      const path = 'http://localhost:5000/to_dos/';
      axios.delete(path, { data: payload })
        .then((res) => {
          this.message = res.data.message;
          this.showMessage = true;
          this.getTasks();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getTasks();
        });
    },
    editTask(task) {
      let completed = 0;
      if (task.done) {
        completed = 0;
      } else {
        completed = 1;
      }
      const payload = {
        description: task.description,
        completed,
      };
      this.updateTask(payload);
    },
    deleteTaskClick(task) {
      const payload = {
        description: task.description,
      };
      this.deleteTask(payload);
    },
    initForm() {
      this.addTaskForm.description = '';
      this.addTaskForm.date_completed = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addTaskModal.hide();
      if (new Date(this.addTaskForm.date_completed) > new Date()) {
        const payload = {
          description: this.addTaskForm.description,
          date_completed: this.addTaskForm.date_completed,
        };
        this.addTasks(payload);
      } else {
        this.showMessage = true;
        this.message = 'Date must be later than today';
      }
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addToDosModal.hide();
      this.initForm();
    },
  },
  created() {
    // eslint-disable-next-line
    window.console.log("aaaa");
    this.getTasks();
  },
};
</script>
