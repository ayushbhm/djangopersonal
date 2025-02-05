<template>
  <v-container>
    <v-row justify="center">
      <v-col v-for="(item, index) in items" :key="index" cols="12" sm="6" md="4">
        <v-card class="pa-3 text-center" outlined>
          <v-card-text class="text-h6 font-weight-bold">
            {{ item }}
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  props: {
    items: Array,
  },
};
</script>
