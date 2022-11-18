<template>
  <div class="login">
    <div class="loginBox">
      <h2 class="loginH2"><strong>Register your</strong> Fightdiabetes</h2>
      <div class="loginCon">
        <div class="titleDiv">
          <p>initialize your username and password:</p>
        </div>
        <el-form ref="loginForm" :rules="rules" :model="ruleForm">
          <el-form-item prop="user">
            <el-input placeholder="请输入账号" prefix-icon="el-icon-user" v-model="username"></el-input>
          </el-form-item>
          <el-form-item prop="password">
            <el-input placeholder="请输入密码" prefix-icon="el-icon-lock" v-model="password" show-password>
            </el-input>
          </el-form-item>
          <el-form-item prop="password">
            <el-input placeholder="请再次输入密码" prefix-icon="el-icon-lock" v-model="password_confirm" show-password>
            </el-input>
          </el-form-item>
          <el-button type="primary" class="loginBtn" @click="send_data()">注册</el-button>
          <el-button type="primary" class="loginBtn" @click="back_login()">返回登录页面</el-button>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      // ruleForm: {
      //   username: '',
      //   password: '',
      //   password_confirm: ''
      // }
      username: '',
      password: '',
      password_confirm: ''
    }
  },
  mounted () {
    // if (location.href.indexOf('#reloaded') === -1) {
    //   location.href = location.href + '#reloaded'
    //   location.reload()
    // }
  },
  methods: {
    back_login () {
      window.location.href = '/#/login'
    },
    send_data: function () {
      var dataobj = {
        'username': this.username,
        'password': this.password,
        'email': 'test.mail.com'
      }
      const path = 'http://127.0.0.1:8000/register/'
      var config = {
        method: 'POST',
        url: path,
        headers: {
          'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
          'Content-Type': 'application/json'
        },
        data: dataobj
      }
      window.alert(dataobj['username'])
      // arrived here
      axios(config)
        .then(function (response) {
          console.log(JSON.stringify(response.data))
        })
        .catch(function (error) {
          console.log(error)
        })
      // axios({
      //   method: 'post',
      //   url: 'http://localhost:8080/register/',
      //   headers: {
      //     'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
      //     'Content-Type': 'application/json'
      //   },
      //   data: dataobj
      // })
      //   .then(function (response) {
      //     console.log(JSON.stringify(response.data))
      //   })
      //   .catch(function (error) {
      //     console.log(error)
      //   })
      // }
    }
  }
}
// var data = {
//   'username': this.username,
//   'password': this.password,
//   'email': 'test.mail.com'
// }
// var config = {
//   methods: 'post',
//   url: 'http://127.0.0.1:8000/register',
//   headers: {
//     'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
//     'Content-Type': 'application/json'
//   },
//   data: data
// }
</script>

<style>

</style>
