import Vue from 'vue'
import Vuex from 'vuex'
import getters from './getters'
const path = require('path')

Vue.use(Vuex)

const files = require.context('./modules', false, /\.js$/)
let modules = {}
files.keys().forEach(key => {
  let name = path.basename(key, '.js')
  modules[name] = files(key).default || files(key)
})
const store = new Vuex.Store({
  modules,
  getters,
<<<<<<< HEAD
  state: {
    HOST: `http://127.0.0.1:8000`,
    Authorization: localStorage.getItem('token')
      ? localStorage.getItem('token')
      : ''
  }
})
export const CHANGE_LOGIN = (state, user) => {
  state.token = user.token
  localStorage.setItem('token', user.token)
}
=======
    state: {
          HOST: `http://127.0.0.1:8000`,
          Authorization: localStorage.getItem('token') ? localStorage.getItem('token') : ''
      },
})

// export const CHANGE_LOGIN = (state, user) => {
//         state.token = user.token;
//         localStorage.setItem('token', user.token);
//       };
>>>>>>> 5e7e2f6b2b6f8da4ec10867c6507767e251816d7
export default store
