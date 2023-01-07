<template>
  <div class="tab-container">
    <div class="button_area">
      <el-button
        class="filter-item"
        style="margin-left: 10px;"
        type="primary"
        icon="el-icon-edit"
        @click="handleCreate"
        >添加健康数据记录</el-button
      >
    </div>
    <el-dialog :visible.sync="dialogFormVisible">
      <el-form
        :model="questionForm"
        ref="dataForm"
        label-position="left"
        label-width="90px"
        style="width: 400px; margin-left:50px;"
      >
        <el-form-item label="血糖含量" prop="glucose" required="true">
          <el-input
            type="textarea"
            :rows="1"
            v-model="questionForm.glucose"
            placeholder="mmol/L"
            oninput="value=value.replace(/^\.+|[^\d.]/g,'')"
          ></el-input>
        </el-form-item>
        <el-form-item label="体重" prop="weight">
          <el-input
            type="textarea"
            :rows="1"
            v-model="questionForm.weight"
            placeholder="kg"
            oninput="value=value.replace(/^\.+|[^\d.]/g,'')"
          ></el-input>
        </el-form-item>
        <el-form-item label="血酮" prop="ketone">
          <el-input
            type="textarea"
            :rows="1"
            v-model="questionForm.ketone"
            placeholder="mmol/L"
            oninput="value=value.replace(/^\.+|[^\d.]/g,'')"
          ></el-input>
        </el-form-item>
        <el-form-item label="血压(收缩压)" prop="ketone">
          <el-input
            type="textarea"
            :rows="1"
            v-model="questionForm.pressure"
            placeholder="mmHg"
            oninput="value=value.replace(/^\.+|[^\d.]/g,'')"
          ></el-input>
        </el-form-item>
        <el-form-item label="备注" prop="note">
          <el-input
            type="textarea"
            clearable
            :rows="1"
            v-model="questionForm.note"
            placeholder="记录此刻感受……"
          ></el-input>
        </el-form-item>
        <el-form-item label="测量时段" required="true">
          <el-select
            v-model="questionForm.measureTime"
            class="filter-item"
            placeholder="选择时段"
          >
            <el-option
              v-for="item in tabMapOptions"
              :key="item.key"
              :label="item.label"
              :value="item.key"
            />
          </el-select>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取消</el-button>
        <el-button type="primary" @click="createData()">确定</el-button>
      </div>
    </el-dialog>
    <el-select v-model="value" placeholder="请选择展示时间" show="false">
      <el-option
        v-for="item in options"
        :key="item.value"
        :label="item.label"
        :value="item.value"
      >
      </el-option>
    </el-select>
    <el-radio-group v-model="radio1" class="radio_class">
      <el-radio-button label="空腹血糖"></el-radio-button>
      <el-radio-button label="血酮"></el-radio-button>
      <el-radio-button label="血压"></el-radio-button>
      <el-radio-button label="体重"></el-radio-button>
    </el-radio-group>
    <div
      class="lineCharts"
      :style="{ width: width, height: height }"
      ref="myCharts"
    ></div>
    <div class="dashbord">
      <!-- <button @click="testfunc()"></button> -->
      <div>
        <el-row class="tableChart">
          <el-col :span="12">
            <div
              ref="PieCharts"
              :style="{ width: width, height: height }"
            ></div>
          </el-col>
          <el-col :span="12">
            <div
              ref="Barcharts"
              :style="{ width: width, height: height }"
            ></div>
          </el-col>
        </el-row>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
