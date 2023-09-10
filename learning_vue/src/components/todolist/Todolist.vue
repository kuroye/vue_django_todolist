<template>
    <div v-for="todo in todolist" :key="todo.id">
        <div class="todo-container">
        <Todo :todo="todo"/>
        </div>
    </div>
    
    <div v-if="todos==0">
        <el-empty description="No todo yet"/>
    </div>
    
</template>

<script setup>
import Todo from '@/components/todolist/Todo.vue'
// import { ref } from 'vue';

import {useTodo} from '@/store/todo'

const todo = useTodo();

const todolist = todo.todos



</script>

<style>
.todo-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 30px;
}
</style>