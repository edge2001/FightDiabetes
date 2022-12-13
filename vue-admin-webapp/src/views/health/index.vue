<template>
  <div class="tab-container">
    <el-button
      class="filter-item"
      style="margin-left: 10px;"
      type="primary"
      icon="el-icon-edit"
      @click="handleCreate"
      >添加</el-button
    >
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
        <el-form-item label="备注" prop="note">
          <el-input
            type="textarea"
            clearable
            :rows="1"
            v-model="questionForm.note"
            placeholder="记录此刻感受……"
          ></el-input>
        </el-form-item>
        <!-- <el-form-item label="分类">
          <el-radio-group
            v-model="questionForm.questionCategory"
            style="margin-right:12px;"
          >
            <el-radio
              v-for="(radio, index) in subjectList"
              :key="index"
              :label="radio"
              >{{ radio }}</el-radio
            >
          </el-radio-group>
        </el-form-item>
        <el-form-item label="正确答案" prop="correctAnswer">
          <el-input v-model="questionForm.correctAnswer" />
        </el-form-item>
        <el-form-item label="其他答案1" prop="otherAnswer1">
          <el-input v-model="questionForm.otherAnswer1" />
        </el-form-item>
        <el-form-item label="其他答案2" prop="otherAnswer2">
          <el-input v-model="questionForm.otherAnswer2" />
        </el-form-item>
        <el-form-item label="其他答案3" prop="otherAnswer3">
          <el-input v-model="questionForm.otherAnswer3" />
        </el-form-item> -->
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
  </div>
</template>
<script>
import axios from 'axios'
export default {
  data() {
    return {
      subjectList: ['黄金', '白银', '钻石'],
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
        note: '',
        time_tag: '',
        measureTime: [],
        questionCategory: ''
      },
      dialogFormVisible: false
    }
  },
  methods: {
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
      alert(this.questionForm.measureTime[0])
      var dataobj = {
        blood_glucose: this.questionForm.glucose,
        time_tag: this.questionForm.measureTime[0],
        weight: this.questionForm.weight,
        ketone: this.questionForm.ketone,
        notes: this.questionForm.note
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
          console.log(JSON.stringify(response.data))
          if (response.status === 200) {
            if (response.data['isrepeated'] == 1) {
              alert('你已覆盖此前填写过的数据')
            }
            // window.location.href = '/#/MainPage'
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
<style scoped></style>
