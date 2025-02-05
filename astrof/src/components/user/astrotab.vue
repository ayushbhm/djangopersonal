<template>
    <v-tab-item>
      <CardGrid :items="items" />
    </v-tab-item>
  </template>
  
  <script>
  import CardGrid from "./CardGrid.vue";
  
  export default {
    components: { CardGrid },
    props: {
      type: String, // "planets", "rashis", "houses"
    },
    data() {
      return {
        items: [],
      };
    },
    mounted() {
      this.getDummyData();
    },
    methods: {
      getDummyData() {
        const data = {
          planets: ["Jupiter", "Saturn", "Mars", "Venus", "Mercury", "Sun", "Moon", "Rahu", "Ketu"],
          rashis: ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"],
          houses: ["1st House", "2nd House", "3rd House", "4th House", "5th House", "6th House", "7th House", "8th House", "9th House", "10th House", "11th House", "12th House"],
        };
        this.items = data[this.type] || [];
      },
    },
  };
  </script>
  