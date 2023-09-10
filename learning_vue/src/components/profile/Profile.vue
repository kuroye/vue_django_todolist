<template>

<div class="profile-box">
        <div v-if="userStore.token">
              {{ userStore.user }}       <br />
              {{ userStore.token }}       <br />
              <el-button @click="onLogout">退 出</el-button>   
         </div>
</div>
    
</template>


<script setup>
import useUserStore from "@/store/user";

const userStore = useUserStore();


const onLogout = () => {
  userStore.logout();
  location.reload()
};


</script>



<style scoped>
.profile-box {
  display: flex;
  align-items: center;
  justify-content: center;
  transform: translate(0, 150px);
}
</style>