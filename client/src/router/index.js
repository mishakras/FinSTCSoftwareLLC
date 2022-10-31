import Vue from 'vue';
import VueRouter from 'vue-router';
import PingPong from '../components/Ping.vue';
import ToDos from '../components/ToDos.vue';

Vue.use(VueRouter);

export default new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/ping',
      name: 'PingPong',
      component: PingPong,
    },
    {
      path: '/to_dos',
      name: 'ToDos',
      component: ToDos,
    },
  ],
});
