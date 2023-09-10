<template>
  <div class="login-box">
    <!-- <el-form :model="form" label-width="120px">
    <el-form-item label="Username">
      <el-input v-model="form.username" />
    </el-form-item>
    <el-form-item label="Password">
      <el-input type="password" v-model="form.password" />
    </el-form-item>
    
    <el-form-item>
      <el-button type="primary" @click="onSubmit(form)">Login</el-button>
      <el-button>Cancel</el-button>
    </el-form-item>
  </el-form> -->
    <!-- <div> -->
         <!-- state：通过 store 直接访问 -->
      <!--    <div v-if="userStore.token">
              {{ userStore.user }}       <br />
              {{ userStore.token }}       <br />
              <el-button @click="onLogout">退 出</el-button>    </div
      > -->
      ​    <div v-if="!userStore.token">
            用户名：<el-input v-model="userData.username"/>      <br />
            密码：<el-input v-model="userData.password" type="password" @keydown.enter="onLogin"/>      <br />
             <el-button @click="onLogin">登 录</el-button>    </div
      >
        
    <!-- </div> -->
  </div>
</template>

<script setup>
import { reactive } from "vue";
// import { useAuthentication } from '@/store/auth';
import useUserStore from "@/store/user";
import router from "@/router";
// import router from "@/router"
// import { useRoute } from "vue-router";

// const router = useRoute();

// const auth = useAuthentication();

// do not use same name with ref
// const form = reactive({
//   username: router.query.username,
//   password: "",
// });

const userData = reactive({
  username: "",
  password: "",
});

// 实例化 store
const userStore = useUserStore();
const onLogin = async () => {
  // 使用 actions，当作函数一样直接调用
  // login action 定义为了 async 函数，所以它返回一个 Promise
  await userStore.login(userData);
  userData.username = "";
  userData.password = "";
  router.push({path: '/'})
};
const onLogout = () => {
  userStore.logout();
};

// 作者：昆吾kw
// 链接：https://juejin.cn/post/7154579554034515982
// 来源：稀土掘金
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

// const onSubmit = (user_data) => {
//   console.log(user_data.username);
//   const data = auth.loginUser(user_data);
//   console.log(data);
// };
</script>


<style scoped>
.login-box {
  display: flex;
  align-items: center;
  justify-content: center;
  transform: translate(0, 150px);
}
</style>