import Vue from 'vue'
import Router from 'vue-router'
import Experiments from '../components/Experiments'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Experiments',
      component: Experiments
    }
  ]
})
