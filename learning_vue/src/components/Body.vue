<template>

  <router-view v-if="isRouterAlive"/> <!-- 进行v-if判断 -->
  
</template>

<script setup>

import { onMounted, ref, watch ,nextTick,provide,} from "vue";//要引入方法
import { useRouter } from "vue-router";

const isRouterAlive = ref(true);
    const reload = () => {
      isRouterAlive.value = false;
      nextTick(() => {
        isRouterAlive.value = true;
      });
    };
    provide("reload", reload);
</script>
