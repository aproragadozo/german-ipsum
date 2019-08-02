<template>
    <IpsumWrapper/>
</template>

<script>
import IpsumWrapper from './components/IpsumWrapper.vue';

export default {
  name: 'app',
  components: {
    IpsumWrapper,
  },
};
</script>

<style>
  @import url('https://fonts.googleapis.com/css?family=IBM+Plex+Serif');
  html {
    font-family: 'IBM Plex Serif', serif;
  }
</style>
