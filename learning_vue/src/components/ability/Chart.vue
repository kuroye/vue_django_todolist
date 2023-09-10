<template>

      <div v-for="(data, index) in abilities" :key="index">

      <router-link :to="{name: 'single group', params: { id : Object.values(data)[1]}}">
        <RadarChart :chartData="data" :chartIndex="index"/>
      </router-link>
    </div>
    
</template>

<script setup>
import { useAbilityStore } from "@/store/ability";
import RadarChart from "./RadarChart.vue";
import { computed, onMounted} from "vue";
import useUserStore from "@/store/user";

const userStore = useUserStore();
const user_id = userStore.user.id

const store = useAbilityStore();

const abilities = computed(() => {
  return store.abilities;
})

onMounted(() => {
  store.fetchAbilities(user_id);
})
// const chart_data = ref(ability.abilities)



</script>

<style scoped>
div {
 margin-top: 60px;
 display: inline-block;
} 
</style>