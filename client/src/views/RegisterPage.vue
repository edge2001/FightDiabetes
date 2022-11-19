<template>
  <div class="login">
    <div class="loginBox">
      <h2 class="loginH2">Register your Fightdiabetes</h2>
      <div class="loginCon">
        <div class="titleDiv">
          <p class="reminder">initialize your username and password:</p>
        </div>
        <el-form ref="loginForm" :rules="rules" :model="ruleForm">
          <el-form-item prop="user">
            <el-input placeholder="请输入账号" prefix-icon="el-icon-user" v-model="username"></el-input>
          </el-form-item>
          <el-form-item prop="password">
            <el-input placeholder="请输入密码" prefix-icon="el-icon-lock" v-model="password" show-password>
            </el-input>
          </el-form-item>
          <el-form-item prop="password_confirm">
            <el-input placeholder="请再次输入密码" prefix-icon="el-icon-lock" v-model="password_confirm" show-password>
            </el-input>
          </el-form-item>
          <el-form-item prop="email">
            <el-input placeholder="请输入邮箱" prefix-icon="el-icon-office-building" v-model="email">
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
      username: '',
      password: '',
      password_confirm: '',
      email: ''
    }
  },
  mounted () {
    if (location.href.indexOf('#reloaded') === -1) {
      location.href = location.href + '#reloaded'
      location.reload()
    }
  },
  methods: {
    back_login () {
      window.location.href = '/#/login'
    },
    is_upper (tmpChar) {
      var asciiNum = tmpChar.charCodeAt(0)
      if ((asciiNum >= 65 && asciiNum <= 90)) {
        return true
      } else {
        return false
      }
    },
    is_lower (tmpChar) {
      var asciiNum = tmpChar.charCodeAt(0)
      if ((asciiNum >= 97 && asciiNum <= 122)) {
        return true
      } else {
        return false
      }
    },
    is_alpha (tmpChar) {
      var asciiNum = tmpChar.charCodeAt(0)
      if ((asciiNum >= 65 && asciiNum <= 90) || (asciiNum >= 97 && asciiNum <= 122)) {
        return true
      } else {
        return false
      }
    },
    is_digit (tmpChar) {
      var asciiNum = tmpChar.charCodeAt(0)
      if ((asciiNum >= 48 && asciiNum <= 57)) {
        return true
      } else {
        return false
      }
    },
    is_special (tmpChar) {
      var specialSymbol = ['!', ',', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '=', '+', '{', '}', '[', ']', ':', ';', ',', '.', '/', '?', '<', '>']
      for (var i = 0; i < specialSymbol.length; i++) {
        if (tmpChar === specialSymbol[i]) {
          return true
        }
      }
      return false
    },
    is_username_valid (username) {
      if (username.length < 8 || username.length > 20) {
        return false
      }
      var hasDigit = 0
      var hasAlpha = 0
      var hasSpecialSymbol = 0
      for (var i = 0; i < username.length; i++) {
        if (hasDigit + hasAlpha + hasSpecialSymbol === 3) {
          break
        }
        var tmpChar = username[i]
        if (hasDigit === 0) {
          if (this.is_digit(tmpChar) === true) {
            hasDigit = 1
          }
        }
        if (hasAlpha === 0) {
          if (this.is_alpha(tmpChar) === true) {
            hasAlpha = 1
          }
        }
        if (hasSpecialSymbol === 0) {
          if (this.is_special(tmpChar) === true) {
            hasSpecialSymbol = 1
          }
        }
      }
      if (hasDigit + hasAlpha + hasSpecialSymbol !== 3) {
        return false
      }
      return true
    },
    is_password_valid (password) {
      if (password.length < 8 || password.length > 20) {
        return false
      }
      var hasDigit = 0
      var hasUpperAlpha = 0
      var hasLowerAlpha = 0
      var hasSpecialSymbol = 0
      for (var i = 0; i < password.length; i++) {
        if (hasDigit + hasUpperAlpha + hasLowerAlpha + hasSpecialSymbol === 4) {
          break
        }
        var tmpChar = password[i]
        if (hasDigit === 0) {
          if (this.is_digit(tmpChar) === true) {
            hasDigit = 1
          }
        }
        if (hasUpperAlpha === 0) {
          if (this.is_upper(tmpChar) === true) {
            hasUpperAlpha = 1
          }
        }
        if (hasLowerAlpha === 0) {
          if (this.is_lower(tmpChar) === true) {
            hasLowerAlpha = 1
          }
        }
        if (hasSpecialSymbol === 0) {
          if (this.is_special(tmpChar) === true) {
            hasSpecialSymbol = 1
          }
        }
      }
      if (hasDigit + hasUpperAlpha + hasLowerAlpha + hasSpecialSymbol !== 4) {
        return false
      }
      return true
    },
    send_data: function () {
      var dataobj = {
        'username': this.username,
        'password': this.password,
        'email': this.email
      }
      if (this.is_username_valid(dataobj['username']) === false) {
        this.$message.error('用户名不合法！')
        return
      }
      if (this.is_password_valid(dataobj['password']) === false) {
        this.$message.error('密码格式不对！')
        return
      }
      if (this.password !== this.password_confirm) {
        this.$message.error('两次输入的密码不匹配！')
        return
      }
      const path = 'http://127.0.0.1:8000/register/'
      var configGet = {
        method: 'POST',
        url: path,
        headers: {
          'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
          'Content-Type': 'application/json'
        },
        data: dataobj
      }
      axios(configGet)
        .then(function (response) {
          console.log(JSON.stringify(response.data))
          if (response.status === 200) {
            window.alert('注册成功')
            window.location.href = '/#/MainPage'
          }
        })
        .catch(function (error) {
          console.log(error)
          if (error.response.status === 401) {
            window.alert('重复的用户名！')
          }
        })
      var config = {
        method: 'POST',
        url: path,
        headers: {
          'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
          'Content-Type': 'application/json'
        },
        data: dataobj
      }
      // arrived here
      axios(config)
        .then(function (response) {
          console.log(JSON.stringify(response.data))
        })
        .catch(function (error) {
          console.log(error)
        })
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
html {
      background-image: url('../images/register.jpeg');
      background-size: 100% 100%;
      display: inline-block;
      height: 100%;
    }

h2 {
  font-family: "Lucida Console",
    "Courier New",
    monospace;
  color:crimson;
  font-size: 40px;
  text-align: center;
}
.reminder {
  font-family:
    'Lobster',
    cursive;
  color:orange;
  text-align: center;
}
</style>
