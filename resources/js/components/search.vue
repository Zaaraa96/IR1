<template>
  <div class="search">
    <el-col :offset="8" :span="6"><el-input  placeholder="search here"  v-model="input"></el-input></el-col>
    <el-col :span="2"><el-button type="danger" icon="el-icon-search">Search</el-button></el-col>
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
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.search{
  margin-top: 15%;
}
</style>
