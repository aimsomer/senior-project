<template>
  <v-card class="content">
    <v-card-title>Content </v-card-title>
    <v-card-text>
      <canvas ref="scatterChart" style="width: 100%; height: 400px;"></canvas>
    </v-card-text>
  </v-card>
</template>

<script>
import axios from 'axios'
// import { Scatter } from 'vue-chartjs'
// import * as chartConfig from './api.ts'
import Chart from 'chart.js/auto'

export default {
  mounted() {
    axios.get('http://127.0.0.1:5000/plot2').then(response => {
      const data = response.data.data
      console.log(data);
      const scatterChart = new Chart(this.$refs.scatterChart, {
        type: 'scatter',
        data: {
          datasets: [
            {
              label: 'My Dataset',
              data: data,
              backgroundColor: 'rgba(255, 99, 132, 0.2)',
              borderColor: 'rgba(255, 99, 132, 1)',
              borderWidth: 1
            }
          ]
        },
        options: {
          scales: {
            x: {
              type: 'linear',
              position: 'bottom'
            },
            y: {
              type: 'linear',
              position: 'left'
            }
          },
          responsive: true,
          maintainAspectRatio: true,
          parsing: {
            xAxisKey: 'power', // Replace with the name of your x property
            yAxisKey: 'speed', // Replace with the name of your y property
          },
        }
      })
    })
  }
}
</script>

<style scoped>
.content {
  width: 100%;
  margin-left: 20px;
  padding: 24px;
  border: 1px solid rgba(0, 0, 0, 0.1);
}
</style>