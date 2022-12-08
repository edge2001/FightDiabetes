<template>
  <div style="height: 100%;">
    <el-menu
      background-color="#545c64"
      text-color="#ffffff"
      active-text-color="#ffd04b"
      class="el-menu-vertical-demo"
      router
    >
      <el-menu-item index="/dashbord/admin"
        ><i class="el-icon-menu"></i>主页</el-menu-item
      >
      <el-menu-item index="/dashbord/user"
        ><i class="el-icon-user"></i>用户信息</el-menu-item
      >
      <el-menu-item index="/dashbord/sports"
        ><i class="el-icon-basketball"></i>运动</el-menu-item
      >
    </el-menu>
  </div>
</template>

<script>
export default {
  name: 'MainPage'
}
</script>

<style scoped>
.el-menu-vertical-demo {
  height: 100%;
}
</style>
