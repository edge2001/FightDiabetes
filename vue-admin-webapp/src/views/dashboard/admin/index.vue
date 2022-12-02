<template>
  <div class="dashbord">
    <!-- <el-row class="chooseitem"> -->
    <!-- <el-switch v-model="value" active-color="#13ce66" inactive-color="#ff4949">
    </el-switch> -->
    <p class="choosefont">
      请选择要展示的数据项（这里显示月份平均值，想查询详细数据请移步数据页面～）
    </p>
    <div style="margin: 15px 0;"></div>
    <el-checkbox v-model="isGlucose">血糖</el-checkbox>
    <el-checkbox v-model="isWeight">体重</el-checkbox>
    <el-checkbox v-model="isKetone">血酮</el-checkbox>
    <el-checkbox v-model="isPressure">血压</el-checkbox>
    <!-- </el-row> -->
    <!-- cardlist -->
    <!-- <el-row class="infoCrads">
      <el-col :span="6">
        <div class="cardItem">
          <div class="cardItem_txt">
            <count-to
              class="cardItem_p0 color-green1"
              :startVal="startVal"
              :endVal="vistors"
              :duration="2000"
            ></count-to>
            <p class="cardItem_p1">Total Visitors</p>
          </div>
          <div class="cardItem_icon">
            <i class="el-icon-user color-green1"></i>
          </div>
        </div>
      </el-col>
      <el-col :span="6">
        <div class="cardItem">
          <div class="cardItem_txt">
            <count-to
              class="cardItem_p0 color-blue"
              :startVal="startVal"
              :endVal="message"
              :duration="2000"
            ></count-to>
            <p class="cardItem_p1">Messages</p>
          </div>
          <div class="cardItem_icon">
            <i class="el-icon-s-comment color-blue"></i>
          </div>
        </div>
      </el-col>
      <el-col :span="6">
        <div class="cardItem">
          <div class="cardItem_txt">
            <count-to
              class="cardItem_p0 color-red"
              :startVal="startVal"
              :endVal="order"
              :duration="2000"
            ></count-to>
            <p class="cardItem_p1">Total Order Placeed</p>
          </div>
          <div class="cardItem_icon">
            <i class="el-icon-shopping-cart-2 color-red"></i>
          </div>
        </div>
      </el-col>
      <el-col :span="6">
        <div class="cardItem">
          <div class="cardItem_txt">
            <count-to
              class="cardItem_p0 color-green2"
              :startVal="startVal"
              :endVal="profit"
              :duration="2000"
            ></count-to>
            <p class="cardItem_p1">Total Profit</p>
          </div>
          <div class="cardItem_icon">
            <i class="el-icon-wallet color-green2"></i>
          </div>
        </div>
      </el-col>
    </el-row> -->
    <!-- end -->
    <!-- lineEcharts -->
    <!-- <line-charts class="lCharts" :lineChartData="lineChartData"></line-charts> -->
    <div
      class="lineCharts"
      :style="{ width: width, height: height }"
      ref="myCharts"
    ></div>
    <!-- end -->
    <!-- table and pie -->
    <el-row class="tableChart">
      <el-col :span="16">
        <table-show :tableData="tableData" class="tableShow"></table-show>
      </el-col>
      <el-col :span="8">
        <pie-charts class="pieCharts"></pie-charts>
      </el-col>
    </el-row>
    <!-- end -->
    <!-- bar chart -->
    <bar-charts class="barCharts" :barData="barData"></bar-charts>
    <!-- end -->
  </div>
</template>

