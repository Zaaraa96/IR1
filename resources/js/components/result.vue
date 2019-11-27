<template>
  <div class="result">
    <br>
    <el-button type="primary" plain @click="sortbydate">sort by date</el-button>
    <div v-for="n in news" >
    <el-card class="box-card">

  <div slot="header" class="clearfix">
    <span>{{n.title}}</span>
    <el-button style="float: left; padding: 3px 0" type="text" icon="el-icon-back" @click="gotonews(n.id)"></el-button>
  </div>
  <div >
    {{n.summary}}
    <br>
    <a :href="n.source">{{n.source}}</a>
  </div>


</el-card>


  </div>
  </div>
</template>

<script>
export default {
  name: "result",
  data() {
    return {
      news:[
         // {title:"پس‌لرزه‌های برهم زدن یک مراسم در قم/جعفری گیلانی: اینها چماقداران مدرن و بی‌عقل هستند/فردی که ۵ حکم از رهبری دارد را تحمل نمی‌کنند",
         //  summary:'جماران نوشت: جعفری گیلانی گفت: متاسفانه این افراد در تمامی مراسم‌ها حضور دارند. برای نمونه، در گذشته هم که رئیس مجلس شورای اسلامی در این شهر سخنرانی داشت، امثال این افراد درصدد برهم زدن سخنرانی او بودند.',
         //  source:'http://khabaronline.ir'},
         // {title:"پس‌لرزه‌های برهم زدن یک مراسم در قم/جعفری گیلانی: اینها چماقداران مدرن و بی‌عقل هستند/فردی که ۵ حکم از رهبری دارد را تحمل نمی‌کنند",
         //   summary:'جماران نوشت: جعفری گیلانی گفت: متاسفانه این افراد در تمامی مراسم‌ها حضور دارند. برای نمونه، در گذشته هم که رئیس مجلس شورای اسلامی در این شهر سخنرانی داشت، امثال این افراد درصدد برهم زدن سخنرانی او بودند.',
         //   source:'http://khabaronline.ir'},
         // {title:"پس‌لرزه‌های برهم زدن یک مراسم در قم/جعفری گیلانی: اینها چماقداران مدرن و بی‌عقل هستند/فردی که ۵ حکم از رهبری دارد را تحمل نمی‌کنند",
         //    summary:'جماران نوشت: جعفری گیلانی گفت: متاسفانه این افراد در تمامی مراسم‌ها حضور دارند. برای نمونه، در گذشته هم که رئیس مجلس شورای اسلامی در این شهر سخنرانی داشت، امثال این افراد درصدد برهم زدن سخنرانی او بودند.',
         //    source:'http://khabaronline.ir'},
         // {title:"پس‌لرزه‌های برهم زدن یک مراسم در قم/جعفری گیلانی: اینها چماقداران مدرن و بی‌عقل هستند/فردی که ۵ حکم از رهبری دارد را تحمل نمی‌کنند",
         //     summary:'جماران نوشت: جعفری گیلانی گفت: متاسفانه این افراد در تمامی مراسم‌ها حضور دارند. برای نمونه، در گذشته هم که رئیس مجلس شورای اسلامی در این شهر سخنرانی داشت، امثال این افراد درصدد برهم زدن سخنرانی او بودند.',
         //     source:'http://khabaronline.ir'},

      ],
    };
  },
  methods:{

    gotonews(id) {
      console.log('id is: ',id);
      let str=''
      str+=id
      let url='http://127.0.0.1:5000/api/results?id=';
      url+=str;
      localStorage.urlnews= url;
      window.location.replace("http://localhost:8000/news");
    },
    sortbydate(){
      this.news=this.news.sort(function(a, b) {
        a = new Date(a.date);
        b = new Date(b.date);
        console.log(b);
        return a>b ? -1 : a<b ? 1 : 0;
      })
    },
  },
  mounted:function(){
    let url=localStorage.getItem('url');
    this.$http.get(url)
    .then(req=>{
      let news=[]
      //console.log(news);
      //console.log(req);
      console.log(req);
      req=req.bodyText;
      console.log(req);
      let bold=localStorage.getItem('bold');
      bold=bold.trim();
      bold= bold.split(' ');
      //console.log(bold);
      req= eval(req);
      console.log(req);
      for (var i = 0; i < req.length; i++) {

        i=i+1;
        let newss={}
        newss.id=req[i-1];
        newss.title=req[i].title;
        let date=req[i].publish_date;
        date= date.split(',');
        date= date[0];
        newss.date=date;
        let text=req[i].summary;
        // console.log(text);
        // for (var j = 0; j < bold.length; j++) {
        //   let word=bold[j];
        //   let str2=`<em>`;
        //   str2+=word;
        //   str2+=`</em>`;
        //   text=text.replace(word, str2);
        // }
        newss.summary=text;
        let str='http://'
        str+=req[i].url;
        newss.source=str;
        //console.log(newss);
        news.push(newss);
      }
      this.news=news;
      console.log(news);


      console.log(document.body.innerHTML);

      // for (var i = 0; i < a.length; i++) {
      //   console.log(a[i]);
      // }
      //
    }, error =>{
      console.log(error);
    });


      },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.box-card{
  direction: rtl;
  margin: 20px;
}
</style>
