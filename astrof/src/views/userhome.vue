<template>
    
    <navbar />
    <h1 class="toptext"> 
         <div class="gradient-container">
            Practice <span class="gradient-pill">Astrology questions</span> like never before!
        </div> 
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

  .gradient-pill {
    display: inline-block;
    background: linear-gradient(90deg, #FF1493 0%, #40E0D0 100%);
    padding: 8px 20px;
    border-radius: 50px;
    color: white;
    font-weight: bold;
    font-family: Arial, sans-serif;
}

/* Alternative version with more precise color matching */
.gradient-pill-exact {
    display: inline-block;
    background: linear-gradient(90deg, #FF69B4 0%, #40E0D0 100%);
    padding: 8px 20px;
    border-radius: 50px;
    color: white;
    font-weight: bold;
    font-family: Arial, sans-serif;
}

/* To use this with text that spans multiple lines */
.gradient-container {
    font-size: 32px;
    line-height: 1.2;
   display: flex;
   justify-content: center;
   padding: 40px 20px;
}

</style>
  
  