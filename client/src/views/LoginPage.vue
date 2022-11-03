<template>
  <div>
    <el-container>
      <el-header>Login Page</el-header>
      <el-main>
        username
        <el-input v-model="input_username" placeholder="请输入内容"></el-input>
        password
        <el-input v-model="input_password" placeholder="请输入内容"></el-input>
      </el-main>
    </el-container>
  </div>
</template>

<script>
export default {
  data () {
    return {
      input_username: '',
      input_password: ''
    }
  }
}
</script>

<style>
  .el-header {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
  }
  .el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: left;
    line-height: 60px;
  }
</style>
