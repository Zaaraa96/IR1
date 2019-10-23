<template>
  <div>
    <router-link to='/search'><el-button type="primary" plain> search</el-button></router-link>
    <router-link to='/news'><el-button type="primary" plain> news</el-button></router-link>
    <br>
    <router-view></router-view>
  </div>
</template>
<script type="text/javascript">
  import search from './components/search.vue';
    import news from './components/news.vue';
  export default {

    name: 'App',
    props: {
      },
    data () {
      return {
      }
    },
    components: {
      search,
      news,
    },
      mounted:function(){
      },
    }

</script>
<style scoped>
  /* Add scoped styles */
  #app {
    padding: 20px;
  }
</style>
