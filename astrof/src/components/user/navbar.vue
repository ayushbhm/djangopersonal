<template>
    <v-app>
      <v-app-bar app color="grey lighten-3">
        <v-btn text>Home</v-btn>
        <v-spacer></v-spacer>
        <v-btn text>Weekly Contest</v-btn>
        <v-btn text>Astro Sutras</v-btn>
      </v-app-bar>
    </v-app>
  </template>
  
  <script>
  export default {
    name: 'navbar',
  };
  </script>
  
  <style scoped>
  /* Add custom styles if needed */
  .v-app {
    padding: 0;  /* Reset any default padding */
    margin: 0;   /* Reset any default margin */
    height: 100%; /* Ensure the height is correct */
 min-height: 0;
 
  }
  </style>
  