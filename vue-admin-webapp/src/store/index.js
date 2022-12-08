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
export default store
