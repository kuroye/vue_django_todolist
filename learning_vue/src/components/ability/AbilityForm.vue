<template>
    <div class="form-container">
        <el-form :inline="true">
        <el-form-item :model="form">
            <el-input placeholder="New Ability"
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
import { useRoute } from "vue-router";
import { reactive } from "vue";
import { useAbilityStore } from "@/store/ability";
// import route from "@/router"

const route = useRoute();
const id = route.params["id"];

const store = useAbilityStore();

const form = reactive({
    name: '',
})

// const reload = inject('reload')
function onClick() {
    console.log("u clicked");
    store.postAbilitiy({subject: form.name,
                            group_id: id})
    // router.push({ path: '/ability/group/'+id})
    location.reload()
}
</script>



<style scoped>


</style>