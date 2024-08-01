<template>
  <div class="container">
    <h1>Pipeline management</h1>
    <button @click="trigger_etl_mage">Trigger_pipeline</button>
    <br>
    <button @click="redirect_to_monitoring_report">GO to Mage Dashboard</button>
    <h1>System Monitoring</h1>
    <button @click="">Monitoring report (Batch)</button>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const predictions = ref([]);

const trigger_etl_mage = async () => {
  try {
    const response = await fetch('http://localhost:8000/mage_trigger_etl', {
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
  window.location.href = 'http://localhost:6789/';
};
</script>
