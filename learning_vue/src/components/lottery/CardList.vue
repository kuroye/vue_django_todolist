<template>
    <div style="display:flex;width:100%; justify-content:center;gap:16px">

        <Card/>
        <Card/>
        

    </div>
    
  </template>
  

<script setup>
// import { onMounted, computed } from "vue";
import Card from "./Card.vue";

</script>




  <style>
  .card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .text {
    font-size: 14px;
  }
  
  .item {
    margin-bottom: 18px;
  }
  
  .box-card {
    width: 480px;
  }
  </style>
  