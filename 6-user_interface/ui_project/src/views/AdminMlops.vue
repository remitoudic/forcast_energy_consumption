<template>
  <div class="container">

    <h1>ML experiements</h1>
    <button @click="redirect_to_notebook_server">Jupyter server</button>
    <br>
    <button @click="redirect_to_mlflow_project">Mlflow Project Dashboard</button>
    <br>
    <h1>Pipeline management</h1>
    <button @click="trigger_etl_mage">Trigger E.T.L pipeline</button>
    <br>
    <button @click="redirect_to_monitoring_report">Mage Dashboard</button>
    <h1>System Monitoring</h1>
    <button @click="">Monitoring report (Batch)</button>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const predictions = ref([]);

const trigger_etl_mage = async () => {
  try {
    const response = await fetch('http://http://172.17.0.1/:8000/mage_trigger_etl', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'accept': 'application/json'
      },
      body: JSON.stringify({})
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    console.log('Response data:', data);
  } catch (error) {
    console.error('Error:', error);
  }
};

const redirect_to_monitoring_report = () => {
  window.location.href = 'http://34.173.156.32:6789/';
};

const redirect_to_notebook_server = () => {
  window.location.href = 'http://34.173.156.32:8888/';
};

const redirect_to_mlflow_project = () => {
  window.location.href = 'http://34.173.156.32:5000/#/experiments/1';
};
</script>


<style scoped>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f7f9fc;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

h1 {
  font-size: 1.5rem;
  margin-bottom: 1rem;
  color: #333;
}

.button-group {
  margin-bottom: 2rem;
}

button {
  display: block;
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  font-size: 1rem;
  color: #fff;
  background-color: #00ce89;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #0056b3;
}

button:focus {
  outline: none;
}
</style>

