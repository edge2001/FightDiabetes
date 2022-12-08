<template>
  <div class="wrapper" :class="{ closeBar: opened }">
    <m-header></m-header>
    <transition
      enter-active-class="animated bounceInRight"
      leave-active-class="animated bounceOutRight"
    >
      <notificat-bar v-show="msgIsShow"></notificat-bar>
    </transition>
    <div class="wrapper_con">
      <el-container style="height: 100%">
        <el-container>
          <el-aside width="201px"><main-page></main-page></el-aside>
          <el-main><router-view></router-view></el-main>
        </el-container>
      </el-container>
    </div>
  </div>
</template>

<script>
import MHeader from './components/header'
import NotificatBar from '@/components/NotificatBar'
import { mapGetters } from 'vuex'
import driver from '@/mixins/useDriver'
import MainPage from '@/layout/components/MainPage'
export default {
  name: 'layout',
  mixins: [driver],
  mounted() {
    if (this.showDriver === 'yes') {
      this.guide()
      this.$store.commit('app/SET_DRIVER', 'no')
    }
  },
  computed: {
    ...mapGetters(['opened', 'msgIsShow', 'showDriver'])
  },
  components: {
    MHeader,
    NotificatBar,
    MainPage
  }
}
</script>
