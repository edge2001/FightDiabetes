<template>
  <div>
    <h1 class="mfont">欢迎加入fightDiabetes!在这里，和我们一起战胜糖尿病吧</h1>
    <div>
      <div class="showImg">
        <img
          @mouseover="changeInterval(true)"
          @mouseleave="changeInterval(false)"
          @click="jumpToArticle(null)"
          v-for="item in imgArr"
          :key="item.id"
          :src="item.url"
          alt="暂无图片"
          v-show="item.id === currentIndex"
        />

        <div @click="clickIcon('up')" class="iconDiv icon-left">
          <i class="el-icon-caret-left"></i>
        </div>

        <div @click="clickIcon('down')" class="iconDiv icon-right">
          <i class="el-icon-caret-right"></i>
        </div>

        <div class="banner-circle">
          <ul>
            <li
              @click="changeImg(item.id)"
              v-for="item in imgArr"
              :key="item.id"
              :class="item.id === currentIndex ? 'active' : ''"
            ></li>
          </ul>
        </div>
        <div
          class="mfont"
          style="text-align:left;position: absolute;top:300px;left:0px;background: rgba(10,10,10,0.5);"
        >
          {{ title }}
        </div>
      </div>
      <div class="articleBar">
        <h4 style="font-size:28px">其他文章</h4>
        <ul>
          <li
            class="articleTitles"
            v-for="titles in titleList"
            @click="jumpToArticle(titles.id)"
          >
            {{ titles.title }}
          </li>
        </ul>
      </div>
    </div>
    
    <h1 class="mfont">这里是您近期血糖数据</h1>
    <div class="dashbord">
      <!-- <button @click="testfunc()"></button> -->
      <el-select v-model="value" placeholder="请选择展示时间">
        <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value"
        >
        </el-option>
      </el-select>
      <div v-if="this.isMainPage === true">
        <el-row class="tableChart">
          <!-- <el-col :span="16">
          <table-show :tableData="tableData" class="tableShow"></table-show>
        </el-col> -->
          <el-col :span="12">
            <!-- <pie-charts class="pieCharts"></pie-charts> -->
            <div
              ref="PieCharts"
              :style="{ width: width, height: height }"
            ></div>
          </el-col>
          <el-col :span="12">
            <!-- <bar-charts class="barCharts" :barData="barData"></bar-charts> -->
            <div
              ref="Barcharts"
              :style="{ width: width, height: height }"
            ></div>
          </el-col>
          <!-- <el-col :span="16">
          <bar-charts class="barCharts" :barData="barData"></bar-charts>
        </el-col> -->
        </el-row>
        <!-- <p class="choosefont">
        请选择要展示的数据项（这里显示月份平均值，想查询详细数据请移步数据页面～）
      </p>
      <div style="margin: 15px 0;"></div>
      <el-checkbox v-model="isGlucose">血糖</el-checkbox>
      <el-checkbox v-model="isWeight">体重</el-checkbox>
      <el-checkbox v-model="isKetone">血酮</el-checkbox>
      <el-checkbox v-model="isPressure">血压</el-checkbox>
      <div
        class="lineCharts"
        :style="{ width: width, height: height }"
        ref="PieCharts"
      ></div> -->
      </div>
      <!-- <el-row class="tableChart">
      <el-col :span="16">
        <table-show :tableData="tableData" class="tableShow"></table-show>
      </el-col>
      <el-col :span="8">
        <pie-charts class="pieCharts"></pie-charts>
      </el-col>
    </el-row>
    <bar-charts class="barCharts" :barData="barData"></bar-charts> -->
    </div>
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
import axios from 'axios'
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
    },
    barData: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      currentIndex: 0, //当前所在图片下标
      timer: null, //定时轮询
      imgArr: [
        {
          id: 0,
          url: require('../../images/1.jpg')
        },
        {
          id: 1,
          url: require('../../images/2.jpg')
        },
        {
          id: 2,
          url: require('../../images/3.jpg')
        },
        {
          id: 3,
          url: require('../../images/4.jpg')
        }
      ],
      options: [
        {
          value: '7Days',
          label: '7days'
        },
        {
          value: '30Days',
          label: '30days'
        }
      ],
      max_glucose: 0,
      min_glucose: 0,
      emp_glucose: 0,
      before_glucose: 0,
      after_glucose: 0,
      sleep_glucose: 0,
      Barcharts: null,
      normal_time: 0,
      above_time: 0,
      below_time: 0,
      value: '',
      not_time: 0,
      time: 0,
      checked: true,
      startVal: 0,
      vistors: 0,
      message: 0,
      order: 0,
      profit: 0,
      tableData: [],
      checkAll: false,
      isIndeterminate: true,
      m_series: [],
      isGlucose: false,
      isWeight: false,
      isKetone: false,
      isPressure: false,
      PieCharts: null,
      isMainPage: true,
      isUserInfo: false,
      isClockIn: false,
      isHealthStandard: false,
      showDays: 0,
      // value: true
      title: '1145141919810',
      titleList: [
        {
          title: '用知识点亮寒冬心灯用行动助力糖尿病之友',
          id: 5
        }
      ]
    }
  },
  watch: {
    value: {
      deep: true,
      // eslint-disable-next-line no-unused-vars
      handler(val) {
        if (this.value == '7Days') {
          this.showDays = 7
          this.getPieData(30)
          this.getBarChartData(30)
          this.initBarChart()
          this.initEcharts()
        } else {
          this.showDays = 30
          this.getPieData(7)
          this.getBarChartData(7)
          this.initBarChart()
          this.initEcharts()
        }
      }
    },
    // value is the choice of 7 days or 30 days of show
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
      // this.initEcharts()
      // this.initBarChart()
    })
    this.getPieData(7)
    this.getBarChartData(7)
    this.initEcharts()
    this.initBarChart()
    this.startInterval()
    this.getTitle()
  },
  components: {
    // eslint-disable-next-line vue/no-unused-components
    CountTo,
    // eslint-disable-next-line vue/no-unused-components
    // LineCharts,
    // eslint-disable-next-line vue/no-unused-components
    PieCharts,
    // eslint-disable-next-line vue/no-unused-components
    TableShow,
    // eslint-disable-next-line vue/no-unused-components
    BarCharts
  },
  methods: {
    initBarChart() {
      this.Barcharts = echarts.init(this.$refs.Barcharts, 'macarons')
      this._setBarOption()
    },
    _setBarOption() {
      this.Barcharts.setOption({
        title: {
          text: '血糖数据(mmol/L)',
          left: '16'
        },
        legend: {
          data: ['']
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            // 坐标轴指示器，坐标轴触发有效
            type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
          }
        },
        grid: {
          left: '20',
          right: '20',
          bottom: '3',
          containLabel: true
        },
        xAxis: {
          type: 'category',
          data: [
            '血糖最高值',
            '血糖最低值',
            '空腹平均值',
            '餐前平均值',
            '餐后平均值'
          ]
        },
        yAxis: {},
        // Declare several bar series, each will be mapped
        // to a column of dataset.source by default.
        series: [
          {
            type: 'bar',
            name: 'mmol/L',
            data: [
              this.max_glucose,
              this.min_glucose,
              this.emp_glucose,
              this.before_glucose,
              this.after_glucose
              // this.sleep_glucose
            ],
            itemStyle: {
              normal: {
                //这里是重点
                color: function(params) {
                  //注意，如果颜色太少的话，后面颜色不会自动循环，最好多定义几个颜色
                  var colorList = [
                    '#c23531',
                    '#2f4554',
                    '#61a0a8',
                    '#d48265',
                    '#91c7ae',
                    '#749f83',
                    '#ca8622'
                  ]
                  return colorList[params.dataIndex]
                }
              }
            }
          }
        ]
      })
    },
    initEcharts() {
      this.PieCharts = echarts.init(this.$refs.PieCharts, 'macarons')
      this._setOption()
    },
    _setOption() {
      this.PieCharts.setOption({
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
              { value: this.above_time, name: '偏高天数' },
              { value: this.below_time, name: '偏低天数' },
              { value: this.normal_time, name: '正常天数' },
              {
                value:
                  this.showDays -
                  this.above_time -
                  this.below_time -
                  this.normal_time,
                name: '未测天数'
              }
            ],
            animationEasing: 'cubicInOut',
            animationDuration: 2600
          }
        ]
      })
    },
    testfunc() {
      window.alert(this.value)
    },
    getBarChartData: function(days) {
      var dataobj = {
        max: 0,
        min: 0,
        empty: 0,
        before: 0,
        after: 0,
        sleep: 0
      }
      var path = ''
      if (days === 7) {
        path = 'http://127.0.0.1:8000/get_week_statistics'
      }
      if (days === 30) {
        path = 'http://127.0.0.1:8000/get_month_statistics'
      }
      var configGet = {
        method: 'GET',
        url: path,
        headers: {
          'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
          'Content-Type': 'application/json'
        },
        data: dataobj
      }
      var self = this
      axios(configGet)
        .then(function(response) {
          console.log(response.data)
          if (response.status === 200) {
            console.log(response)
            // if successfully transfer data to front-end
            self.min_glucose = response.data['min']
            self.max_glucose = response.data['max']
            self.emp_glucose = response.data['av1']
            self.before_glucose =
              (response.data['av3'] + response.data['av5']) / 2
            self.after_glucose =
              (response.data['av2'] +
                response.data['av4'] +
                response.data['av6']) /
              3
            // self.sleep_glucose
          }
        })
        .catch(function(error) {
          console.log(error)
          if (error.response.status === 401) {
            window.alert('重复的用户名！')
          }
        })
    },
    getPieData: function(days) {
      var dataobj = {
        min: 0,
        max: 0,
        time: 0,
        av1: 0,
        av2: 0,
        av3: 0,
        av4: 0,
        av5: 0,
        av6: 0,
        normal_time: 0,
        above_time: 0,
        below_time: 0
      }
      var path = ''
      if (days === 7) {
        path = 'http://127.0.0.1:8000/get_week_statistics'
      }
      if (days === 30) {
        path = 'http://127.0.0.1:8000/get_month_statistics'
      }
      var configGet = {
        method: 'GET',
        url: path,
        headers: {
          'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
          'Content-Type': 'application/json'
        },
        data: dataobj
      }
      var self = this
      axios(configGet)
        .then(function(response) {
          console.log(response.data)
          if (response.status === 200) {
            // if successfully transfer data to front-end
            // if (days === 7) {
            //   self.showDays = 7
            // } else {
            //   self.showDays = 30
            // }
            var abv_time = response.data['above_time']
            var blw_time = response.data['below_time']
            var nor_time = response.data['normal_time']
            self.above_time = abv_time
            self.below_time = blw_time
            self.normal_time = nor_time
          }
        })
        .catch(function(error) {
          console.log(error)
          // eslint-disable-next-line no-empty
          if (error.response.status === 401) {
          }
        })
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
    },
    startInterval() {
      // 事件里定时器应该先清除在设置，防止多次点击直接生成多个定时器
      clearInterval(this.timer)
      this.timer = setInterval(() => {
        this.currentIndex++
        if (this.currentIndex > this.imgArr.length - 1) {
          this.currentIndex = 0
        }

        this.getTitle()
      }, 3000)
    },

    // 点击左右箭头
    clickIcon(val) {
      if (val === 'down') {
        this.currentIndex++
        if (this.currentIndex === this.imgArr.length) {
          this.currentIndex = 0
        }
      } else {
        /* 第一种写法
					this.currentIndex--;
					if(this.currentIndex < 0){
						this.currentIndex = this.imgArr.length-1;
					} */
        // 第二种写法
        if (this.currentIndex === 0) {
          this.currentIndex = this.imgArr.length
        }
        this.currentIndex--
      }

      this.getTitle()
    },
    // 点击控制圆点
    changeImg(index) {
      this.currentIndex = index
    },
    //鼠标移入移出控制
    changeInterval(val) {
      if (val) {
        clearInterval(this.timer)
      } else {
        this.startInterval()
      }
    },
    jumpToArticle(a) {
      if (a == null) {
        this.$router.push({
          name: 'article',
          params: {
            id: this.currentIndex + 1
          }
        })
      } else {
        this.$router.push({
          name: 'article',
          params: {
            id: a
          }
        })
      }
      window.location.reload()
    },
    getTitle() {
      var id = this.currentIndex + 1
      if (id == 1) {
        this.title = '糖尿病患者空腹血糖升高的8种常见原因及对策，糖友必学技能'
      } else if (id == 2) {
        this.title =
          '糖友朋友们，今天按这个顺序吃饭，看看你的餐后血糖可以降多少'
      } else if (id == 3) {
        this.title = '哪种水果糖分低？糖尿病友聪明控糖'
      } else if (id == 4) {
        this.title = '四招预防糖尿病肾病'
      }
    }
  }
}
</script>
<style scoped lang="scss">
$mgTop: 30px;
@mixin shadow {
  box-shadow: 0 0 10px #e2e2e2;
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

* {
  padding: 0;
  margin: 0;
}
/* 清除li前面的圆点 */
li {
  list-style-type: none;
}
.showImg {
  position: relative;
  width: 600px;
  height: 350px;
  margin: 100px;
  overflow: hidden;
  display: inline-block;
  vertical-align: top;
}
/* 轮播图片 */
.showImg img {
  width: 100%;
  height: 100%;
}
.articleBar {
  overflow: hidden;
  color: #36a3f7;
  width: auto;
  height: 100% auto;
  overflow: hidden;
  display: inline-block;
  vertical-align: top;
  margin-bottom: 100px;
}
.articleTitles {
  font-size: 16px;
}
.articleTitles:hover {
  background-color: rgb(241, 195, 109);
}

/* 箭头图标 */
.iconDiv {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 30px;
  height: 30px;
  border: 1px solid #666;
  border-radius: 15px;
  background-color: rgba(125, 125, 125, 0.2);
  line-height: 30px;
  text-align: center;
  font-size: 25px;
  cursor: pointer;
}
.iconDiv:hover {
  background-color: white;
}
.icon-left {
  left: 10px;
}
.icon-right {
  right: 10px;
}

/* 控制圆点 */
.banner-circle {
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 20px;
}
.banner-circle ul {
  margin: 0 50px;
  height: 100%;
  text-align: right;
}
.banner-circle ul li {
  display: inline-block;
  width: 14px;
  height: 14px;
  margin: 0 5px;
  border-radius: 7px;
  background-color: rgba(125, 125, 125, 0.8);
  cursor: pointer;
}
.active {
  background-color: black !important;
}

.mfont {
  font-size: large;
  font-family: Tahoma, sans-serif;
  color: #36a3f7;
}
</style>
