<template>
  <div class="notificatBar">
    <div class="cardBox">
      <div class="cardHead">
        <p>消息中心</p>
        <i
          class="el-icon-close"
          @click="$store.commit('app/SET_MSGISOPEN')"
        ></i>
      </div>
      <ul class="conUl">
        <li v-for="item in msgList" :key="item.id">
          <router-link
            :to="item.link"
            @click.native="showMsg(item.time)"
            class="conUl_link"
          >
            <span class="conUl_sp0">{{ item.content }}</span>
            <span class="conUl_sp1">{{ item.time }}</span>
          </router-link>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import index from '../../../src/layout/components/header/index'
import axios from 'axios'
export default {
  data() {
    return {
      msgList: [],
      msgNum: 0,
      medicineTime: []
    }
  },

  mounted() {
    axios
      .get('http://127.0.0.1:8000/getMedicineTime/')
      .then(response => {
        this.medicineTime = response.data['list']
        console.log(this.medicineTime)
      })
      .catch(error => {
        console.log(error)
      }),
      this.$nextTick(() => {
        setInterval(this.checkMedicineTime, 540000)
      })
  },

  methods: {
    checkMedicineTime() {
      let now = new Date()
      let nowhours = now.getHours()
      let nowmin = now.getMinutes()
      for (var i = 0, len = this.medicineTime.length; i < len; i++) {
        if (nowhours == this.medicineTime[i]['hour']) {
          console.log('时')
          if (Math.abs(this.medicineTime[i]['minute'] - nowmin) < 5) {
            this.msgNum = this.msgNum + 1
            console.log('提醒吃药')
            this.msgList.push({
              id: this.msgNum,
              content: '提醒您按时吃药！',
              link: '',
              time: nowhours + '时' + nowmin + '分'
            })
            index.methods.red()
          }
        }
      }
    },
    showMsg(time) {
      this.$alert('我已经按时服药', '服药提醒', {
        confirmButtonText: '确定'
      })
    }
  }
}
</script>
<style lang="scss">
.cardBox {
  width: 100%;
  .cardHead {
    height: 50px;
    padding: 0 20px;
    border-bottom: 1px solid #e4e4e4;
    line-height: 50px;
    p {
      font-size: 16px;
      color: #333;
      float: left;
    }
    i {
      float: right;
      font-size: 20px;
      margin-top: 14px;
      color: #b3b3b3;
      cursor: pointer;
      transition: all 0.2s;
      &:hover {
        color: #333;
      }
    }
  }
}
.conUl {
  li {
    height: 50px;
    line-height: 50px;
    .conUl_link {
      display: block;
      margin: 0 20px;
      height: 100%;
      border-bottom: 1px solid #e4e4e4;
    }
    .conUl_sp0 {
      font-size: 14px;
    }
    .conUl_sp1 {
      font-size: 12px;
      color: #b3b3b3;
      float: right;
    }
  }
}
</style>
