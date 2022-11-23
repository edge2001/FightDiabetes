<template>
  <div>
    <el-header style="text-align: left; font-size: 12px;">
      <span style="font: italic 2em Georgia, serif;">Fightdiabetes</span>
    </el-header>
    <el-container style="height: 700px; border: 1px solid #eee">
      <el-aside width="200px">
        <el-menu :default-openeds="['1']" @open="handleOpen" @select="handleSelect" @close="handleClose">
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
      <el-main>
        <div v-if="1">
          <div id="myChart" :style="{width: '300px', height: '300px'}"></div>
        </div>
      </el-main>
    </el-container>
  </div>
</template>

<script>
export default {
  data () {
    return {
      myChart: null,
      ChartOptions: {
        title: { text: '血糖水平' },
        tooltip: {},
        xAxis: {
          data: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        },
        yAxis: {},
        series: [{
          name: 'mg/L',
          type: 'bar',
          data: [0, 0, 1, 2, 79, 82, 27]
        }]
      },
      key: null
    }
  },
  mounted () {
    // this.drawLine()
    if (location.href.indexOf('#reloaded') === -1) {
      location.href = location.href + '#reloaded'
      location.reload()
    }
  },
  methods: {
    drawLine () {
      // 基于刚刚准备好的 DOM 容器，初始化 EChart 实例
      this.myChart = this.$echarts.init(document.getElementById('myChart'))
      // 绘制图表
      this.myChart.setOption(this.ChartOptions)
    },
    handleOpen (key, keyPath) {
      console.log('open', key, keyPath)
    },
    handleSelect (key, keyPath) {
      console.log('select', key, keyPath)
      if (this.myChart != null) {
        this.myChart.dispose()
      }
      if (key === '1-1') {

      } else if (key === '1-2') {
        this.drawLine()
      }
    },
    handleClose (key, keyPath) {
      console.log('close', key, keyPath)
    }
  }
}
</script>

<style>
.el-header {
      background-color: coral;
      color: #333;
      line-height: 60px;
  }
  .el-aside {
    color: #333;
  }
</style>
