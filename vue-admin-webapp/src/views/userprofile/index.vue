<!-- eslint-disable prettier/prettier -->
<template>
  <div>
    <div class="profile_div">
      <h3 class="profile_info">账户信息</h3>
      <div class="profile_input">
        用户名：<input id="uname" v-model="username" disabled />
      </div>
      <div class="profile_input">
        邮箱：<input id="email" v-model="email" disabled />
      </div>
    </div>
    <div class="user_div">
      <h3 class="user_info">个人信息</h3>
      <div class="profile_input">
        性别：
        <input type="radio" name="gender" value="man" />男
        <input type="radio" name="gender" value="woman" />女
      </div>
      <div class="profile_input">
        出生年月：
        <el-date-picker
          v-model="birth"
          :picker-options="date_limit"
          type="month"
          placeholder="选择时间"
        />
      </div>
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
      email: null
    }
  },
  name: 'index.vue',
  computed: {},
  methods: {}
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
