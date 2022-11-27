<template>
  <div class="background">
    <!-- 登录 -->
    <div class="login">
      <p class="login-value">LOG IN</p>
      <div><i class="el-icon-user"></i><input type="text" class="login-num" placeholder="请输入账号"
          v-model="ruleForm.username"></div>
      <div><i class="el-icon-lock"></i><input type="password" class="login-pwd" placeholder="请输入密码"
          v-model="ruleForm.password"></div>
      <input type="button" value="忘记密码？" class="forget">
      <input type="submit" value="登录" class="login-button" @click="send_data()">
    </div>
    <div class="change-register-box">
      <p class="a">No account?</p>
      <p class="b">join Fightdiabetes!</p>
      <button class="change-register-button">SIGN UP &nbsp;></button>
    </div>
    <!-- 注册 -->
    <div class="register">
      <p class="signup-value">SIGN UP</p>
      <!-- <button class="reset">重新获取</button> -->
      <form action="">
        <div><i class="el-icon-user"></i><input type="text" class="signup-num" placeholder="请输入账号" v-model="ruleForm.register_username"></div>
        <div><i class="el-icon-lock"></i><input type="password" class="signup-pwd" placeholder="请输入密码" v-model="ruleForm.register_password"></div>
        <div><i class="el-icon-check"></i><input type="password" class="signup-repwd" placeholder="再次输入确认密码" v-model="ruleForm.register_confirm_password"></div>
        <!-- <div class="random">????</div> -->
        <!-- <input type="text" class="write" placeholder="请输入验证码"> -->
        <input type="submit" value="注册" class="signup-button" @click="send_data_register()">
      </form>
    </div>
    <div class="change-login-box">
      <p class="c">欢迎加入</p>
      <p class="d">快去登陆看看吧</p>
      <button class="change-login-button">LOG IN</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import $ from 'jquery'
