<template>
  <div class="login">
    <div class="loginBox">
      <h1 class="loginH2"><strong>Login your</strong> Fightdiabetes</h1>
      <div class="loginCon">
        <div class="titleDiv">
          <!-- <button class="signup_button" @click="jump_to_Register">Sign up now</button> -->
          <p>Enter your username and password to log on:</p>
        </div>
        <el-form ref="loginForm" :rules="rules" :model="ruleForm" class="btn_out">
          <el-form-item prop="user">
            <el-col :span="7" class="intro_text">username</el-col>
            <el-col :span="8" class="input_text">
              <el-input placeholder="请输入账号" prefix-icon="el-icon-user" v-model="ruleForm.username">
              </el-input>
            </el-col>
          </el-form-item>
          <el-form-item prop="password" class="fill_in">
            <el-col :span="7" class="intro_text">password</el-col>
            <el-col :span="8" class="input_text">
              <el-input placeholder="请输入密码" prefix-icon="el-icon-lock" v-model="ruleForm.password" show-password>
              </el-input>
            </el-col>
          </el-form-item>
        </el-form>
        <div class="btn_in">
          <button class="btn-1" @click="send_data()">登录</button>
          <button class="signup_button" @click="jump_to_Register">Sign up now</button>
        </div>
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
      var dataobj = {
        username: this.ruleForm.username,
        password: this.ruleForm.password
      }
      var config = {
        method: 'post',
        url: 'http://127.0.0.1:8000/login/',
        headers: {
          'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
          'Content-Type': 'application/json'
        },
        data: dataobj
      }
      axios(config)
        .then(function (response) {
          console.log(JSON.stringify(response.data))
          if (response.status === 200) {
            window.location.href = '/#/MainPage'
          }
        })
        .catch(function (error) {
          console.log(error)
          if (error.response.status === 401) {
            window.alert('密码错误')
          } else if (error.response.status === 404) {
            window.alert('用户不存在')
          }
        })
    }
  }
}
</script>

<style>
html {
  background: linear-gradient(to right,
      rgba(186, 218, 179, 1) 30%,
      rgba(241, 164, 60, 1) 30%,
      rgba(241, 164, 60, 1) 70%,
      rgba(213, 100, 42, 1) 70%);
  height: 100%;
}

/* $color: #f1a43c;
    $color2: #bdd9b2;
    $color3: #f1ebc9; */
body {
  padding: 2rem;
  height: 100%;
}

h1 {
  font-size: 5vw;
  top: 80%;
  left: 0;
  margin: 0;
  padding: 0 2rem;
  box-sizing: border-box;
  transform: translate(0, -50%);
  position: absolute;
  color: #f1ebc9;
  width: 100%;
  text-align: center;
  font-family: 'Lobster', cursive;
}

    .signup_button {
      position: relative;
      /* right: 20px; */
      /* bottom: 20px; */
      /* top:1%;
      right: 50%; */
      border: none;
      box-shadow: none;
      width: 130px;
      height: 40px;
      line-height: 42px;
      -webkit-perspective: 230px;
      perspective: 230px;
      left: 45%;
    }

    .signup_button {
      background: rgb(0, 172, 238);
      background: linear-gradient(0deg, rgba(0, 172, 238, 1) 0%, rgba(2, 126, 251, 1) 100%);
      display: block;
      position: absolute;
      width: 130px;
      height: 40px;
      box-shadow: inset 2px 2px 2px 0px rgba(255, 255, 255, .5),
        7px 7px 20px 0px rgba(0, 0, 0, .1),
        4px 4px 5px 0px rgba(0, 0, 0, .1);
      border-radius: 5px;
      margin: 0;
      text-align: center;
      -webkit-box-sizing: border-box;
      -moz-box-sizing: border-box;
      box-sizing: border-box;
      -webkit-transition: all .3s;
      transition: all .3s;
    }

.signup_button {
  width: 130px;
  height: 40px;
  line-height: 42px;
  padding: 0;
  border: none;
  background: rgb(255, 27, 0);
  background: linear-gradient(0deg, rgba(255, 27, 0, 1) 0%, rgba(251, 75, 2, 1) 100%);
}

.signup_button:hover {
  color: #f0094a;
  background: transparent;
  box-shadow: none;
}

.signup_button:before,
.signup_button:after {
  content: '';
  position: absolute;
  top: 0;
  right: 0;
  height: 2px;
  width: 0;
  background: #f0094a;
  box-shadow:
    -1px -1px 5px 0px #fff,
    7px 7px 20px 0px #0003,
    4px 4px 5px 0px #0002;
  transition: 400ms ease all;
}

.signup_button:hover:after {
  left: auto;
  right: 0;
  width: 100%;
}

.signup_button:after {
  right: inherit;
  top: inherit;
  left: 0;
  bottom: 0;
}

.signup_button:hover:before,
.signup_button:hover:after {
  width: 100%;
  transition: 800ms ease all;
}

.intro_text {
  font-family: 'Lobster', cursive;
  margin-right: 55px;
}

p {
  font-family: 'Lato', sans-serif;
  font-weight: 300;
  text-align: center;
  font-size: 28px;
  color: #676767;
  top: 30%;
}

/* .btn-in {
      height: 400px;
      width: 600px;
      margin: 500px;
    } */
.intro_text {
  text-align: right;
}

.btn-1 {
  left: 45%;
  margin-top: 50px;
  align-self: center;
  text-align: center;
  width: 130px;
  height: 40px;
  color: #fff;
  border-radius: 5px;
  padding: 10px 25px;
  font-family: 'Lato', sans-serif;
  font-weight: 500;
  /* background: transparent; */
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  display: inline-block;
  box-shadow: inset 2px 2px 2px 0px rgba(255, 255, 255, .5),
    7px 7px 20px 0px rgba(0, 0, 0, .1),
    4px 4px 5px 0px rgba(0, 0, 0, .1);
  outline: none;
}

.btn-1 {
  background: rgb(6, 14, 131);
  background: linear-gradient(0deg, rgba(6, 14, 131, 1) 0%, rgba(12, 25, 180, 1) 100%);
  border: none;
}

.btn-1:hover {
  background: rgb(0, 3, 255);
  background: linear-gradient(0deg, rgba(0, 3, 255, 1) 0%, rgba(2, 126, 251, 1) 100%);
}
</style>