<script>
import CountTo from 'vue-count-to'
// import LineCharts from './components/LineCharts'
import PieCharts from './components/PieCharts'
import TableShow from './components/TableShow'
import BarCharts from './components/BarCharts'
import echarts from 'echarts'
import resize from '@/mixins/resize'
require('echarts/theme/macarons')
import {
  getCardsData,
  getTableData,
  getLineData,
  getBarData
} from '@/api/dashboard'
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
    },
    lineChartData: {
      type: Object,
      required: true
    }
    // isGlucose: {
    //   type: Boolean
    // },
    // isWeight: {
    //   type: Boolean
    // },
    // isKetone: {
    //   type: Boolean
    // },
    // isPressure: {
    //   type: Boolean
    // }
  },
  data() {
    return {
      checked: true,
      startVal: 0,
      vistors: 0,
      message: 0,
      order: 0,
      profit: 0,
      tableData: [],
      testData: [10000, 20000, 30000, 40000, 50000, 60000],
      testData2: [60000, 50000, 40000, 30000, 20000, 10000],
      testData3: [20000, 20000, 20000, 20000, 20000, 20000],
      testData4: [40000, 40000, 40000, 40000, 40000, 40000],
      // lineChartData: {},
      barData: {},
      checkAll: false,
      isIndeterminate: true,
      m_series: [],
      isGlucose: false,
      isWeight: false,
      isKetone: false,
      isPressure: false,
      mycharts: null
      // value: true
    }
  },
  watch: {
    lineChartData: {
      deep: true,
      handler(val) {
        this._setOption(val.inPrice, val.outPrice)
      }
    },
    isWeight: {
      // deep: true,
      // eslint-disable-next-line no-unused-vars
      handler(val) {
        this.m_series = []
        var m_glucose = {
          name: 'glucose(g/L)',
          type: 'line',
          itemStyle: {
            color: '#f4516c'
          },
          lineStyle: {
            color: '#f4516c'
          },
          smooth: true,
          data: this.testData,
          animationDuration: 2800,
          animationEasing: 'quadraticOut'
        }
        var m_weight = {
          name: 'kg',
          type: 'line',
          // areaStyle: {
          //   color: '#55a8fd',
          //   opacity: 0.3
          // },
          itemStyle: {
            color: '#55a8fd'
          },
          lineStyle: {
            color: '#55a8fd'
          },
          smooth: true,
          data: this.testData2,
          animationDuration: 2800,
          animationEasing: 'quadraticOut'
        }
        var m_ketone = {
          name: 'ketone(g/L)',
          type: 'line',
          itemStyle: {
            color: '#55a8fd'
          },
          lineStyle: {
            color: '#55a8fd'
          },
          smooth: true,
          data: this.testData3,
          animationDuration: 2800,
          animationEasing: 'quadraticOut'
        }
        var m_pressure = {
          name: 'mmHg',
          type: 'line',
          itemStyle: {
            color: '#55a8fd'
          },
          lineStyle: {
            color: '#55a8fd'
          },
          smooth: true,
          data: this.testData4,
          animationDuration: 2800,
          animationEasing: 'quadraticOut'
        }
        if (this.isGlucose === true) {
          this.m_series.push(m_glucose)
        }
        if (this.isWeight === true) {
          this.m_series.push(m_weight)
        }
        if (this.isKetone === true) {
          this.m_series.push(m_ketone)
        }
        if (this.isPressure === true) {
          this.m_series.push(m_pressure)
        }
        this._setOption(this.m_series)
      }
    },
    isGlucose: {
      // deep: true,
      // eslint-disable-next-line no-unused-vars
      handler(val) {
        // window.alert(this.m_series.length)
        this.m_series = []
        var m_glucose = {
          name: 'glucose(g/L)',
          type: 'line',
          itemStyle: {
            color: '#f4516c'
          },
          lineStyle: {
            color: '#f4516c'
          },
          smooth: true,
          data: this.testData,
          animationDuration: 2800,
          animationEasing: 'quadraticOut'
        }
        var m_weight = {
          name: 'kg',
          type: 'line',
          itemStyle: {
            color: '#55a8fd'
          },
          lineStyle: {
            color: '#55a8fd'
          },
          smooth: true,
          data: this.testData2,
          animationDuration: 2800,
          animationEasing: 'quadraticOut'
        }
        var m_ketone = {
          name: 'ketone(g/L)',
          type: 'line',
          itemStyle: {
            color: '#55a8fd'
          },
          lineStyle: {
            color: '#55a8fd'
          },
          smooth: true,
          data: this.testData3,
          animationDuration: 2800,
          animationEasing: 'quadraticOut'
        }
        var m_pressure = {
          name: 'mmHg',
          type: 'line',
          itemStyle: {
            color: '#55a8fd'
          },
          lineStyle: {
            color: '#55a8fd'
          },
          smooth: true,
          data: this.testData4,
          animationDuration: 2800,
          animationEasing: 'quadraticOut'
        }
        if (this.isGlucose === true) {
          this.m_series.push(m_glucose)
        }
        if (this.isWeight === true) {
          this.m_series.push(m_weight)
        }
        if (this.isKetone === true) {
          this.m_series.push(m_ketone)
        }
        if (this.isPressure === true) {
          this.m_series.push(m_pressure)
        }
        // window.alert(this.m_series.length)
        this._setOption(this.m_series)
      }
    },
    isKetone: {
      // deep: true,
      // eslint-disable-next-line no-unused-vars
      handler(val) {
        // window.alert(this.m_series.length)
        this.m_series = []
        var m_glucose = {
          name: 'glucose(g/L)',
          type: 'line',
          itemStyle: {
            color: '#f4516c'
          },
          lineStyle: {
            color: '#f4516c'
          },
          smooth: true,
          data: this.testData,
          animationDuration: 2800,
          animationEasing: 'quadraticOut'
        }
        var m_weight = {
          name: 'kg',
          type: 'line',
          itemStyle: {
            color: '#55a8fd'
          },
          lineStyle: {
            color: '#55a8fd'
          },
          smooth: true,
          data: this.testData2,
          animationDuration: 2800,
          animationEasing: 'quadraticOut'
        }
        var m_ketone = {
          name: 'ketone(g/L)',
          type: 'line',
          itemStyle: {
            color: '#55a8fd'
          },
          lineStyle: {
            color: '#55a8fd'
          },
          smooth: true,
          data: this.testData3,
          animationDuration: 2800,
          animationEasing: 'quadraticOut'
        }
        var m_pressure = {
          name: 'mmHg',
          type: 'line',
          itemStyle: {
            color: '#55a8fd'
          },
          lineStyle: {
            color: '#55a8fd'
          },
          smooth: true,
          data: this.testData4,
          animationDuration: 2800,
          animationEasing: 'quadraticOut'
        }
        if (this.isGlucose === true) {
          this.m_series.push(m_glucose)
        }
        if (this.isWeight === true) {
          this.m_series.push(m_weight)
        }
        if (this.isKetone === true) {
          this.m_series.push(m_ketone)
        }
        if (this.isPressure === true) {
          this.m_series.push(m_pressure)
        }
        // window.alert(this.m_series.length)
        this._setOption(this.m_series)
      }
    },
    isPressure: {
      // deep: true,
      // eslint-disable-next-line no-unused-vars
      handler(val) {
        // window.alert(this.m_series.length)
        this.m_series = []
        var m_glucose = {
          name: 'glucose(g/L)',
          type: 'line',
          itemStyle: {
            color: '#f4516c'
          },
          lineStyle: {
            color: '#f4516c'
          },
          smooth: true,
          data: this.testData,
          animationDuration: 2800,
          animationEasing: 'quadraticOut'
        }
        var m_weight = {
          name: 'kg',
          type: 'line',
          itemStyle: {
            color: '#55a8fd'
          },
          lineStyle: {
            color: '#55a8fd'
          },
          smooth: true,
          data: this.testData2,
          animationDuration: 2800,
          animationEasing: 'quadraticOut'
        }
        var m_ketone = {
          name: 'ketone(g/L)',
          type: 'line',
          itemStyle: {
            color: '#55a8fd'
          },
          lineStyle: {
            color: '#55a8fd'
          },
          smooth: true,
          data: this.testData3,
          animationDuration: 2800,
          animationEasing: 'quadraticOut'
        }
        var m_pressure = {
          name: 'mmHg',
          type: 'line',
          itemStyle: {
            color: '#55a8fd'
          },
          lineStyle: {
            color: '#55a8fd'
          },
          smooth: true,
          data: this.testData4,
          animationDuration: 2800,
          animationEasing: 'quadraticOut'
        }
        if (this.isGlucose === true) {
          this.m_series.push(m_glucose)
        }
        if (this.isWeight === true) {
          this.m_series.push(m_weight)
        }
        if (this.isKetone === true) {
          this.m_series.push(m_ketone)
        }
        if (this.isPressure === true) {
          this.m_series.push(m_pressure)
        }
        // window.alert(this.m_series.length)
        this._setOption(this.m_series)
      }
    }
  },
  created() {
    this._getAllData()
  },
  mounted() {
    this.$nextTick().then(() => {
      this.initEcharts()
    })
  },
  components: {
    // eslint-disable-next-line vue/no-unused-components
    CountTo,
    // eslint-disable-next-line vue/no-unused-components
    // LineCharts,
    PieCharts,
    TableShow,
    BarCharts
  },
  methods: {
    initEcharts() {
      this.mycharts = echarts.init(this.$refs.myCharts, 'macarons')
      if (Object.keys(this.lineChartData).length > 0) {
        this._setOption(this.lineChartData.inPrice, this.lineChartData.outPrice)
      }
    },
    // eslint-disable-next-line no-unused-vars
    _setOption(m_series) {
      this.mycharts.setOption(
        {
          title: {
            text: '健康数据',
            left: '16'
          },
          tooltip: {
            trigger: 'axis',
            axisPointer: {
              type: 'cross',
              label: {
                background: '#6a7985'
              }
            }
          },
          // legend: {
          //   data: ['血糖', '体重']
          // },
          grid: {
            left: '20',
            right: '20',
            bottom: '3',
            containLabel: true
          },
          xAxis: [
            {
              type: 'category',
              boundaryGap: false,
              data: ['1月', '2月', '3月', '4月', '5月', '6月']
            }
          ],
          yAxis: [
            {
              type: 'value'
            }
          ],
          series: m_series
          // series: [
          //   {
          //     name: '收入',
          //     type: 'line',
          //     // areaStyle: {
          //     //   color: '#f4516c',
          //     //   opacity: 0.3
          //     // },
          //     itemStyle: {
          //       color: '#f4516c'
          //     },
          //     lineStyle: {
          //       color: '#f4516c'
          //     },
          //     smooth: true,
          //     data: inprice,
          //     animationDuration: 2800,
          //     animationEasing: 'quadraticOut'
          //   },
          //   {
          //     name: '支出',
          //     type: 'line',
          //     // areaStyle: {
          //     //   color: '#55a8fd',
          //     //   opacity: 0.3
          //     // },
          //     itemStyle: {
          //       color: '#55a8fd'
          //     },
          //     lineStyle: {
          //       color: '#55a8fd'
          //     },
          //     smooth: true,
          //     data: this.testData,
          //     animationDuration: 2800,
          //     animationEasing: 'quadraticOut'
          //   }
          // ]
        },
        { notMerge: true }
      )
    },
    _getAllData() {
      this.$http
        .all([getCardsData(), getLineData(), getTableData(), getBarData()])
        .then(
          this.$http.spread((cardData, lineData, tabData, barData) => {
            this.vistors = cardData.data.vistors
            this.message = cardData.data.message
            this.order = cardData.data.order
            this.profit = cardData.data.profit
            this.lineChartData = lineData.data
            ;(this.tableData = tabData.data.tableList),
              (this.barData = barData.data)
          })
        )
    }
  }
}
</script>
<style scoped lang="scss">
$mgTop: 30px;
@mixin shadow {
  box-shadow: 0 0 10px #e2e2e2;
}
.choosefont {
  font-family: 'Helvetica Neue', Helvetica, 'PingFang SC', 'Hiragino Sans GB',
    'Microsoft YaHei', '微软雅黑', Arial, sans-serif;
  font-size: large;
}
.color-green1 {
  color: #40c9c6 !important;
}
.color-blue {
  color: #36a3f7 !important;
}
.color-red {
  color: #f4516c !important;
}
.color-green2 {
  color: #34bfa3 !important;
}
.dashbord {
  background-color: #f0f3f4;
}
.infoCrads {
  margin: 0 -20px 0 -20px;
  .el-col {
    padding: 0 20px;
    .cardItem {
      height: 108px;
      background: #fff;
    }
  }
}
.cardItem {
  color: #666;
  @include shadow();
  .cardItem_txt {
    float: left;
    margin: 26px 0 0 20px;
    .cardItem_p0 {
      font-size: 20px;
      font-weight: bold;
    }
    .cardItem_p1 {
      font-size: 16px;
    }
  }
  .cardItem_icon {
    float: right;
    margin: 24px 20px 0 0;
    i {
      font-size: 55px;
    }
  }
}
.lCharts {
  background: #fff;
  margin-top: $mgTop;
  padding: 30px 0;
  @include shadow();
}
.barCharts {
  background: #fff;
  margin-top: $mgTop;
  padding: 30px 0;
  @include shadow();
}
.pieCharts {
  background: #fff;
  padding: 20px 0;
  @include shadow();
}
.tableChart {
  margin-top: $mgTop;
}
</style>
