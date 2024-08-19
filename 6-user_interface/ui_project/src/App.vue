<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Navbar from './components/Navbar.vue';
</script>
<template>
  <Navbar />
  <div class="content">
    <RouterView />
  </div>
</template>


<style scoped>
.content {
  margin-top: 60px;

}

</style>
