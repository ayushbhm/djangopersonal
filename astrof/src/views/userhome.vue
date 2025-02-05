<template>
    
    <navbar />
    <h1 class="toptext"> 
        Practice Astrology questions <br>like never before!
    </h1>
    <tabscontainer />
  </template>
  
  <script>
  import navbar from '@/components/user/navbar.vue'
  import tabscontainer from '@/components/user/tabscontainer.vue';
  
  export default {
    components: {
      navbar,
      tabscontainer,
    },
  };
  </script>

  <style scoped>

.toptext{
    margin-left: 30%;
}
</style>
  
  