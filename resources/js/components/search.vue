<template>
  <div class="search">
    <el-col :offset="8" :span="6"><el-input  placeholder="در این جا جستجو کنید"  v-model="input"></el-input></el-col>
    <el-col :span="2"><el-button type="danger" icon="el-icon-search" @click="search">جستجو</el-button></el-col>
  </div>
</template>

<script>
export default {
  name: "search",
  data() {
    return {
       input: '',
    };
  },
  methods:{
    search(){
      let input= this.input;
      let length= input.length;
      let inputarr=[];
      let inputarrlist=[];
      let fixed=[];
      let notin=[];
      let source="";
      let cat="";
      if (length>0) {
        for (var i = 0; i <length; i++) {
          if (input[i]=='"') {
            fixed.push(i);
          }
        }
      }


      if (fixed.length>1) {
        //if one of " is extra we delete it
        if(fixed.length%2==1){
          fixed.pop();
        }
        //find exact word between ""
        for (var j = fixed.length-1; j >=0; j=j-2) {
          //word is in fixed[j-1],fixed[j]
          if (fixed[j]>fixed[j-1]+1) {
            let word= input.slice(fixed[j-1], fixed[j]+1);
            let word2= input.slice(fixed[j-1]+1, fixed[j]);
            input = input.replace(word, '');
            word2= word2.trim();
            let check=0;

            for (var s2=0; s2<word2.length-1;s2++){

              if(word2[s2]==" "){
                //console.log(word2[s2]);
                check++;
              }
            }
            if(check>0)
              {inputarrlist.push(word2);}
            else{
              inputarr.push(word2);
            }

          }else {
            let word='""';
            input = input.replace(word, '');
          }
        }
      }


      input = input.replace('"', '');
      input = input.replace(/: /g, ":");
      input = input.replace(/:/g, ": ");
      input = input.trim();
      input= input.split(' ');

      let s= input.indexOf("source:");
      let c= input.indexOf("cat:");
      if(s!=-1){
        source= input[s+1];
        input[s]='';
        input[s+1]='';
      }
      if(c!=-1){
        cat= input[c+1];
        input[c]='';
        input[c+1]='';
      }

      for (var i = 0; i < input.length; i++) {
        if (input[i]!="") {
          if (input[i][0]=='!') {
            if(input[i].length>1){
              notin.push(input[i].slice(1));
            }
          }
          else {
            inputarr.push(input[i]);
          }

        }
      }
      console.log(" list of words in '': ",inputarrlist);
      console.log("word list: ",inputarr);
      console.log("not in list: ",notin);
      console.log("source: ",source);
      console.log("cat: ",cat);


          let query={};
          query.list=inputarrlist;
          query.words= inputarr;
          query.notin=notin;
          query.source=source;
          query.cat=cat;
          let bold='';
          for (var i = 0; i < inputarr.length; i++) {
            bold+=inputarr[i];
            bold+=" ";
          }
          for (var i = 0; i < inputarrlist.length; i++) {
            bold+=inputarrlist[i];
            bold+=" ";
          }
          localStorage.bold= bold;
          this.$http.post('http://127.0.0.1:5000/api/search',query)
          .then(req=>{
            console.log(req);
            let docIDs=req.body;
            let str=''
            for (var i = 0; i < docIDs.length; i++) {
              let num=0;
              num= docIDs[i]-1;
              str+=num;
              if(i<docIDs.length-1)
                {str+=',';}
            }
            //console.log(req);
            //console.log(body);
            let url='http://127.0.0.1:5000/api/results?id=';
            url+=str;
            localStorage.url= url;
            window.location.replace("http://localhost:8000/result");


          }, error =>{
            console.log(error);
          });









},
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.search{
  direction: rtl;
  margin-top: 15%;
}
</style>
