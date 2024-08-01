<template>
 
    <div class="container">
      <h1>MLOps Dashboard</h1>

      <!-- Input form for number of days -->
      <form @submit.prevent="makePrediction" class="input-form">
        <label for="nb_days">Number of days (1-30):</label>
        <input 
          id="nb_days" 
          type="number" 
          v-model.number="nbDays" 
          min="1" 
          max="30" 
          required 
          class="input-box"
        />
        <button type="submit" class="submit-button">Get Prediction</button>
      </form>
      
      <ul v-if="forecastData" class="forecast-list">
        <li v-for="(value, date) in forecastData" :key="date">
          <strong>{{ date }}:</strong> {{ value }}
        </li>
      </ul>

      <div v-if="graphImage" class="graph-container">
        <h2>Prediction vs test data </h2>
        <img :src="graphImage" alt="Train vs Test Data" class="graph-image" />
      </div>

      <div v-if="error" class="error-message">{{ error }}</div>
    </div>

</template>

<script>
export default {
  data() {
    return {
      nbDays: 5, // Default value
      forecastData: null,
      graphImage: null, // For storing the graph image
      error: null,
    };
  },
  methods: {
    async makePrediction() {
      try {
        const predictionResponse = await fetch('http://localhost:8000/predictions', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
          },
          body: JSON.stringify({ nb_day: this.nbDays }),
        });

        if (!predictionResponse.ok) {
          throw new Error(`HTTP error! Status: ${predictionResponse.status}`);
        }

        const predictionResult = await predictionResponse.json();
        this.forecastData = predictionResult.forcast;
        this.error = null;

        // Fetch the graph image
        const graphResponse = await fetch('http://localhost:8000/graph_input_data', {
          method: 'POST',
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json', 
          },
          body: JSON.stringify({ nb_day: this.nbDays }),
        });

        if (!graphResponse.ok) {
          throw new Error(`HTTP error! Status: ${graphResponse.status}`);
        }

        const graphResult = await graphResponse.json();
        this.graphImage = `data:image/png;base64,${graphResult.image}`;

      } catch (error) {
        console.error('Error making prediction:', error);
        this.error = `An error occurred: ${error.message}`;
      }
    },
  },
};
</script>

<style scoped>

.container {
  padding: 20px;
  background-color: white;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
}

h1 {
  font-size: 2em;
  margin-bottom: 20px;
}



.submit-button {
  margin-left: 10px;
  padding: 5px 10px;
  font-size: 1em;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.submit-button:hover {
  background-color: #0056b3;
}

.forecast-list {
  list-style-type: none;
  padding: 0;
  margin: 20px 0;
}

.forecast-list li {
  margin: 5px 0;
  font-size: 1.2em;
}

.graph-container {
  width: 1000px;
  max-width: 100%;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  background-color: white;
  border-radius: 10px;
  margin-top: 20px;
}

.graph-image {
  width: 100%;
  height: auto;
  border: 2px solid #ccc;
  border-radius: 10px;
}

.error-message {
  color: red;
  margin-top: 20px;
}
</style>
