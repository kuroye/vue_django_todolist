<template>
    <div class="form-container">
        <el-form :inline="true">
        <el-form-item :model="form">
            <el-input placeholder="Title"
             v-model="form.title" :autofocus=true @keydown.enter="onClick"></el-input>
        </el-form-item>

        <el-form-item>
            <el-button :type="submit" @click="onClick()"
            >Submit</el-button>
            <router-link to="/"><el-button>Cancel</el-button></router-link>
            
      
            
        </el-form-item>
        <el-transfer v-model="value" :data="abilities?.map(x => ({  key: x.id,
                                                                    label: x.subject,
                                                                    disabled: 0,
                                                                }))"/>
        <h3>{{ abilities?.map(({ id,subject }) => `${id}-${subject}`) }}</h3>
        <h3>{{ getRandomInt(20)}}</h3>
        
    </el-form>

      

    </div>
  
</template>

<script setup>
import {getRandomInt} from "@/utils/utils";
// import { CirclePlus } from "@element-plus/icons-vue";
import { ref, reactive, computed, onMounted, inject } from "vue";

import {useTodo} from '@/store/todo'
import {useAbilityStore} from '@/store/ability'

import router from "@/router"

const do_reload = inject('reload');

const todo = useTodo();

const ability_store = useAbilityStore();


import useUserStore from "@/store/user";

const userStore = useUserStore();

const user_id = userStore.user.id

const abilities = computed(() => {
    // console.log(ability_store.getAbilities(user_id));
  return ability_store.abilities.abilities;
})

const value = ref([])
// const el_transfer_data=[]
// abilities?.value.forEach(element => {
//       el_transfer_data.push({
//           key: element.id,
//           label: element.subject,
//           disabled: 0,
//       })
// })


// console.log(el_transfer_data);
// var mapped_val = []
// if(abilities.value) {
//     mapped_val = abilities.value.abilities.map(({ subject }) => subject)
// }
// console.log(mapped_val);

onMounted(() => {
  ability_store.getAbilities(user_id);
})

const form = reactive({
    title: '',
})

function onClick() {
    console.log("u clicked", Object.values(value.value));
    todo.postTodo({subject: Object.values(value.value),
                        title: form.title,
                        dodo: getRandomInt(10),
                        user_id: user_id})
    router.push({ path: '/', replace:true}).then(do_reload())
    
}

</script>


<style scoped>

.new-todo-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  transform: translate(0, 50px);
}
.form-container {
    transform: translate(0,50px);
}
</style>