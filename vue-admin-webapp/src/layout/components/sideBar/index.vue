<template>
  <div class="sideBar" id="domSideBar">
    <el-scrollbar>
      <!-- <el-button @click="testfunc()">默认按钮</el-button> -->
      <el-menu
        :default-active="activeMenu"
        class="el-menu-vertical-demo"
        background-color="#3a3f51"
        text-color="#b5b6bd"
        active-text-color="#ffd04b"
        mode="vertical"
        :collapse-transition="false"
        :collapse="opened"
      >
        <el-menu-item @click="jumpTomain()">
          <template slot="title">
            <i class="el-icon-menu"></i>
            <span>主页</span>
          </template>
        </el-menu-item>
        <el-menu-item>
          <template slot="title">
            <i class="el-icon-user"></i>
            <span>用户信息</span>
          </template>
        </el-menu-item>
        <el-menu-item>
          <template slot="title">
            <i class="el-icon-check"></i>
            <span>打卡</span>
          </template>
        </el-menu-item>
        <el-menu-item>
          <template slot="title">
            <i class="el-icon-check"></i>
            <span>健康标准</span>
          </template>
        </el-menu-item>
        <sidebar-item
          v-for="item in routes"
          :key="item.path"
          :item="item"
          :basePath="item.path"
        ></sidebar-item>
      </el-menu>
    </el-scrollbar>
  </div>
</template>

<script>
import SidebarItem from './SideBarItem'
import { mapGetters } from 'vuex'
export default {
  components: { SidebarItem },
  computed: {
    ...mapGetters(['routes', 'opened']),
    // booleanOpen() {
    //   return this.opened === 'true' ? true : false
    // },
    activeMenu() {
      return this.$route.path
    }
  },
  methods: {
    testfunc() {
      window.alert('shit')
    },
    jumpTomain() {
      window.location.href = '/#/login'
    }
  }
}
</script>
