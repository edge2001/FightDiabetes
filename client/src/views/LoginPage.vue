<template>
  <div class="login">
    <div class="loginBox">
      <h2 class="loginH2"><strong>Login your</strong> Fightdiabetes</h2>
      <div class="loginCon">
        <div class="titleDiv">
          <h3 @click="jump_to_Register">Sign up now</h3>
          <p>Enter your username and password to log on:</p>
          <!-- <p><i class="el-icon-user"></i></p>
          <i class="el-icon-key"></i> -->
        </div>
        <el-form ref="loginForm" :rules="rules" :model="ruleForm">
          <el-form-item prop="user">
            <el-input placeholder="请输入账号" prefix-icon="el-icon-user" v-model="ruleForm.username"></el-input>
          </el-form-item>
          <el-form-item prop="password">
            <el-input placeholder="请输入密码" prefix-icon="el-icon-lock" v-model="ruleForm.password" show-password>
            </el-input>
          </el-form-item>
          <el-button type="primary" class="loginBtn" @click="send_data()">登录</el-button>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script>
// import SlideVerify from '@/components/SlideVerify'
import axios from 'axios'
export default {
  data () {
    return {
      ruleForm: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    jump_to_Register: function () {
      window.location.href = '/#/register'
    },
    send_data: function () {
      // window.alert('sss')
    }
  }
}
var data = {
  username: this.username,
  password: this.password
}
var config = {
  method: 'post',
  url: 'http://127.0.0.1/login',
  headers: {
    'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
    'Content-Type': 'application/json'
  },
  data: data
}

axios(config)
  .then(function (response) {
    console.log(JSON.stringify(response.data))
  })
  .catch(function (error) {
    console.log(error)
  })
</script>

<style>

</style>
