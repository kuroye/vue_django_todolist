<template>
  <div class="new-group-btn">
    <router-link to="/ability/group">
      <el-button :icon="CirclePlus">New group</el-button>
    </router-link>
  </div>

  <AbilityChart />
</template>

<script setup>
import AbilityChart from "@/components/ability/Chart.vue";

import { CirclePlus } from "@element-plus/icons-vue";
</script>

<style scoped>

.new-group-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    transform: translate(0,50px);
}

</style>