<template>
  <div>
    <el-container style="height: 500px; border: 1px solid #eee">
      <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <el-menu :default-openeds="['1']">
          <el-submenu index="1">
            <template slot="title"><i class="el-icon-message"></i>选项</template>
            <el-menu-item-group>
              <el-menu-item index="1-1"><i class="el-icon-user"></i>用户</el-menu-item>
              <el-menu-item index="1-2"><i class="el-icon-s-data"></i>健康数据</el-menu-item>
              <el-menu-item index="1-3"><i class="el-icon-finished"></i>打卡</el-menu-item>
              <el-menu-item index="1-4"><i class="el-icon-s-help"></i>论坛</el-menu-item>
              <el-menu-item index="1-5"><i class="el-icon-food"></i>饮食</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
        </el-menu>
      </el-aside>
    </el-container>
  </div>
</template>

<script>
export default {

}
</script>

<style>
  .el-header {
        background-color: #B3C0D1;
        color: #333;
        line-height: 60px;
      }
  .el-aside {
    color: #333;
  }
</style>
