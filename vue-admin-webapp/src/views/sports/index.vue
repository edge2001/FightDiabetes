<template>
  <div>
    <div class="button-area">
      <div class="button1">
        <el-button
          class="filter-item"
          style="margin-left: 10px;"
          type="primary"
          icon="el-icon-basketball"
          @click="handleCreateSports"
          >运动打卡</el-button
        >
        <el-dialog :visible.sync="dialogFormVisible1">
          <el-form
            :model="questionFormSport"
            ref="dataForm"
            label-position="left"
            label-width="90px"
            style="width: 400px; margin-left:50px;"
          >
            <el-form-item label="运动种类" prop="sport_type" required="true">
              <el-cascader
                v-model="questionFormSport.sport_type"
                :options="options"
                @change="handleChange"
              ></el-cascader>
            </el-form-item>
            <el-form-item label="备注" prop="notes">
              <el-input
                type="textarea"
                v-model="questionFormSport.notes"
              ></el-input>
            </el-form-item>
            <el-form-item label="时间" prop="datetime" required="true">
              <el-date-picker
                v-model="questionFormSport.datetime"
                type="datetime"
                placeholder="选择日期时间"
              >
              </el-date-picker>
            </el-form-item>
          </el-form>
          <div slot="footer" class="dialog-footer">
            <el-button @click="dialogFormVisible1 = false">取消</el-button>
            <el-button type="primary" @click="createSportsData()"
              >确定</el-button
            >
          </div>
        </el-dialog>
      </div>
      <div class="space1"></div>
      <div class="button1">
        <el-button
          class="filter-item"
          style="margin-left: 10px;"
          type="primary"
          icon="el-icon-coffee-cup"
          @click="handleCreateMedicine"
          >用药打卡</el-button
        >
        <el-dialog :visible.sync="dialogFormVisible2">
          <el-form
            :model="questionFormMedicine"
            ref="dataForm"
            label-position="left"
            label-width="90px"
            style="width: 400px; margin-left:50px;"
          >
            <el-form-item label="用药种类" prop="medicine_type" required="true">
              <el-cascader
                v-model="questionFormMedicine.medicine_type"
                :options="options"
                @change="handleChange"
              ></el-cascader>
            </el-form-item>
            <el-form-item label="用量(mg)" prop="quantity" required="true">
              <el-input
                type="textarea"
                :rows="1"
                v-model="questionFormMedicine.quantity"
                placeholder="20"
                oninput="value=value.replace(/^\.+|[^\d.]/g,'')"
              ></el-input>
            </el-form-item>
            <el-form-item label="备注" prop="notes">
              <el-input
                type="textarea"
                v-model="questionFormMedicine.notes"
              ></el-input>
            </el-form-item>
            <el-form-item label="时间" prop="datetime" required="true">
              <el-date-picker
                v-model="questionFormMedicine.datetime"
                type="datetime"
                placeholder="选择日期时间"
              >
              </el-date-picker>
            </el-form-item>
          </el-form>
          <div slot="footer" class="dialog-footer">
            <el-button @click="dialogFormVisible2 = false">取消</el-button>
            <el-button type="primary" @click="createMedicineData"
              >确定</el-button
            >
          </div>
        </el-dialog>
      </div>
    </div>
    <div class="vertical-space"></div>

    <div class="con">
      <div class="calendar1">
        <div class="now-data-myself">
          <div class="now-data-myself-time">{{ date }}</div>
          <div class="now-data-myself-week">{{ week }}</div>
        </div>
        <Calendar
          v-on:choseDay="clickDay"
          :markDate="date_arr1"
          v-on:changeMonth="changeDate"
          v-on:isToday="clickToday"
        ></Calendar>
      </div>
      <div class="space"></div>
      <div class="calendar1">
        <div class="now-data-myself">
          <div class="now-data-myself-time">{{ date }}</div>
          <div class="now-data-myself-week">{{ week }}</div>
        </div>
        <Calendar
          v-on:choseDay="clickDay"
          :markDate="date_arr2"
          v-on:changeMonth="changeDate"
          v-on:isToday="clickToday"
        ></Calendar>
      </div>
    </div>
    <div class="charts">
      <el-row class="tableChart">
        <el-col :span="12">
          <!-- <bar-charts class="barCharts" :barData="barData"></bar-charts> -->
          <div ref="Barcharts" :style="{ width: width, height: height }"></div>
        </el-col>
        <el-col :span="12">
          <!-- <pie-charts class="pieCharts"></pie-charts> -->
          <div ref="PieCharts" :style="{ width: width, height: height }"></div>
        </el-col>
        <!-- <el-col :span="16">
                <bar-charts class="barCharts" :barData="barData"></bar-charts>
              </el-col> -->
      </el-row>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import Calendar from 'vue-calendar-component';
