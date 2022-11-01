import Vue from 'vue';
import VueRouter from 'vue-router';
import PingPong from '../components/Ping.vue';
import TasksToDo from '../components/TasksToDo.vue';

Vue.use(VueRouter);

export default new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'TasksToDo',
      component: TasksToDo,
    },
  ],
});
