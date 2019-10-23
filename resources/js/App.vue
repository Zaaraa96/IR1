<template>
  <div>
    <router-link to='/search'><el-button type="primary" plain> search</el-button></router-link>
    <br>
    <router-view></router-view>
  </div>
</template>
<script type="text/javascript">
  import search from './components/search.vue';
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
