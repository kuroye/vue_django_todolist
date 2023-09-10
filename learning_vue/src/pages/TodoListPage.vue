<template>
    <!-- <TodoList/> -->

    <div class="new-todo-btn">
    <router-link to="/todo-add">
      <el-button :icon="CirclePlus">New todo</el-button>
    </router-link>
    </div>
    <Table/>
 </template>
 
<script setup>
 // import TodoList from '@/components/todolist/Todolist.vue'
import Table from '@/components/todolist/Table.vue'
import { CirclePlus } from "@element-plus/icons-vue";

 </script>
<style scoped>

.new-todo-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  transform: translate(0, 50px);
}

</style>