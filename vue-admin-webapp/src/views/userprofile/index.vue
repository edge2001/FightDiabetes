<!-- eslint-disable prettier/prettier -->
<template>
  <div>
      <div class="profile_div">
        <h3 class="profile_info">账户信息</h3>
        <div class="profile_input">
          用户名：<input :disabled="profile" id="uname" v-model="username" />
        </div>
        <div class="profile_input">
          邮箱：<input :disabled="profile" id="email" v-model="email" />
        </div>
      </div>
      <div class="user_div">
        <h3 class="user_info">个人信息</h3>
        <div class="profile_input">
          性别：
          <input  :disabled="profile" type="radio" name="gender" value="man" />男
          <input :disabled="profile" type="radio" name="gender" value="woman" />女
        </div>
        <div class="profile_input">
          出生年月：
          <el-date-picker
            :disabled="profile"
            v-model="birth"
            :picker-options="date_limit"
            type="month"
            placeholder="选择时间"
          />
        </div>
      </div>
    <div>
      <button id="modify" v-text="modifyOrSave" @click="modify"></button>
    </div>
    </div>
</template>

<script>
export default {
  data() {
    return {
      birth: null,
      date_limit: {
        disabledDate(time) {
          return time.getTime() > Date.now() - 8.64e6
        }
      },
      username: null,
      email: null,
      modifyOrSave: '修改',
      profile:true
    }
  },
  name: 'index.vue',
  computed: {},
  methods: {
    modify() {
      if(this.modifyOrSave=='修改'){
        this.modifyOrSave='保存';
        this.profile=false;
      }
      else{
        this.modifyOrSave='修改';
        this.profile=true;
        //TODO:axios() 后端修改
      }

    }
  },
  mounted() {
    this.username = localStorage.getItem('username')
    this.email = localStorage.getItem('email')
  }
}
</script>

<style scoped>
.profile_info {
  color: blue;
  font-size: 3em;
}
.user_info {
  color: green;
  font-size: 3em;
}
h3 {
  height: 2em;
}
.profile_input {
  margin: 5px;
  font-size: 1.5em;
}
</style>
