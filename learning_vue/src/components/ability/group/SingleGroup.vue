<template>
  <div v-for="(data, index) in single" :key="index">
    <div v-if="data.group_id == id">

        <AbilityForm></AbilityForm>
        <h1>{{ Object.keys(data)[0] }}</h1>
      <router-link
        :to="{ name: 'single group', params: { id: Object.values(data)[1] } }"
      >
        <BarChart :chartData="data" :chartIndex="index"/>
      </router-link>
    </div>
  </div>
</template>

<script setup>
import { useRoute } from "vue-router";
import { useAbilityStore } from "@/store/ability";
import { computed, onMounted } from "vue";
import BarChart from "@/components/ability/BarChart.vue";
import AbilityForm from "../AbilityForm.vue";
import useUserStore from "@/store/user";

const userStore = useUserStore();

const user_id = userStore.user.id

const route = useRoute();
const id = route.params["id"];

const store = useAbilityStore();

const single = computed(() => {
  return store.abilities;
});

onMounted(() => {
  store.fetchAbilities(user_id);
});
</script>


<style scoped>
div {
 margin-top: 60px;
 display: inline-block;
} 

h1 {
    transform: translate(0, -150px);
}
</style>