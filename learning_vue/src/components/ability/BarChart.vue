<template>
    <div style="width: 400px;" class="bar-chart-container">
    <canvas :id="chartId"></canvas>
    </div>
</template>

<script setup>
import {defineProps, onMounted} from 'vue'
import Chart from 'chart.js/auto'

const props = defineProps(['chartData', 'chartIndex'])

const chartId = `${props.chartIndex}`

const abilities = Object.values(props.chartData)[0]

const my_label = Object.keys(props.chartData)[0]


onMounted(()=>{
    const ctx = document.getElementById(chartId)

    const data = {

        labels: abilities.map((dict) => dict.subject),
        datasets: [{
        label: my_label,
        // data: [28, 48, 30, 19, 96, 27, 200],
        data: abilities.map((dict) => dict.score),
        fill: true,
        backgroundColor: 'rgba(54, 162, 235, 0.5)',
        borderColor: 'rgb(54, 162, 235)',
        pointBackgroundColor: 'rgb(54, 162, 235)',
        pointBorderColor: '#fff',
        pointHoverBackgroundColor: '#fff',
        pointHoverBorderColor: 'rgb(54, 162, 235)'
        },]
        }

    const config = {
        type: 'bar',
        data: data,
        options: {
            elements: {
                line: {
                borderWidth: 3
                }
            },
            responsive: true,
            maintainAspectRatio:false,
        
            },
        }
    new Chart(ctx, config);

})
</script>

<style scoped>
.bar-chart-container {
    transform: translate(0,-60px);
}
</style>