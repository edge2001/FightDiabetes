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
        ><i class="el-icon-s-claim"></i>打卡</el-menu-item
      >
      <el-menu-item index="/dashbord/health"
        ><i class="el-icon-check"></i>健康数据录入</el-menu-item
      >
      <el-menu-item index="/dashbord/food"
        ><i class="el-icon-food"></i>饮食查询</el-menu-item
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
