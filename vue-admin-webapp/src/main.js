import Vue from 'vue'
import App from './App.vue'
import router from '@/router'
import store from './store'
import '@/style/index.scss' // glob scss
import './plugins/element.js'
import animated from 'animate.css'
import '@/assets/iconfont/iconfont.css'
import 'element-ui/lib/theme-chalk/index.css'
import ElementUI from 'element-ui'
import Buefy from "buefy";
import 'buefy/dist/buefy.css'
// import global from '@/global/global.js'

Vue.use(ElementUI)
// Vue.prototype.global = global
Vue.use(Buefy)
Vue.use(animated)
// import SlideVerify from 'vue-monoplasty-slide-verify'

// Vue.use(SlideVerify)
Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

router.beforeEach((to, from, next) => {
  if (to.path === '/login' || to.path === '/') {
    //若是进入登录与注册页面 ==> pass
    next()
  } else {
    let userToken = localStorage.getItem('token')
    console.log('Token为:' + userToken)
    if (userToken == null || userToken == '') {
      alert('无权限，请先登录!')
      return next('/login')
    } else {
      next()
    }
  }
})
