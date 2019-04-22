// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import axios from 'axios'
import VueAxios from 'vue-axios'
import router from './router'
import ECharts from 'vue-echarts'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

import 'echarts/lib/chart/bar'
import 'echarts/lib/component/tooltip'

Vue.use(ElementUI)
Vue.use(VueAxios, axios)
Vue.component('charts', ECharts)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
