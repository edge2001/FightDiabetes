<template>
  <div ref="myCharts" :style="{ width: width, height: height }"></div>
</template>

<script>
import echarts from 'echarts'
import resize from '@/mixins/resize'
import chart_data from '../index.vue'
require('echarts/theme/macarons') // echarts theme
export default {
  mixins: [resize],
  props: {
    width: {
      type: String,
      default: '100%'
    },
    height: {
      type: String,
      default: '350px'
    }
  },
  data() {
    return {
      mycharts: null,
      nor_time: 0,
      abv_time: 0,
      blw_time: 0,
      not_time: 0,
      time: 0
    }
  },
  mounted() {
    this.$nextTick().then(() => {
      this.initEcharts()
    })
  },
  methods: {
    initEcharts() {
      // window.alert(chart_data['above_time'])
      this.mycharts = echarts.init(this.$refs.myCharts, 'macarons')
      this._setOption()
    },
    _setOption() {
      this.mycharts.setOption({
        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b} : {c} ({d}%)'
        },
        legend: {
          left: 'center',
          bottom: '10',
          data: ['Vue', 'js', 'html', 'css', 'webpack', 'node']
        },
        series: [
          {
            name: '统计数据',
            type: 'pie',
            roseType: 'radius',
            radius: [15, 120],
            center: ['50%', '42%'],
            data: [
              { value: chart_data['above_time'], name: '偏高天数' },
              { value: 35, name: '偏低天数' },
              { value: 20, name: '正常天数' },
              { value: 10, name: '未测天数' }
            ],
            animationEasing: 'cubicInOut',
            animationDuration: 2600
          }
        ]
      })
    }
  }
}
</script>
<style></style>
