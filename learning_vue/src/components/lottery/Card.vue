<template>
    <div style="display:flex;width:100%; justify-content:center;gap:16px">

        <div v-for="x in card.cards" :key="x">
        <el-card class="box-card" shadow="hover" style="width:max-content">
      <template #header>
        <div class="card-header">
          <span>{{ x.rarity }}</span>
          <!-- <el-button class="button" text>Operation button</el-button> -->
        </div>
      </template>
      <div style="align-items:center" class="text item">{{ x.title }}</div>
        </el-card>
        </div>

    </div>
    
  </template>
  

<script setup>
import { onMounted, computed } from "vue";
import {useCard} from "@/store/lottery";

const card = useCard();

onMounted(() => {
  card.getCard();
});

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
  