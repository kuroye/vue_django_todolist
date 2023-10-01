<template>
    <div class="new-todo-btn">
    <router-link to="/todo-add">
      <el-button :icon="CirclePlus">New Card</el-button>
    </router-link>
    </div>

    <CardList/>
</template>

<script setup>
 import CardList from '@/components/lottery/CardList.vue'
import { CirclePlus } from "@element-plus/icons-vue";

</script>


<style scoped>

.new-todo-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  transform: translate(0, 50px);
}

</style>