<template>
  <div>
    <div class="main">
      <!-- <div class="header">
        <h1>登录或创建一个免费帐户！</h1>
      </div> -->
      <!-- <p></p> -->
      <form>
        <ul class="left-form">
          <h2>个人基本信息:</h2>
          <h3>username</h3>
          <li>
            <input
              type="text"
              placeholder="Username"
              v-model="username"
              required
            />
            <a href="#" class="icon ticker"> </a>
            <div class="clear"></div>
          </li>
          <h3>email</h3>
          <li>
            <input type="text" placeholder="Email" v-model="email" required />
            <a href="#" class="icon ticker"> </a>
            <div class="clear"></div>
          </li>
          <!-- <h3>gender</h3> -->
          <!-- <li>
            <el-date-picker
              :disabled="profile"
              v-model="birth"
              :picker-options="date_limit"
              type="month"
              placeholder="选择时间"
            />
            <div class="clear"></div>
          </li> -->
          <!-- <label class="checkbox"
            ><input type="checkbox" name="checkbox" checked="" /><i> </i>Please
            inform me of upcoming w3layouts, Promotions and news</label
          > -->
          <input type="submit" onClick="myFunction()" value="保存" />
          <div class="clear"></div>
        </ul>
        <ul class="right-form">
          <h2>gender</h2>
          <!-- <h3>gender</h3> -->
          <li class="gender">
            <!-- <input type="password" placeholder="password" required /> -->
            <a href="#" class="icon into"> </a>
            <input
              :disabled="profile"
              type="radio"
              name="gender"
              value="man"
            />男
            <input
              :disabled="profile"
              type="radio"
              name="gender"
              value="woman"
            />女
            <div class="clear"></div>
          </li>
          <h2>birthday</h2>
          <li>
            <el-date-picker
              :disabled="profile"
              v-model="birth"
              :picker-options="date_limit"
              type="month"
              class="profile_input"
              placeholder="选择时间"
            />
          </li>
          <div class="clear"></div>
        </ul>
        <div class="clear"></div>
      </form>
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
      profile: false
    }
  },
  name: 'index.vue',
  computed: {},
  methods: {
    modify() {
      if (this.modifyOrSave == '修改') {
        this.modifyOrSave = '保存'
        this.profile = false
      } else {
        this.modifyOrSave = '修改'
        this.profile = true
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

<style>
.gender {
  margin-bottom: 100px;
}
.profile_input {
  margin-top: 100px;
  font-size: 1.5em;
  text-align: right;
}
html,
body,
div,
span,
applet,
object,
iframe,
h1,
h2,
h3,
h4,
h5,
h6,
p,
blockquote,
pre,
a,
abbr,
acronym,
address,
big,
cite,
code,
del,
dfn,
em,
img,
ins,
kbd,
q,
s,
samp,
small,
strike,
strong,
sub,
sup,
tt,
var,
b,
u,
i,
dl,
dt,
dd,
ol,
nav ul,
nav li,
fieldset,
form,
label,
legend,
table,
caption,
tbody,
tfoot,
thead,
tr,
th,
td,
article,
aside,
canvas,
details,
embed,
figure,
figcaption,
footer,
header,
hgroup,
menu,
nav,
output,
ruby,
section,
summary,
time,
mark,
audio,
video {
  margin: 0;
  padding: 0;
  border: 0;
  font-size: 100%;
  font: inherit;
  vertical-align: baseline;
}

article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
menu,
nav,
section {
  display: block;
}

ol,
ul {
  list-style: none;
  margin: 0px;
  padding: 0px;
}

blockquote,
q {
  quotes: none;
}

blockquote:before,
blockquote:after,
q:before,
q:after {
  content: '';
  content: none;
}

table {
  border-collapse: collapse;
  border-spacing: 0;
}

a {
  text-decoration: none;
}

.txt-rt {
  text-align: right;
}

.txt-lt {
  text-align: left;
}

.txt-center {
  text-align: center;
}

.float-rt {
  float: right;
}

.float-lt {
  float: left;
}

.clear {
  clear: both;
}

.pos-relative {
  position: relative;
}

.pos-absolute {
  position: absolute;
}

.vertical-base {
  vertical-align: baseline;
}

.vertical-top {
  vertical-align: top;
}

nav.vertical ul li {
  display: block;
}

nav.horizontal ul li {
  display: inline-block;
}

img {
  max-width: 100%;
}

body {
  background: #eee;
  font-family: 'HelveticaNeue', 'Helvetica Neue', Helvetica, Arial, sans-serif;
}

.main {
  margin: 7em auto 0;
  width: 80%;
  background: #fff;
}

.header h1 {
  color: #272727;
  font-weight: 700;
  font-size: 22px;
}

.main p {
  text-align: center;
  font-size: 15px;
  font-weight: 600;
  color: #383737;
  padding: 20px 30px;
  border-bottom: 1px solid #e7e0e0;
  margin-top: -13px;
}

.main h2,
.main h3 {
  text-align: left;
  font-size: 17px;
  font-weight: 600;
  margin: 15px 3px;
  color: #3f3d3d;
}

.left-form,
.right-form {
  float: left;
  margin: 22px 28px;
  width: 40%;
}

.left-form input[type='text'],
.left-form input[type='email'],
.left-form input[type='password'] {
  float: left;
  font-family: 'HelveticaNeue', 'Helvetica Neue', Helvetica, Arial, sans-serif;
  width: 80%;
  padding: 0.7em 2em 0.7em 1em;
  border: none;
  color: #000;
  font-size: 15px;
  float: left;
  outline: none;
}

.right-form {
  margin-top: 60px;
  float: right;
}

form {
  padding-bottom: 2em;
}

.right-form li {
  display: block;
  color: #4d4949;
  border: 1px solid #ebebeb;
  border-radius: 0.3em;
  -webkit-border-radius: 0.3em;
  -moz-border-radius: 0.3em;
  -o-border-radius: 0.3em;
  margin-bottom: 10px;
}

.right-form input[type='text'],
input[type='password'] {
  font-family: 'HelveticaNeue', 'Helvetica Neue', Helvetica, Arial, sans-serif;
  width: 90%;
  padding: 0.7em 1em 0.7em 1em;
  color: #000;
  font-size: 15px;
  border: none;
  outline: none;
}

.left-form li {
  display: block;
  color: #4d4949;
  border: 1px solid #ebebeb;
  border-radius: 0.3em;
  -webkit-border-radius: 0.3em;
  -moz-border-radius: 0.3em;
  -o-border-radius: 0.3em;
  margin-bottom: 10px;
}

.icon {
  height: 28px;
  width: 28px;
  background: url(./images/spirit.png) no-repeat;
  display: block;
  float: right;
  margin: 7px 9px 9px 0px;
}

.ticker {
  background: url(./images/spirit.png) no-repeat 0px 0px;
}

.into {
  background: url(./images/spirit.png) no-repeat -31px 0px;
}

.left-form submit {
  float: left;
}

.right-form submit {
  float: right;
}

.main h4 {
  float: left;
  font-size: 13px;
  font-weight: 600;
  color: #363535;
}

.left-form input[type='submit'] {
  padding: 10px 19px;
  border-radius: 0.3em;
  -webkit-border-radius: 0.3em;
  -moz-border-radius: 0.3em;
  -o-border-radius: 0.3em;
  color: #4d4949;
  background: #f3f3f3;
  border: 1px solid #ebebeb;
  font-weight: bold;
  font-size: 15px;
  outline: none;
  transition: all 0.5s ease-out;
  -webkit-transition: all 0.5s ease-out;
  -moz-transition: all 0.5s ease-out;
  -ms-transition: all 0.5s ease-out;
  -o-transition: all 0.5s ease-out;
  margin-top: 15px;
  cursor: pointer;
}

.right-form input[type='submit'] {
  float: left;
  padding: 8px 19px;
  border-radius: 0.3em;
  border: none;
  outline: none;
  -webkit-border-radius: 0.3em;
  -moz-border-radius: 0.3em;
  -o-border-radius: 0.3em;
  font-weight: bold;
  font-size: 15px;
  transition: all 0.5s ease-out;
  -webkit-transition: all 0.5s ease-out;
  -moz-transition: all 0.5s ease-out;
  -ms-transition: all 0.5s ease-out;
  -o-transition: all 0.5s ease-out;
  margin: 2em -9em;
  cursor: pointer;
}

input[type='submit']:hover {
  background: #2e2d2d;
  color: #fff;
}

.uncheked {
  height: 40px;
  width: 28px;
  display: block;
  background: url(./images/check-icon.png) no-repeat;
}

.cheked {
  height: 40px;
  width: 28px;
  display: block;
  background: url(./images/check-icon.png) no-repeat 50% 50%;
}

.disabled {
  height: 40px;
  width: 28px;
  display: block;
  background: url(./images/check-icon.png) no-repeat 0% 100%;
}

.price-selection-tree input[type='checkbox'] {
  display: none;
}

.price-selection-tree input[type='checkbox'] + label {
  float: left;
  display: block;
  /* vertical-align: top; */
  font-size: 13px;
  font-weight: 600;
  margin-top: -0.3em;
  height: 76px;
  cursor: pointer;
}

.checkbox-grid-left p {
  display: block;
}

.left-form > label {
  font-size: 13px;
  float: left;
  vertical-align: super;
  margin-left: 10px;
  color: #4c4a4a;
  margin-top: 2px;
  font-weight: 600;
}

input[type='checkbox'].css-checkbox10 + label i.css-label10 {
  /* float: left; */
  height: 40px;
  width: 28px;
  display: inline-block;
  line-height: 18px;
  background-repeat: no-repeat;
  background-position: 0 0px;
  cursor: pointer;
  background: url(./images/check-icon.png) no-repeat -0px -82px;
}

input[type='checkbox'].css-checkbox10:checked + label i.css-label10 {
  background: url(./images/check-icon.png) no-repeat -0px -82px;
  height: 20px;
}

.copy-right {
  text-align: center;
}

.copy-right p {
  color: #000;
  font-size: 1em;
  margin-top: 5em;
  font-weight: 600;
}

.copy-right p a {
  font-size: 1em;
  font-weight: 600;
  color: #669a16;
  -webkit-transition: all 0.3s ease-out;
  -moz-transition: all 0.3s ease-out;
  -ms-transition: all 0.3s ease-out;
  -o-transition: all 0.3s ease-out;
  transition: all 0.3s ease-out;
}

.copy-right a:hover {
  color: #000;
}

@media only screen and (max-width: 1680px) and (min-width: 1440px) {
  .main {
    width: 70%;
    margin: 6em auto 0;
  }

  .copy-right p {
    margin: 3.5em 0em;
  }
}

@media only screen and (max-width: 1440px) and (min-width: 1366px) {
  .main {
    width: 80%;
    margin: 6em auto 0;
  }

  .copy-right p {
    margin: 3.8em 0em;
  }
}

@media only screen and (max-width: 1366px) and (min-width: 1280px) {
  .main {
    width: 82%;
    margin: 6em auto 0;
  }

  .copy-right p {
    margin: 4em 0em;
  }
}

@media only screen and (max-width: 1280px) and (min-width: 1024px) {
  .main {
    width: 89%;
    margin: 5em auto 0;
  }

  .copy-right p {
    margin: 3.5em 0em;
  }
}

@media only screen and (max-width: 1024px) and (min-width: 768px) {
  .main {
    width: 97%;
    margin: 5em auto 0;
  }

  .left-form input[type='text'],
  .left-form input[type='email'],
  .left-form input[type='password'] {
    font-family: 'HelveticaNeue', 'Helvetica Neue', Helvetica, Arial, sans-serif;
    width: 78%;
  }

  .right-form input[type='text'],
  input[type='password'] {
    font-family: 'HelveticaNeue', 'Helvetica Neue', Helvetica, Arial, sans-serif;
    width: 86%;
  }

  .copy-right p {
    margin: 3.5em 0em;
  }
}

@media only screen and (max-width: 768px) and (min-width: 640px) {
  .main {
    width: 95%;
    margin: 5em auto 0;
  }

  .left-form input[type='text'],
  .left-form input[type='email'],
  .left-form input[type='password'] {
    font-family: 'HelveticaNeue', 'Helvetica Neue', Helvetica, Arial, sans-serif;
    padding: 0.7em 1em 0.7em 1em;
    width: 70%;
  }

  .right-form input[type='text'],
  input[type='password'] {
    font-family: 'HelveticaNeue', 'Helvetica Neue', Helvetica, Arial, sans-serif;
    padding: 0.7em 1em 0.7em 0em;
    width: 89%;
  }

  .left-form {
    width: 88%;
    text-align: center;
  }

  .right-form {
    float: none;
    width: 88%;
    text-align: center;
  }

  .left-form > label {
    margin-left: 42px;
    margin-top: 13px;
  }

  .main h2,
  .main h3 {
    text-align: center;
  }

  .left-form li {
    margin-left: 32px;
  }

  .right-form li {
    margin-left: 40px;
  }

  .left-form input[type='submit'] {
    padding: 12px 12px;
    float: right;
    margin: 2px 0px;
  }

  .main h4 {
    float: left;
    margin: 7px 36px;
  }

  .main h3 {
    margin-top: -2em;
  }

  .right-form input[type='submit'] {
    float: right;
    padding: 8px 19px;
    margin: 2px 3px;
  }

  .copy-right p {
    margin: 3.5em 0em;
  }
}

@media only screen and (max-width: 640px) and (min-width: 480px) {
  .main {
    width: 95%;
    margin: 5em auto 0;
  }

  .left-form input[type='text'],
  .left-form input[type='email'],
  .left-form input[type='password'] {
    font-family: 'HelveticaNeue', 'Helvetica Neue', Helvetica, Arial, sans-serif;
    padding: 0.7em 1em 0.7em 1em;
    width: 70%;
  }

  .right-form input[type='text'],
  input[type='password'] {
    font-family: 'HelveticaNeue', 'Helvetica Neue', Helvetica, Arial, sans-serif;
    padding: 0.7em 1em 0.7em 0em;
    width: 89%;
  }

  .left-form {
    width: 88%;
    text-align: center;
  }

  .right-form {
    float: none;
    width: 88%;
    text-align: center;
  }

  .left-form > label {
    margin-left: 42px;
    margin-top: 13px;
  }

  .main h2,
  .main h3 {
    text-align: center;
  }

  .left-form li {
    margin-left: 13px;
  }

  .right-form li {
    margin-left: 16px;
  }

  .left-form input[type='submit'] {
    padding: 12px 12px;
    text-align: center;
    float: none;
  }

  .main h4 {
    float: left;
    margin: 7px 17px;
  }

  .right-form input[type='submit'] {
    float: right;
    padding: 8px 19px;
    margin: 2px 3px;
  }

  .copy-right p {
    margin: 3.5em 0em;
  }
}

@media only screen and (max-width: 480px) and (min-width: 320px) {
  .main {
    width: 95%;
    margin: 2em auto 0;
  }

  .main p {
    padding: 16px 20px;
  }

  .left-form input[type='text'],
  .left-form input[type='email'],
  .left-form input[type='password'] {
    font-family: 'HelveticaNeue', 'Helvetica Neue', Helvetica, Arial, sans-serif;
    padding: 0.7em 1em 0.7em 1em;
    width: 70%;
  }

  .right-form input[type='text'],
  input[type='password'] {
    font-family: 'HelveticaNeue', 'Helvetica Neue', Helvetica, Arial, sans-serif;
    padding: 0.7em 2em 0.7em 0em;
    width: 89%;
  }

  .left-form,
  .right-form {
    width: 83%;
    float: none;
    text-align: center;
  }

  .left-form > label {
    margin-left: 10px;
    margin-top: 13px;
  }

  .main h2,
  .main h3 {
    text-align: center;
  }

  .left-form li {
    margin-left: 13px;
  }

  .right-form li {
    margin-left: 16px;
  }

  .left-form input[type='submit'] {
    padding: 12px 12px;
    text-align: center;
    margin: 9px 0px;
  }

  .main h4 {
    float: left;
    margin: 7px 17px;
  }

  .right-form input[type='submit'] {
    float: right;
    padding: 8px 19px;
    margin: 2px 3px;
  }

  .copy-right p {
    margin: 3em 0em;
  }
}

@media only screen and (max-width: 320px) and (min-width: 240px) {
  .main {
    width: 96%;
    margin: 2em auto 0;
  }

  .main p {
    padding: 16px 17px;
  }

  .left-form input[type='text'],
  .left-form input[type='email'],
  .left-form input[type='password'] {
    font-family: 'HelveticaNeue', 'Helvetica Neue', Helvetica, Arial, sans-serif;
    padding: 0.4em 1em 0.4em 1em;
    width: 70%;
  }

  .right-form input[type='text'],
  input[type='password'] {
    font-family: 'HelveticaNeue', 'Helvetica Neue', Helvetica, Arial, sans-serif;
    padding: 0.6em 0.9em 0.6em 0em;
    width: 89%;
  }

  .left-form,
  .right-form {
    text-align: center;
  }

  .left-form > label {
    margin-left: 10px;
    margin-top: 13px;
  }

  .main h2,
  .main h3 {
    text-align: center;
  }

  .left-form li {
    margin-left: -6px;
  }

  .right-form li {
    margin-left: -5px;
  }

  .left-form input[type='submit'] {
    padding: 12px 12px;
    text-align: center;
    margin: 9px 0px;
  }

  .main h4 {
    float: left;
    margin: 7px 17px;
  }

  .right-form input[type='submit'] {
    float: right;
    padding: 8px 19px;
    margin: 2px 3px;
  }

  .copy-right p {
    margin: 2.5em 0em;
  }

  .icon {
    margin: 7px 5px 9px 0px;
  }
}
</style>
