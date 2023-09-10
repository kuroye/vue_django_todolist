<template>
    <div style="width: 400px; ">
    <canvas :id="chartId"></canvas>
    </div>

</template>

<script setup>
import {defineProps, onMounted, inject} from 'vue'
import Chart from 'chart.js/auto'

const do_reload = inject('reload')
const props = defineProps(['chartData', 'chartIndex'])

if (!props.chartData instanceof Array) {
    console.log("REFRESH daze");
    // location.reload()
    do_reload();
}

console.log("I AN CHARTDATA", props.chartData);
const chartId = `${props.chartIndex}`

const abilities = Object.values(props.chartData)[0]

const my_label = Object.keys(props.chartData)[0]
console.log("I AM ABILITIES", abilities);
onMounted(()=>{
    const ctx = document.getElementById(chartId)

    const data = {

        labels: abilities instanceof Array ? abilities.map((dict) => dict.subject) : '',
        datasets: [{
        label: my_label,
        // data: [28, 48, 30, 19, 96, 27, 200],
        data: abilities instanceof Array ? abilities.map((dict) => dict.score) : [] ,
        fill: true,
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        borderColor: 'rgb(54, 162, 235)',
        pointBackgroundColor: 'rgb(54, 162, 235)',
        pointBorderColor: '#fff',
        pointHoverBackgroundColor: '#fff',
        pointHoverBorderColor: 'rgb(54, 162, 235)'
        },]
        }

    const config = {
        type: 'radar',
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