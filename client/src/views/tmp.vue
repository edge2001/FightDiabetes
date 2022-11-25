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
      <button class="reset">重新获取</button>
      <form action="">
        <input type="text" class="signup-num" placeholder="请输入账号">
        <input type="password" class="signup-pwd" placeholder="请输入密码">
        <input type="password" class="signup-repwd" placeholder="再次输入确认密码">
        <!-- <div class="random">????</div> -->
        <input type="text" class="write" placeholder="请输入验证码">
        <input type="submit" value="注册" class="signup-button">
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
            window.alert('密码错误!!')
          } else if (error.response.status === 404) {
            window.alert('用户不存在')
            this.jump_to_Register()
          }
        })
    }
  }
}
</script>

<style>
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
  margin-top: -18px;
  margin-left: 60px;
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
  height: 70px;
  outline: none;
  margin-top: 15px;
  margin-left: 60px;
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
  margin-top: 15px;
  margin-left: 60px;
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
