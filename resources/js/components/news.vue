<template>
  <div class="news">

    <el-col :offset="2" :span="20">
    <el-container>
  <el-header>{{header}}</el-header>
  <el-container>
    <el-aside width="400px">
      <el-image class="image"
      :src="aside"
      ></el-image></el-aside>
    <el-main>
      <div v-html="main">

      </div>
    </el-main>
  </el-container>
 <el-footer v-html="footer"></el-footer>
</el-container>
</el-col>
  </div>
</template>

<script>
export default {
  name: "news",
  data() {
    return {
      header: `
      پس‌لرزه‌های برهم زدن یک مراسم در قم/جعفری گیلانی: اینها چماقداران مدرن و بی‌عقل هستند/فردی که ۵ حکم از رهبری دارد را تحمل نمی‌کنند
      `,
      footer:`
      date: September 1st 2019, 18:25:00.000
      from: <a href="http://khabaronline.ir">khabaronline.ir</a>
`,
      main:`<p>روز پنجشنبه در همایش مبلغان در دفتر تبلیغات اسلامی حوزه علمیه قم، از سخنرانی احمد واعظی، ریاست این دفتر جلوگیری کردند.</p>
<p>در همین راستا، حجت الاسلام &nbsp;محمد جعفری گیلانی، رئیس هیأت امنای دفتر تبلیغات اسلامی&nbsp; دراین باره گفت: متاسفانه این افراد در تمامی مراسم‌ها حضور دارند. برای نمونه، در گذشته هم که رئیس مجلس شورای اسلامی در این شهر سخنرانی داشت، امثال این افراد درصدد برهم زدن سخنرانی او بودند.</p>
<p>وی افزود: این افراد چماقداران مدرن هستند و برای چنین کارهایی خلق شده‌اند. وقتی کسی احمد واعظی را که ۵ حکم از مقام معظم رهبری دارد، تحمل نکند دیگر چه کسی را می تواند تحمل کند؟</p>
<p>جعفری گیلانی با بیان اینکه ریشه چنین اقداماتی در بی‌عقلی، بی‌مبالاتی، خودزنی و خودسری خلاصه می‌شود، گفت: متاسفانه وقتی دو رئیس قوه‌قضاییه پیشین به جان هم می‌افتند و به هم توهین می‌کنند، چنین رفتارهایی هم در جامعه بروز می‌کند.<br /> &nbsp;<br /> وی با ابراز امیدواری نسبت به برخورد با چنین رفتارهایی گفت: البته به نظر می‌رسد که در این ماجرا مقام‌معظم رهبری ورود کنند. اگر من به شخصه در این مراسم حضور داشتم نمی‌گذاشتم که چنین اتفاقی بیفتد و با همه کسانی که قصد اخلال و برهم زدن سخنرانی‌ها را داشتند برخورد می‌کردم. من خودم ۴۰ سال است که در دفتر تبلیغات اسلامی هستم و همچنین موسس این دفتر بوده‌ام و در این قبیل مراسمات معمولا چند ده نفر روحانی را در جای جای مجلس می‌نشاندم که اگر کسی بخواهد در آنها حرفی اضافه بزند، فورا ۵۰ نفر بگویند خفه شو! متاسفانه من حضور نداشتم اگر بودم حتما این کار را می‌کردم و نمی‌گذاشتم کسی به رئیس دفتر تبلیغات اسلامی جسارت کند.</p>
<p>جعفری گیلانی با بیان اینکه تعداد اخلال‌گران مراسم‌های سخنرانی اندک و معدود است، گفت: با این وجود کاملا مشخص است که آبشخور این افراد کجاست. وقتی عده‌ای در ۱۵خرداد سال ۸۵ به آیت‌الله هاشمی که در حرم حضرت معصومه(س) سخنرانی داشت، هتاکی کردند. چنین رفتارهایی با سخنرانی رئیس دفتر تبلیغات اسلامی امر عجیبی نیست. ولی فکر می‌کنم این‌بار مقام معظم رهبری پیگیر ماجرا خواهند شد.</p>
<p>۲۷۲۱۵</p>
<div class=""gallery hidden""></div>
`,
      aside:`https://media.khabaronline.ir/d/2019/09/01/3/5252226.jpg
`
    };
  },
  mounted:function(){
    let url=localStorage.getItem('urlnews');
    this.$http.get(url)
    .then(req=>{
      //console.log(news);
      console.log(req);
      req=req.bodyText;
      req= eval(req);
      console.log(req);
      req= req[1];
        this.header=req.title;
        let str='';
        str+='date: ';
        str+=req.publish_date;
        str+=`

        from: <a href="http://
        `;
        str+=req.url;
        str+='">';
        str+=req.url;
        str+='</a>';
        this.footer=str;
        this.main=req.content;
        this.aside=req.thumbnail;
        //this.=req.summary;
      //  newss.source=req.url;




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
.news{
  margin: 20px;
}
.el-header{

  font-weight: bold;
  text-align: right;
   direction: rtl;
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
  }
  .el-footer {
     background-color: #B3C0D1;
     color: #333;
     text-align: center;
   }

  .el-aside {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
    line-height: 200px;
  }

  .el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: right;
     direction: rtl;
  }

  body > .el-container {
    margin: 40px;
  }
  .image{
    margin: 5px;
    border-radius: 2%;
  }
</style>
