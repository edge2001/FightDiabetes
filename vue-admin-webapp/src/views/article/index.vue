<template>
  <div>
    <div class="111">
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
          <li v-for="title in showTitleList" @click="jumpToArticle(title.id)">
            {{ title.title }}
          </li>
        </ul>
      </div>
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
          id: 1,
          updateTime: '2020-01-01'
        },
        {
          title: '糖友朋友们，今天按这个顺序吃饭，看看你的餐后血糖可以降多少',
          id: 2,
          updateTime: '2020-05-14'
        },
        {
          title: '哪种水果糖分低？糖尿病友聪明控糖',
          id: 3,
          updateTime: '2019-09-24'
        },
        {
          title: '四招预防糖尿病肾病',
          id: 4,
          updateTime: '2019-11-07'
        },
        {
          title: '用知识点亮寒冬心灯用行动助力糖尿病之友',
          id: 5,
          updateTime: '2021-01-11'
        },
        {
          title: '18年坚守磨一剑科普创新洞见未来',
          id: 6,
          updateTime: '2021-04-01'
        },
        {
          title: '这些危险因素让糖尿病“找上门”',
          id: 7,
          updateTime: '2018-12-03'
        },
        {
          title:'给小糖友的“运动处方”',
          id: 8,
          updateTime: '2019-04-16'
        },
        {
          title:'哪些人容易得糖尿病',
          id: 9,
          updateTime:'2019-03-05'
        },
        {
          title:'Diabetes Care：糖尿病会遗传吗？“糖二代”怎样饮食预防？',
          id: 10,
          updateTime:'2022-03-17'
        },
        {
          title:'3种食物是“升糖王”，得了糖尿病不忌口，打再多胰岛素也没用',
          id: 11,
          updateTime:'2022-11-17'
        },
        {
          title:'糖友如何运动才不伤身？',
          id: 12,
          updateTime:'2020-03-12'
        },
      ],
      showTitleList:[]
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
      // if (id == 1) {
      //   this.title = '糖尿病患者空腹血糖升高的8种常见原因及对策，糖友必学技能'
      //   this.updateTime = '2020-01-01'
      // } else if (id == 2) {
      //   this.title ='糖友朋友们，今天按这个顺序吃饭，看看你的餐后血糖可以降多少'
      //   this.updateTime = '2020-05-14'
      // } else if (id == 3) {
      //   this.title = '哪种水果糖分低？糖尿病友聪明控糖'
      //   this.updateTime = '2019-09-24'
      // } else if (id == 4) {
      //   this.title = '四招预防糖尿病肾病'
      //   this.updateTime = '2019-11-07'
      // } else if (id == 5) {
      //   this.title = '用知识点亮寒冬心灯用行动助力糖尿病之友'
      //   this.updateTime = '2021-01-11'
      // } else if (id == 6) {
      //   this.title = '18年坚守磨一剑科普创新洞见未来'
      //   this.updateTime='2021-04-01'
      // }
      if (id > this.titleList.length) {
        this.$router.push({
          name: '404'
        })
      }
      var i=0
      for (; i < this.titleList.length; i++) {
        if (id == this.titleList[i].id) {
          this.title = this.titleList[i].title
          this.updateTime = this.titleList[i].updateTime
          break
        }
      }
      id = String(id)
      let xhr = new XMLHttpRequest()
      xhr.open('GET', id + '.txt', false)
      xhr.overrideMimeType('text/html;charset=utf-8')
      xhr.send(null)
      this.content = xhr.responseText
      i=0
      var idList=[]
      while(i<6) {
        var j=parseInt(Math.random()*this.titleList.length,10)+1
        if(!idList.includes(j)){
          idList.push(j)
          console.log(j)
          this.showTitleList.push(this.titleList[j-1])
          i++
        }
      }
    },
    jumpToArticle(id) {
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
  width: 65%;
  margin-right: 3%;
  border-style: solid;
  border-width: 1px;
  border-color: black;
  border-radius: 0.5rem;
  overflow: hidden;
  display: inline-block;
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
  display: inline-block;
  vertical-align: top;
  border-style: solid;
  border-width: 3px;
  border-color: aqua;
  border-radius: 0.5rem;
  overflow: hidden;
  color: #36a3f7;
  position: relative;
  width: 24%;
  height: auto;
  font-size: 20px;
}
li {
  padding-top: 10px;
}
li:hover {
  background-color: rgb(241, 195, 109);
}
</style>
