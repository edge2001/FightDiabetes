<template>
    <div>
        <div class="main_div">
            <article>
                <h1 class="title">{{title}}</h1>
                <div class="meta">上传时间：{{updateTime}}</div>
                <div class="content"><pre>{{content}}</pre></div>
            </article>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            title:'Title!-----------!!!',
            updateTime:'2020-01-01',
            content:null,
        }
    },
    mounted() {
        this.getText();
    },
    methods:{
        getText() {
            let xhr = new XMLHttpRequest();
            xhr.open("GET", "test.txt", false);
            xhr.overrideMimeType("text/html;charset=utf-8");
            xhr.send(null);
            this.content=xhr.responseText;
        }
    }

}
</script>

<style scoped>
.main_div {
    position:relative;
    margin-left: 10%;
    margin-right: 10%;
    background-color: #Cfcfcf;
    border-radius: 0.5rem;
    overflow: hidden;
}
.title {
    font-size: 3.5em;
    margin:1%;
}
.meta {
    font-size: 2em;
    margin: 1%;
    text-align: center;
}
.content {
    font-size: 2em;
    margin: 1%;
    overflow: hidden;
    table-layout: fixed;
    word-break: break-all;
}
</style>