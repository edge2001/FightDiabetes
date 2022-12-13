<template>
  <div>
    <div class="main_div">
      <article>
        <h1 class="title">{{ title }}</h1>
        <div class="meta">上传时间：{{ updateTime }}</div>
        <div class="content">{{ content }}</div>
      </article>
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
      content: null
    }
  },
  mounted() {
    this.getText()
  },
  watch: {
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
        this.title =
          '糖友朋友们，今天按这个顺序吃饭，看看你的餐后血糖可以降多少'
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
      }
      id = String(id)
      let xhr = new XMLHttpRequest()
      xhr.open('GET', id + '.txt', false)
      xhr.overrideMimeType('text/html;charset=utf-8')
      xhr.send(null)
      this.content = xhr.responseText
    }
  }
}
</script>

<style scoped>
.main_div {
  position: relative;
  margin-left: 10%;
  margin-right: 10%;
  background-color: #cfcfcf;
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
</style>