import PieCharts from '../dashboard/admin/components/PieCharts'
import BarCharts from '../dashboard/admin/components/BarCharts'
import echarts from 'echarts'
import resize from '../../mixins/resize'
require('echarts/theme/macarons') // echarts theme
import axios from "axios";
import { stringify } from 'zrender/lib/tool/color';
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
  components: {
    Calendar,
    PieCharts,
  },
  data() {
    return {
      PieCharts: null,
      Barcharts: null,
      value: [],
      options: [{
        value: 'mouth',
        label: '口服',
        children: [
          {
            value: 'type1',
            label: '双胍类'
          }, {
            value: 'type2',
            label: '促胰岛素分泌剂'
          }, {
            value: 'type3',
            label: '胰岛素增敏剂'
          },
          {
            value: 'others',
            label: '其他'
          },
        ]
      },
      {
        value: 'injection',
        label: '注射',
        children: [
          {
            value: 'type1',
            label: '胰岛素'
          },
          {
            value: 'others',
            label: '其他注射剂'
          }
        ]
      }

      ],
      date: "",
      week: "",
      date_arr1:[],
      date_arr2:[],
      dialogFormVisible1 : false,
      dialogFormVisible2 : false,
      questionFormSport : {
        sport_type: '',
        notes: '',
        datetime: ''
      },
      questionFormMedicine : {
        medicine_type: '',
        notes: '',
        quantity: '',
        datetime: '',
      }
    };
  },
  mounted() {
    this.getMedicineData()
    this.getSportsData()
    this.initEcharts()
    this.initBarChart()
  },
  created() {
    var now = new Date();
    this.date = now.getDate();//得到日期
    var day = now.getDay();//得到周几
    var arr_week = new Array("星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六");
    this.week = arr_week[day];
  },
  methods: {
    initBarChart() {
      this.Barcharts = echarts.init(this.$refs.Barcharts, 'macarons')
      this._setBarOption()
    },
    _setBarOption() {
      this.Barcharts.setOption({
        title: {
          text: '运动统计',
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
            '本周运动次数',
            '上周运动次数',
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
                color: function (params) {
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
    clickDay(data) {
      console.log(data); //选中某天
    },
    changeDate(data) {
      console.log(data); //左右点击切换月份
    },
    clickToday(data) {
      console.log(data); // 跳到了本月
    },
    handleCreateSports() {
      this.questionFormSport = {
        sport_type: '',
        notes: '',
        datetime: ''
      }
      this.dialogFormVisible1 = true
    },
    handleCreateMedicine() {
      this.questionFormMedicine = {
        medicine_type: '',
        notes: '',
        quantity: '',
        datetime: '',
      }
      this.dialogFormVisible2 = true
    },

    async createSportsData() {
      var dataobj = {
        sport_type: this.questionFormSport.sport_type,
        notes: this.questionFormSport.notes,
        datetime: this.questionFormSport.datetime
      }
      const path = 'http://127.0.0.1:8000/add_sports_record/'
      var configGet = {
        method: 'POST',
        url: path,
        headers: {
          'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
          'Content-Type': 'application/json'
        },
        data: dataobj
      }
      axios(configGet)
        .then(function(response) {
          console.log(JSON.stringify(response.data))
          if (response.status === 200) {
            // alert('success')
          }
        })
        .catch(function(error) {
          console.log(error)
          if (error.response.status === 401) {
            window.alert('wrong!')
          }
        })
      this.dialogFormVisible1 = false
      // alert(params['glucose'])
      location.reload()
    },

    async createMedicineData() {
      var dataobj = {
        medicine_type: this.questionFormMedicine.medicine_type,
        notes: this.questionFormMedicine.notes,
        datetime: this.questionFormMedicine.datetime,
        quantity: this.questionFormMedicine.quantity
      }
      const path = 'http://127.0.0.1:8000/add_medicine_record/'
      var configGet = {
        method: 'POST',
        url: path,
        headers: {
          'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
          'Content-Type': 'application/json'
        },
        data: dataobj
      }
      axios(configGet)
        .then(function(response) {
          console.log(JSON.stringify(response.data))
          if (response.status === 200) {
            // alert('success')
          }
        })
        .catch(function(error) {
          console.log(error)
          if (error.response.status === 401) {
            window.alert('wrong!')
          }
        })
      this.dialogFormVisible2 = false
      // alert(params['glucose'])
      location.reload()
    },
    getSportsData: function () {
      var path = 'http://127.0.0.1:8000/get_sports_data/'
      var configGet = {
        method: 'GET',
        url: path,
        headers: {
          'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
          'Content-Type': 'application/json'
        },
      }
      var self = this
      axios(configGet)
        .then(function(response) {
          if (response.status === 200) {
            self.date_arr1 = response.data['dates']
            for (var i = 0; i < self.date_arr1.length; i++) { // for each date string
              var j = 0
              var cnt = 0
              while (cnt < 1) {
                if (self.date_arr1[i][j] === '/') {
                  cnt++
                }
                j++
              }
              var yearnum = ''
              for (var k = j; k < self.date_arr1[i].length; k++) {
                datenum += self.date_arr1[i][k]
              }
            }
          }
        })
        .catch(function(error) {
          console.log(error)
          window.alert('error!')
        })
    },
    getMedicineData : function() {
      var path = 'http://127.0.0.1:8000/get_medicine_data/'
      var configGet = {
        method: 'GET',
        url: path,
        headers: {
          'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
          'Content-Type': 'application/json'
        },
      }
      var self = this
      axios(configGet)
        .then(function(response) {
          if(response.status ===200) {
            self.date_arr2 = response.data['dates']
          }
        })
        .catch(function(error) {
          console.log(error)
          window.alert('error!')
        })
    }
  }
}
</script>
 
<style>
.now-data-myself {
  width: 40%;
  position: absolute;
  border-right: 1px solid rgba(227, 227, 227, 0.6);
}
.con {
  /*display: flex;*/
  position: relative;
  display:flex;
  justify-content:center;
  /*max-width: 280px;*/
  margin: auto;
}
.button-area {
  position: relative;
  display:flex;
  justify-content:center;
  /*max-width: 280px;*/
  margin: auto;
}
.vertical-space {
  height: 100px;
}
.space {
  width: 20%
}
.space1 {
  width: 250px
}
.calendar1 {
  display: inline-block;
}
.con .wh_content_all {
  background: transparent !important;
}
.wh_top_changge li {
  color: #F56C6C !important;
  font-size: 15px !important;
}
.wh_content_item, .wh_content_item_tag {
  color: #303133 !important;
}
.wh_content_item .wh_isToday {
  background: #00d985  !important;
  color: #fff  !important;
}
.wh_content_item .wh_chose_day {
  background: #409EFF  !important;
  color: #ffff  !important;
}
.wh_item_date:hover {
    background: rgb(217, 236, 255) !important;
    border-radius: 100px !important;
    color: rgb(102, 177, 255)  !important;
}
.wh_jiantou1[data-v-2ebcbc83] {
    border-top: 2px solid #909399;
    border-left: 2px solid #909399;
    width: 7px;
    height: 7px;
}
.wh_jiantou2[data-v-2ebcbc83] {
    border-top: 2px solid #909399;
    border-right: 2px solid #909399;
    width: 7px;
    height: 7px;
}
.wh_top_tag[data-v-2ebcbc83] {
  color: #409EFF;
  border-top: 1px solid rgba(227, 227, 227, 0.6);
  border-bottom: 1px solid rgba(227, 227, 227, 0.6);
}
.wh_container[data-v-2ebcbc83] {
    max-width: 280px;
}
.wh_top_changge[data-v-2ebcbc83] {
    display: flex;
    width: 50%;
    margin-left: 43%;
}
.now-data-myself-time {
  color: #F56C6C;
  font-size: 28px;
  height: 30px;
  font-family: "Helvetica Neue";
}
.now-data-myself-week {
  font-size: 10px;
  color: #909399;
}
.wh_top_changge .wh_content_li[data-v-2ebcbc83] {
  font-family: Helvetica;
}
</style>
