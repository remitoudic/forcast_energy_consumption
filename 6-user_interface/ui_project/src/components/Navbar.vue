<template>
  <nav class="navbar">
    <router-link :to="{ name: 'AdminMlops' }">Workflow</router-link>
    <router-link :to="{ name: 'home' }">Project</router-link>
  </nav>
</template>

<script>
export default {
};
</script>

<style scoped>
.navbar {
  width: 100%;
  height: 60px;
  background-color: #333;
  color: white;
  display: flex;
  align-items: center;
  justify-content: flex-start; /* Adjust alignment */
  padding: 0 20px;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 1000;
}

nav {
  display: flex;
  gap: 20px; /* Add space between links */
}

.router-link {
  color: white; /* Ensures the text is visible on a dark background */
  text-decoration: none;
  font-size: 18px;
}

a.router-link-active {
  border-bottom: 2px solid #00ce89;
  padding-bottom: 4px;
}

.router-link:hover {
  color: #ddd; /* Hover effect */
}
</style>