import echarts from 'echarts'
require('echarts/theme/macarons')
export default {
  props: {
    width: {
      type: String,
      default: '100%'
    },
    height: {
      type: String,
      default: '350px'
    },
    isGlucose: {
      type: Boolean
    }
  },
  data() {
    return {
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
      value: '',
      radio1: '空腹血糖',
      timeTag: 1,
      xAxisData: ['1', '2', '3'],
      lineChartData: {
        emptyGlucose: [],
        emptyGlucoseStandard: [6.1, 6.1, 6.1, 6.1, 6.1, 6.1, 6.1],
        ketone: [],
        ketoneStandard: [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        pressure: [],
        pressureStandard: [140, 140, 140, 140, 140, 140, 140],
        weight: []
      },
      mycharts: null,
      input: '',
      tabMapOptions: [
        { label: '空腹', key: '1' },
        { label: '早餐后', key: '2' },
        { label: '午餐前', key: '3' },
        { label: '午餐后', key: '4' },
        { label: '晚餐前', key: '5' },
        { label: '晚餐后', key: '6' }
      ],
      questionForm: {
        glucose: '',
        weight: '',
        ketone: '',
        pressure: '',
        note: '',
        time_tag: '',
        measureTime: [],
        questionCategory: ''
      },
      dialogFormVisible: false
    }
  },
  watch: {
    lineChartData: {
      deep: true,
      handler(val) {
        if (this.radio1 == '空腹血糖') {
          this._setOption(val.emptyGlucose, val.emptyGlucoseStandard)
        }
      }
    },
    radio1: {
      deep: true,
      handler(val) {
        if (this.radio1 == '空腹血糖') {
          this.lineChartData.emptyGlucose = []
          this.getData('glucose')
          this._setOption(
            this.lineChartData.emptyGlucose,
            this.lineChartData.emptyGlucoseStandard
          )
        } else if (this.radio1 == '血酮') {
          // this.lineChartData.ketone = []
          this.getData('ketone')
          this._setOption(
            this.lineChartData.ketone,
            this.lineChartData.ketoneStandard
          )
        } else if (this.radio1 == '血压') {
          this.lineChartData.pressure = []
          this.getData('pressure')
          this._setOption(
            this.lineChartData.pressure,
            this.lineChartData.pressureStandard
          )
          this.getPressureData()
        } else if (this.radio1 == '体重') {
          this.lineChartData.weight = []
          this.getData('weight')
          this._setOption(this.lineChartData.weight)
        }
      }
    }
  },
  mounted() {
    this.initEcharts()
    this.getData('glucose')
    this.getData('ketone')
    this.getData('pressure')
    this.getData('weight')
  },
  methods: {
    initEcharts() {
      this.mycharts = echarts.init(this.$refs.myCharts, 'macarons')
      this._setOption(
        this.lineChartData.emptyGlucose,
        this.lineChartData.emptyGlucoseStandard
      )
    },
    // eslint-disable-next-line no-unused-vars
    _setOption(inprice = [], outprice = []) {
      this.mycharts.setOption({
        title: {
          text: '近期健康数据',
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
        legend: {
          data: ['血糖', '体重']
        },
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
            data: this.xAxisData
          }
        ],
        yAxis: [
          {
            type: 'value'
          }
        ],
        series: [
          {
            name: '测量值',
            type: 'line',
            // areaStyle: {
            //   color: '#f4516c',
            //   opacity: 0.3
            // },
            itemStyle: {
              color: '#f4516c'
            },
            lineStyle: {
              color: '#f4516c'
            },
            smooth: true,
            data: inprice,
            animationDuration: 2800,
            animationEasing: 'quadraticOut'
          },
          {
            name: '标准值',
            type: 'line',
            areaStyle: {
              color: '#55a8fd',
              opacity: 0.3
            },
            itemStyle: {
              color: '#55a8fd'
            },
            lineStyle: {
              color: '#55a8fd'
            },
            smooth: true,
            data: outprice,
            animationDuration: 2800,
            animationEasing: 'quadraticOut'
          }
        ]
      })
    },
    getData(prop) {
      var dataobj = {
        time_tag: this.timeTag
      }
      var path = 'http://127.0.0.1:8000/get_week_glucose/'
      var configGet = {
        method: 'POST',
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
          if (response.status === 200) {
            let oneDay = 24 * 60 * 60 * 1000
            self.xAxisData = []
            var cnt2 = 0
            var cntdays = 0
            var m_data = response.data[prop]
            while (cnt2 < 90 && cntdays < 7) {
              var cur_datetime = new Date(Date.now() - oneDay * cnt2)
              var month = cur_datetime.getMonth() + 1
              var day = cur_datetime.getDate()
              var cur_datetime_str = month + '.' + day
              var isSelected = 0
              for (var j = 0; j < m_data.length; j++) {
                if (m_data[j][0] == month && m_data[j][1] == day) {
                  self.xAxisData.push(cur_datetime_str)
                  isSelected = 1
                }
              }
              if (isSelected == 1) {
                cntdays++
              }
              cnt2++
            }
            for (var ii = 0; ii < self.xAxisData.length / 2; ii++) {
              var tmp = self.xAxisData[ii]
              // eslint-disable-next-line prettier/prettier
              self.xAxisData[ii] =
                self.xAxisData[self.xAxisData.length - 1 - ii]
              self.xAxisData[self.xAxisData.length - 1 - ii] = tmp
            }
            if (prop == 'glucose') {
              for (var k = 0; k < response.data[prop].length; k++) {
                self.lineChartData.emptyGlucose.push(response.data[prop][k][2])
              }
            }
            if (prop == 'ketone') {
              for (var kk = 0; kk < response.data[prop].length; kk++) {
                self.lineChartData.ketone.push(response.data[prop][kk][2])
              }
              this._setOption(
                this.lineChartData.ketone,
                this.lineChartData.ketoneStandard
              )
            }
            if (prop == 'pressure') {
              for (var l = 0; l < response.data[prop].length; l++) {
                self.lineChartData.pressure.push(response.data[prop][l][2])
              }
              self._setOption(
                self.lineChartData.pressure,
                self.lineChartData.pressureStandard
              )
              // this._setOption([1, 2, 3], this.lineChartData.pressureStandard)
            }
            if (prop == 'weight') {
              console.log(response.data)
              for (var ll = 0; ll < response.data[prop].length; ll++) {
                self.lineChartData.weight.push(response.data[prop][ll][2])
              }
              self._setOption(self.lineChartData.weight)
              // this._setOption([1, 2, 3], this.lineChartData.pressureStandard)
            }
          }
        })
        .catch(function(error) {
          console.log(error)
          if (error.response.status === 401) {
            window.alert('重复的用户名！')
          }
        })
    },
    handleCreate() {
      this.questionForm = {
        glucose: '',
        weight: '',
        ketone: '',
        time_tag: '',
        note: '',
        measureTime: [],
        questionCategory: ''
      }
      this.dialogFormVisible = true
    },
    // post data
    async createData() {
      var dataobj = {
        blood_glucose: this.questionForm.glucose,
        time_tag: this.questionForm.measureTime[0],
        weight: this.questionForm.weight,
        ketone: this.questionForm.ketone,
        notes: this.questionForm.note,
        pressure: this.questionForm.pressure
      }
      const path = 'http://127.0.0.1:8000/add_datum/'
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
          if (response.status === 200) {
            this.xAxisData = response.data['glucose']
            this.initEcharts()
          }
        })
        .catch(function(error) {
          console.log(error)
          if (error.response.status === 401) {
            window.alert('重复的用户名！')
          }
        })
      this.dialogFormVisible = false
      // alert(params['glucose'])
    }
  }
}
</script>
<style scoped>
.lineCharts {
  margin-top: 10px;
}
.button_area {
  margin-bottom: 50px;
}
.radio_class {
  position: absolute;
  left: 45%;
}
</style>
