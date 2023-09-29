<template>
    <div style="display:flex; justify-content:center;">
      <div style="width:80%;">
        <div v-for="x in card.cards" :key="x">
          <el-card class="box-card" shadow="hover" :style="[x.card.rarity=='Rare' ? {width:max-content, color:blue} : {width:max-content}]">
        <template #header>
          <div class="card-header">
            <span>{{ x.card.rarity }}</span>
            <!-- <el-button class="button" text>Operation button</el-button> -->
          </div>
        </template>
        <div style="align-items:center" class="text item">{{ x.card.title }}</div>
        </el-card>
        </div>
      </div>
        

    </div>
    
  </template>
  

<script setup>
import { onMounted, computed } from "vue";
import {useCard} from "@/store/lottery";

const card = useCard();

import useUserStore from "@/store/user";

const userStore = useUserStore();

const user_id = userStore.user.id

console.log(user_id);
onMounted(() => {
  card.getCardStock(user_id);
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
  