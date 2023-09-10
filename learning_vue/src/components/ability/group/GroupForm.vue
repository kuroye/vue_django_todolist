<template>
    <div class="form-container">
        <el-form :inline="true">
        <el-form-item :model="form">
            <el-input placeholder="Group name"
             v-model="form.name" :autofocus=true @keydown.enter="onClick"></el-input>
        </el-form-item>

        <el-form-item>
            <el-button :type="submit" @click="onClick()" :icon="CirclePlus"
            >Submit</el-button>
            <router-link to="/ability"><el-button>Cancel</el-button></router-link>
            
      
            
        </el-form-item>
    </el-form>

    </div>
    
       
</template>

<script setup>
import { reactive } from "vue";
import { useAbilityStore } from "@/store/ability";
import router from "@/router"
import useUserStore from "@/store/user";

const userStore = useUserStore();

const user_id = userStore.user.id

const store = useAbilityStore();

const form = reactive({
    name: '',
})

function onClick() {
    console.log("u clicked");
    store.postAbilitiyGroup({"name":form.name,
                            "user_id":user_id})
    router.push({ path: '/ability'})
}
</script>



<style scoped>

.form-container {
    transform: translate(0,50px);
}

</style>