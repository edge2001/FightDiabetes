<template>
  <div>
    <div class="item">
      <input
        type="text"
        v-model="name"
        placeholder="吃前查一查更健康"
        v-on:input="changetext"
      />
      <el-button type="primary" v-on:click="clickTest">查询</el-button>
    </div>
    <ul v-show="flag" class="item-ul">
      <li
        class="item-ul-li"
        v-for="(item, index) in nlist"
        :key="index"
        @click="queryadd(item)"
      >
        <span>{{ item.name }}</span>
      </li>
    </ul>
    <el-table :data="tableData">
      <el-table-column prop="name" label="食物" width="180"> </el-table-column>
      <el-table-column prop="calory" label="热量" width="180">
      </el-table-column>
      <el-table-column prop="sugar" label="糖分"> </el-table-column>
    </el-table>
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
      tableData: []
    }
  },
  methods: {
    changetext() {
      this.flag = false
    },
    queryadd(item) {
      this.url =
        '/api/food_heat/food/details?foodId=' +
        item.foodId +
        '&page=1&app_id=kjngvptstfopqhpk&app_secret=TnZTSkVuOUpsOERFMndoMnNvQ3pNUT09'
      console.log(this.url)
      axios
        .get(this.url)
        .then(response => {
          console.log(response.data['data']['name'])
          console.log(response.data['data']['calory'])
          console.log()
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
    clickTest() {
      this.url =
        '/api/food_heat/food/search?keyword=' +
        this.name +
        '&page=1&app_id=kjngvptstfopqhpk&app_secret=TnZTSkVuOUpsOERFMndoMnNvQ3pNUT09'
      console.log(this.url)
      axios
        .get(this.url)
        .then(response => {
          console.log(response.data['data']['list'][1])
          this.nlist = response.data['data']['list']
          console.log(this.nlist)
          this.flag = true
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
