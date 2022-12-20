<template>
  <div>
    <div class="button-area">
      <div class="button1">
        <!--        <div class="block">-->
        <!--          <div class="demonstration">运动打卡</div>-->

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
              <el-input
                type="textarea"
                :rows="1"
                v-model="questionFormSport.sport_type"
                placeholder="篮球"
              ></el-input>
            </el-form-item>
            <el-form-item label="备注" prop="notes" required="true">
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
              <el-input
                type="textarea"
                :rows="1"
                v-model="questionFormMedicine.medicine_type"
                placeholder="胰岛素"
              ></el-input>
            </el-form-item>
            <el-form-item label="用量(mg)" prop="quantity" required="true">
              <el-input
                type="textarea"
                :rows="1"
                v-model="questionFormMedicine.quantity"
                placeholder="20"
              ></el-input>
            </el-form-item>
            <el-form-item label="备注" prop="notes" required="true">
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
  </div>
</template>

<script>
/* eslint-disable */
import Calendar from 'vue-calendar-component';
import axios from "axios";
export default {
  components: {
    Calendar
  },
  data() {
    return {
      date: "",
      week: "",
      date_arr1:["2022/12/16"],
      date_arr2:["2022/12/17"],
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
  created() {
    var now = new Date();
    this.date = now.getDate();//得到日期
    var day = now.getDay();//得到周几
    var arr_week = new Array("星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六");
    this.week = arr_week[day];
  },
  methods: {
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
            alert('success')
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
            alert('success')
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

    },
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
  height: 300px;
}
.space {
  width: 20%
}
.space1 {
  width: 25%
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