export default {
  data () {
    return {
      ruleForm: {
        username: '',
        password: '',
        register_username: '',
        register_password: '',
        register_confirm_password: '',
        email: 'hello.cn'
      }
    }
  },
  methods: {
    jump_to_Register: function () {
      window.location.href = '/#/register'
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
    is_email_valid (email) {
      var mLen = email.length
      var lastLen = 0
      for (var i = mLen - 1; i >= 0; i--) {
        if (email[i] === '.') {
          break
        }
        lastLen++
      }
      if (lastLen !== 2 && lastLen !== 3) {
        return false
      }
      if (lastLen === 2) {
        if (email[i + 1] === 'c' && email[i + 2] === 'n') {
          return true
        }
        return false
      }
      if (lastLen === 3) {
        if (email[i + 1] === 'c' && email[i + 2] === 'o' && email[i + 3] === 'm') {
          return true
        }
        return false
      }
      return false
    },
    send_data: function () {
      var dataobj = {
        username: this.ruleForm.username,
        password: this.ruleForm.password,
        islogin: true
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
            this.jump_to_Register()
          }
        })
    },
    send_data_register: function () {
      var dataobj = {
        'username': this.ruleForm.register_username,
        'password': this.ruleForm.register_password,
        'email': this.ruleForm.email,
        'islogin': false
      }
      // if (this.is_username_valid(dataobj['username']) === false) {
      //   this.$message.error('用户名不合法！')
      //   return
      // }
      // if (this.is_password_valid(dataobj['password']) === false) {
      //   this.$message.error('密码格式不对！')
      //   return
      // }
      // if (this.password !== this.password_confirm) {
      //   this.$message.error('两次输入的密码不匹配！')
      //   return
      // }
      // if (this.is_email_valid(dataobj['email']) === false) {
      //   this.$message.error('请输入正确的邮箱地址！')
      //   return
      // }
      const path = 'http://127.0.0.1:8000/login/'
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
            // window.location.href = '/#/MainPage'
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
document.addEventListener('DOMContentLoaded', function (event) {
  document.addEventListener('selectstart', function (event) {
    event.preventDefault()
  })
  document.addEventListener('contextmenu', function (event) {
    event.preventDefault()
  })
  var randomBox = document.querySelector('.random')
  var btn = document.querySelector('.reset')
  // eslint-disable-next-line no-unused-vars
  var write = document.querySelector('.write')
  function random (min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min
  }
  btn.addEventListener('click', function () {
    btn.style.backgroundColor = '#fff'
    window.setTimeout(function (event) {
      btn.style.backgroundColor = 'rgb(255, 224, 146)'
    }, 50)
    var randoms = random(1000, 9999)
    window.alert(randoms)
    console.log(randoms)
    randomBox.innerHTML = randoms
  })
})
$(function () {
  $('.change-register-button').on('click', function () {
    $('.login').animate(
      {
        'left': '240px'
      }, 400, function () {
        $('.login').css({
          'display': 'none',
          'left': '60px'
        })
        $('.change-register-box').css('display', 'none')
        $('.register').css('display', 'block')
        $('.change-login-box').css('display', 'block')
      }
    )
  })
  $('.change-login-button').on('click', function () {
    $('.register').animate(
      {
        'right': '240px'
      }, 400, function () {
        $('.register').css({
          'display': 'none',
          'right': '60px'
        })
        $('.change-login-box').css('display', 'none')
        $('.login').css('display', 'block')
        $('.change-register-box').css('display', 'block')
      }
    )
  })
})
</script>

<style>
html {
  background-color: antiquewhite;
  background-image: url('../images/logo.png');
  background-size: 12% 20%;
  display: inline-block;
  height: 100%;
  background-repeat: no-repeat;
}
.background {
  width: 900px;
  height: 400px;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  background-color: rgba(10, 10, 10, 0.598);
}

.el-icon-user {
  border-right: 30px;
  margin-left: 30px;
  text-align: right;
  color: coral;
}

.el-icon-lock {
  border-right: 30px;
  margin-left: 30px;
  text-align: right;
  color: coral;
}

.el-icon-check {
  border-right: 30px;
  margin-left: 30px;
  text-align: right;
  color: coral;
}

/* 登录框 */
.login {
  position: absolute;
  top: -12%;
  left: 60px;
  width: 600px;
  height: 500px;
  background-color: rgb(249, 249, 249);
  z-index: 10;
  box-shadow: 0 0 12px 0.6px rgb(106, 106, 106);
  background-color: azure;
  /* display: none; */
}

.login-value {
  width: 600px;
  font-size: 40px;
  font-weight: bold;
  color: blue;
  padding-left: 60px;
  margin-top: 90px;
}

.login-num {
  width: 485px;
  height: 50px;
  outline: none;
  margin-top: -5px;
  margin-left: 30px;
  box-sizing: border-box;
  border-top: none;
  border-left: none;
  border-right: none;
  border-bottom: 2px solid rgb(182, 182, 182);
  background-color: transparent;
  font-size: 20px;
  color: grey;
}

.login-pwd {
  width: 485px;
  height: 50px;
  outline: none;
  margin-top: 30px;
  margin-left: 30px;
  box-sizing: border-box;
  border-top: none;
  border-left: none;
  border-right: none;
  border-bottom: 2px solid rgb(182, 182, 182);
  background-color: transparent;
  font-size: 20px;
  color: grey;
}

.forget {
  position: absolute;
  bottom: 90px;
  left: 60px;
  width: 220px;
  height: 60px;
  border: 1.5px solid rgb(151, 151, 151);
  background-color: transparent;
  font-size: 18px;
  font-weight: bold;
  letter-spacing: 2px;
  color: rgb(113, 113, 113);
}

.forget:hover {
  background-color: rgb(235, 235, 235);
}

.login-button {
  position: absolute;
  bottom: 90px;
  right: 60px;
  width: 220px;
  height: 60px;
  border: none;
  background-color: rgb(222, 59, 59);
  ;
  font-size: 20px;
  font-weight: bold;
  letter-spacing: 10px;
  color: rgb(255, 255, 255);
  text-shadow: 1px 1px 1px rgb(138, 138, 138);
}

.login-button:hover {
  background-color: rgb(199, 38, 38);
}

/* 切换注册框的盒子 */
.change-register-box {
  position: absolute;
  right: 0px;
  width: 240px;
  height: 400px;
  background-color: transparent;
  /* display: none; */
}

.a {
  position: absolute;
  top: 90px;
  left: 62px;
  font-size: 18px;
  font-weight: bold;
  color: rgba(255, 255, 255, 0.846);
  letter-spacing: 2px;
}

.b {
  position: absolute;
  top: 140px;
  left: 30px;
  font-size: 18px;
  font-weight: bold;
  color: rgba(255, 255, 255, 0.858);
  letter-spacing: 2px;
}

.change-register-button {
  position: absolute;
  left: 46px;
  bottom: 120px;
  width: 140px;
  height: 50px;
  border: 1.5px solid #fff;
  background-color: transparent;
  letter-spacing: 2px;
  color: #fff;
  font-size: 16px;
  font-weight: bold;
  border-radius: 5px;
}

.change-register-button:hover {
  border: 1.5px solid rgb(217, 217, 217);
  color: rgb(217, 217, 217);
}

/* 注册框 */
.register {
  position: absolute;
  top: -12%;
  right: 60px;
  width: 600px;
  height: 500px;
  background-color: rgb(249, 249, 249);
  display: none;
  z-index: 10;
  box-shadow: 0 0 12px 0.6px rgb(106, 106, 106);
}

.change-login-box {
  position: absolute;
  left: 0;
  width: 240px;
  height: 400px;
  background-color: transparent;
  display: none;
}

.signup-value {
  width: 600px;
  font-size: 40px;
  font-weight: bold;
  color: rgb(255, 108, 108);
  padding-left: 40px;
  margin-top: 30px;
}

.signup-num {
  width: 485px;
  height: 50px;
  outline: none;
  margin-top: 0px;
  margin-left: 15px;
  box-sizing: border-box;
  border-top: none;
  border-left: none;
  border-right: none;
  border-bottom: 2px solid rgb(182, 182, 182);
  background-color: transparent;
  font-size: 20px;
  color: grey;
}

.signup-pwd {
  width: 485px;
  height: 50px;
  outline: none;
  margin-top: 30px;
  margin-left: 15px;
  box-sizing: border-box;
  border-top: none;
  border-left: none;
  border-right: none;
  border-bottom: 2px solid rgb(182, 182, 182);
  background-color: transparent;
  font-size: 20px;
  color: grey;
}

.signup-repwd {
  width: 485px;
  height: 50px;
  outline: none;
  margin-top: 30px;
  margin-left: 15px;
  box-sizing: border-box;
  border-top: none;
  border-left: none;
  border-right: none;
  border-bottom: 2px solid rgb(182, 182, 182);
  background-color: transparent;
  font-size: 20px;
  color: grey;
}

.random {
  position: absolute;
  top: 305px;
  left: 60px;
  width: 110px;
  height: 47px;
  border: 1px solid black;
  line-height: 47px;
  text-align: center;
  font-size: 27px;
  font-weight: bold;
  letter-spacing: 3px;
  background-color: rgb(221, 246, 255);
  color: grey;
}

.reset {
  position: absolute;
  top: 305px;
  left: 186px;
  width: 150px;
  height: 47px;
  border: 1px solid black;
  line-height: 47px;
  text-align: center;
  font-size: 16px;
  font-weight: 600;
  letter-spacing: 3px;
  background-color: rgb(255, 224, 146);
  border-radius: 6px;
  color: rgb(92, 92, 92);
  /* text-shadow: 2px 1px 1px grey; */
}

.write {
  position: absolute;
  top: 305px;
  right: 58px;
  width: 180px;
  height: 47px;
  border: 1px solid black;
  outline: none;
  font-size: 22px;
  padding-left: 10px;
}

.signup-button {
  position: absolute;
  bottom: 50px;
  right: 60px;
  width: 482px;
  height: 60px;
  border: none;
  background-color: rgb(222, 59, 59);
  font-size: 20px;
  font-weight: bold;
  letter-spacing: 15px;
  color: rgb(255, 255, 255);
  text-shadow: 1px 1px 1px rgb(138, 138, 138);
}

.signup-button:hover {
  background-color: rgb(199, 38, 38);
}

.c {
  position: absolute;
  top: 90px;
  left: 79px;
  font-size: 18px;
  font-weight: bold;
  color: rgba(255, 255, 255, 0.846);
  letter-spacing: 2px;
}

.d {
  position: absolute;
  top: 140px;
  left: 46px;
  font-size: 18px;
  font-weight: bold;
  color: rgba(255, 255, 255, 0.858);
  letter-spacing: 2px;
}

.change-login-button {
  position: absolute;
  left: 46px;
  bottom: 120px;
  width: 140px;
  height: 50px;
  border: 1.5px solid #fff;
  background-color: transparent;
  letter-spacing: 2px;
  color: #fff;
  font-size: 16px;
  font-weight: bold;
  border-radius: 5px;
}

.change-login-button:hover {
  border: 1.5px solid rgb(217, 217, 217);
  color: rgb(217, 217, 217);
}
</style>
