<template>
  <div>
    <div class="item">
      <input
        type="text"
        v-model="name"
        placeholder="吃前查一查更健康"
        v-on:input="changetext"
      />
      <el-button type="primary" v-on:click="clickT">查询</el-button>
    </div>
    <!-- <ul v-show="flag" class="item-ul">
      <li
        class="item-ul-li"
        v-for="(item, index) in nlist"
        :key="index"
        @click="queryadd(item)"
      >
        <span>{{ item.name }}</span>
      </li>
    </ul> -->
    <el-select
      v-model="foodId"
      value-key="foodId"
      @change="testfunc"
      ref="selectRef"
      class="selector"
    >
      <el-option
        v-for="item in nlist"
        :key="item.index"
        :label="item.name"
        :value="item.foodId"
      >
      </el-option>
    </el-select>
    <el-table :data="tableData">
      <el-table-column prop="name" label="食物" width="180"> </el-table-column>
      <el-table-column prop="calory" label="热量" width="180">
      </el-table-column>
      <el-table-column prop="sugar" label="糖分"> </el-table-column>
    </el-table>
    <!-- <el-select v-model="test" value-key="foodId">
      <el-option
        v-for="item in nlist"
        :label="item.name"
        :key="item.id"
        :value="item"
      ></el-option>
    </el-select> -->
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'index.vue',
  data() {
    return {
      flag: false,
      name: '',
      nlist: [],
      url: '',
      dict: {},
      tableData: [],
      finalList: [],
      tmpDataList: [],
      test: ''
    }
  },
  watch: {
    nlist: {
      deep: true,
      // eslint-disable-next-line no-unused-vars
      handler(val) {
        for (var i = 0; i < this.nlist.length; i++) {
          var tmpID = this.nlist[i]['foodId']
          this.url =
            '/api/food_heat/food/details?foodId=' +
            tmpID +
            '&page=1&app_id=kjngvptstfopqhpk&app_secret=TnZTSkVuOUpsOERFMndoMnNvQ3pNUT09'
          // console.log(this.url)
          axios
            .get(this.url)
            .then(response => {
              console.log(response.data)
              if (
                response.data['data']['sugar'] == '' ||
                response.data['data']['sugar'] == 0.0
              ) {
                alert(this.nlist[i]['name'])
              }
              var p = {
                name: response.data['data']['name'],
                calory: response.data['data']['calory'],
                sugar: response.data['data']['sugar']
              }

              this.tableData.push(p)
            })
            .catch(error => {
              console.log(error)
            })
        }
      }
    }
  },
  methods: {
    // eslint-disable-next-line no-unused-vars
    testfunc(event, item) {
      this.queryadd(event)
    },
    changetext() {
      this.flag = false
    },
    queryadd(foodId) {
      this.url =
        '/api/food_heat/food/details?foodId=' +
        foodId +
        '&page=1&app_id=kjngvptstfopqhpk&app_secret=TnZTSkVuOUpsOERFMndoMnNvQ3pNUT09'
      console.log(this.url)
      axios
        .get(this.url)
        .then(response => {
          // console.log(response.data['data']['name'])
          // console.log(response.data['data']['calory'])
          // console.log(response.data['data']['sugar'] == '')
          if (
            response.data['data']['sugar'] == '' ||
            response.data['data']['sugar'] == 0.0
          ) {
            alert('currently not support')
            return
          }
          var p = {
            name: response.data['data']['name'],
            calory: response.data['data']['calory'],
            sugar: response.data['data']['sugar']
          }

          this.tableData.push(p)
        })
        .catch(error => {
          console.log(error)
        })
    },
    clickT() {
      this.clickTest()
      this.$refs.selectRef.toggleMenu()
    },
    clickTest() {
      this.nlist = []
      this.url =
        '/api/food_heat/food/search?keyword=' +
        this.name +
        '&page=1&app_id=kjngvptstfopqhpk&app_secret=TnZTSkVuOUpsOERFMndoMnNvQ3pNUT09'
      console.log(this.url)
      axios
        .get(this.url)
        .then(response => {
          var usedNameList = []
          for (var i = 0; i < response.data['data']['list'].length; i++) {
            var tmpFoodObject = response.data['data']['list'][i]
            var isRepeated = 0
            for (var j = 0; j < usedNameList.length; j++) {
              if (tmpFoodObject['name'] == usedNameList[j]) {
                isRepeated = 1
                break
              }
            }
            if (isRepeated === 1) {
              continue
            } else {
              this.nlist.push(tmpFoodObject)
              this.nlist[i]['index'] = i
              usedNameList.push(tmpFoodObject['name'])
            }
          }
          this.flag = true
          this.tmpDataList = this.nlist
          for (var k = 0; k < this.nlist.length; k++) {
            // console.log(this.nlist[k])
          }
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>

<style scoped lang="scss">
.item {
  text-align: center;
  input {
    border: 2px solid #b8b8b8;
    height: 40px;
    width: 35%;
    font-size: 16px;
  }
  input:focus {
    border: 2px solid #3385ff;
  }
}
.item-ul {
  .item-ul-li {
    margin: auto;
    height: 30px;
    line-height: 30px;
    width: 35%;
    span {
      font-size: 16px;
    }
  }
  .item-ul-li:hover {
    background-color: #f1f3f4;
  }
}
</style>
