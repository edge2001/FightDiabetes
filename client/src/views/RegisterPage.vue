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
            <el-input placeholder="请输入账号" prefix-icon="el-icon-user" v-model="ruleForm.username"></el-input>
          </el-form-item>
          <el-form-item prop="password">
            <el-input placeholder="请输入密码" prefix-icon="el-icon-lock" v-model="ruleForm.password" show-password>
            </el-input>
          </el-form-item>
          <el-form-item prop="password">
            <el-input placeholder="请再次输入密码" prefix-icon="el-icon-lock" v-model="ruleForm.password_confirm" show-password>
            </el-input>
          </el-form-item>
          <el-button type="primary" class="loginBtn" @click="send_data()">登录</el-button>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      ruleForm: {
        username: '',
        password: '',
        password_confirm: ''
      }
    }
  }
}
</script>

<style>

</style>
