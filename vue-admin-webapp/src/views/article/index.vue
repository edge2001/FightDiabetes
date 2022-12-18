<template>
  <div>
    <div class="main_div">
      <article>
        <h1 class="title">{{ title }}</h1>
        <div class="meta">上传时间：{{ updateTime }}</div>
        <div class="content">{{ content }}</div>
      </article>
    </div>
    <div class="article_list">
      <h3 style="font-size:28px;text-align: center;">其他文章</h3>
      <ul>
        <li v-for="title in titleList" @click="jumpToArticle(title.id)">{{ title.title }}</li>

      </ul>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      name: 'article',
      title: null,
      updateTime: null,
      content: null,
      titleList: [
        {
          title: '糖尿病患者空腹血糖升高的8种常见原因及对策，糖友必学技能',
          id: 1
        },
        {
          title: '糖友朋友们，今天按这个顺序吃饭，看看你的餐后血糖可以降多少',
          id: 2
        },
        {
          title: '哪种水果糖分低？糖尿病友聪明控糖',
          id: 3
        },
        {
          title: '四招预防糖尿病肾病',
          id: 4
        },
        {
          title: '用知识点亮寒冬心灯用行动助力糖尿病之友',
          id: 5
        },
        {
          title: '18年坚守磨一剑科普创新洞见未来',
          id: 6
        }
      ]
    }
  },
  mounted() {
    this.getText()
  },
  watch: {
    // eslint-disable-next-line no-unused-vars
    $route(to, from) {
      this.getText()
    }
  },
  methods: {
    getText() {
      var id = this.$route.params.id
      if (id == 1) {
        this.title = '糖尿病患者空腹血糖升高的8种常见原因及对策，糖友必学技能'
        this.updateTime = '2020-01-01'
      } else if (id == 2) {
        this.title ='糖友朋友们，今天按这个顺序吃饭，看看你的餐后血糖可以降多少'
        this.updateTime = '2020-05-14'
      } else if (id == 3) {
        this.title = '哪种水果糖分低？糖尿病友聪明控糖'
        this.updateTime = '2019-09-24'
      } else if (id == 4) {
        this.title = '四招预防糖尿病肾病'
        this.updateTime = '2019-11-07'
      } else if (id == 5) {
        this.title = '用知识点亮寒冬心灯用行动助力糖尿病之友'
        this.updateTime = '2021-01-11'
      } else if (id == 6) {
        this.title = '18年坚守磨一剑科普创新洞见未来'
        this.updateTime='2021-04-01'
      }
      id = String(id)
      let xhr = new XMLHttpRequest()
      xhr.open('GET', id + '.txt', false)
      xhr.overrideMimeType('text/html;charset=utf-8')
      xhr.send(null)
      this.content = xhr.responseText
    },
    jumpToArticle(id){
      this.$router.push({
          name: 'article',
          params: {
            id: id
          }
        })
      window.location.reload()
    }
  }
}
</script>

<style scoped>
.main_div {
  position: relative;
  margin-left: 7%;
  margin-right: 30%;
  border-style: solid;
  border-width: 1px;
  border-color: black;
  border-radius: 0.5rem;
  overflow: hidden;
}
.title {
  font-size: 3em;
  margin: 1%;
  text-align: center;
}
.meta {
  font-size: 1.5em;
  margin: 1%;
  text-align: center;
}
.content {
  font-size: 2em;
  margin: 1%;
  overflow: hidden;
  table-layout: fixed;
  word-break: break-all;
  white-space: pre-wrap;
}
.article_list {
  border-style: solid;
  border-width: 3px;
  border-color: aqua;
  border-radius: 0.5rem;
  overflow: hidden;
  color: #36a3f7;
  position: absolute;
  width:  20%;
  height: 60%;
  right: 5%;
  top:  10%;
  font-size: 20px;
}
li {
  padding-top: 10px;
}
li:hover{
  background-color: rgb(241, 195, 109);
}
</style>
