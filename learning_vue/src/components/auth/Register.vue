<template>

    <div class="register-box">
        <el-form :model="form" label-width="120px">
    <el-form-item label="Username">
      <el-input v-model="form.username" />
    </el-form-item>
    <el-form-item label="Password">
      <el-input type="password" v-model="form.password" />
    </el-form-item>
    
    <el-form-item>
      <el-button type="primary" @click="onSubmit(form)">Register</el-button>
      <el-button>Cancel</el-button>
    </el-form-item>
  </el-form>

    </div>
        
</template>

<script setup>
import { reactive } from 'vue'
import { useAuthentication } from '@/store/auth';
import router from "@/router"

const auth = useAuthentication();


// do not use same name with ref
const form = reactive({
  username: '',
  password: '',
})

const onSubmit = (user_data) => {
  console.log(user_data.username)
  const data = auth.registerUser(user_data)
  console.log(data);
  console.log("success register");
  if (data['status']){
    router.push({ path: '/auth/login', query: {username: user_data.username}})
  }

}

</script>


<style scoped>

.register-box {
    display: flex;
    align-items: center;
    justify-content: center;
    transform: translate(0, 150px);
}
</style>