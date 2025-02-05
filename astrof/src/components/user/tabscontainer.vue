<template>
    <v-container class="tabs-container">
      <v-tabs v-model="tab">
        <v-tab>Prepare by planets</v-tab>
        <v-tab>Prepare by Rashi</v-tab>
        <v-tab>Prepare by houses</v-tab>
      </v-tabs>
  
      <v-tabs-items v-model="tab">
        <v-tab-item v-if="tab === 0">
          <AstroTab type="planets" />
        </v-tab-item>
        <v-tab-item v-if="tab === 1">
          <AstroTab type="rashis" />
        </v-tab-item>
        <v-tab-item v-if="tab === 2">
          <AstroTab type="houses" />
        </v-tab-item>
      </v-tabs-items>
    </v-container>
  </template>
  
  <script>
  import AstroTab from "@/components/user/AstroTab.vue";
  
  export default {
    components: { AstroTab },
    data() {
      return {
        tab: 0, // Keeps track of the selected tab (0, 1, 2)
      };
    },
  };
  </script>
  <style scoped>
  .tabs-container {
    margin-top: 84px; /* Adjust based on your navbar height */
  }
  </style>
  