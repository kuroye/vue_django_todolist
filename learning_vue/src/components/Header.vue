<template>


  <el-row>

    <el-col :span="8">
      <div v-if="!userStore.token">
      <router-link to="/auth/register"><el-button type="primary" size="large" :icon="Memo">Register</el-button></router-link>
      <router-link to="/auth/login"><el-button size="large" :icon="Memo">Login</el-button></router-link>
      </div>
    </el-col>
    <el-col :span="8">

    <el-row>
      <el-col :span="6">
        
          <div v-if="userStore.user">
          
          <router-link to="/profile"><el-avatar :size="50" :src="circleUrl"/></router-link>
          
          </div>
        
      </el-col>

      <el-col :span="6">

        <div v-if="userStore.user">
          <div class="user-box">
      <b>{{ userStore.user.username }}</b>
              <hr style="width:50%">
              dodo: <b>{{ userStore.user.dodo }}</b>
          </div>
          
        </div>
        

      </el-col>

      <el-col :span="6">
        
        <div class="button-container">
        <router-link to="/"><el-button type="primary" size="large" :icon="Memo">Todo</el-button></router-link>
        </div>
      </el-col>
      <el-col :span="6">
        <div class="button-container">
          <router-link to="/ability"><el-button type="info" size="large" :icon="Histogram">Ability</el-button></router-link>
        </div>
      </el-col>
    </el-row>
      
    </el-col>
    <el-col :span="8"> 
      <div class="button-container">
          <router-link to="/"><el-button type="warning" size="large" :icon="MagicStick">Card</el-button></router-link>
      </div></el-col>
    
  </el-row>
        
</template>

<script setup>
import {
  // Check,
  // Delete,
  // Edit,
  // Message,
  // Search,
  MagicStick,
  Memo,
  Histogram,
} from '@element-plus/icons-vue'
import useUserStore from "@/store/user";

const userStore = useUserStore();

const circleUrl = 'https://p.qqan.com/up/2020-12/16070652276806379.jpg'



// const user = computed(() => {
//   return userStore.user;
// })


// const username = ref(userStore.username).value()
// const dodo =  ref(userStore.dodo).value()



</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 10px;

}
.button-container {
  /* margin: 7px 0 0 0; */
  display: flex;
  align-items: center;
}

.ava-container {
  margin: 0 5px 30px 0;
}

.user-box {
  transform: translate(-25%,0);
}
</style>