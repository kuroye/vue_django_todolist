<template>


    <el-card class="box-card" shadow="hover">
        <el-collapse>
        
            <el-collapse-item :title="todo.title">

                <div class="card-header">         
                    
                </div>

                <div class="text item">"ability subject": {{ todo.subject }}</div>
                <div class="text item">"dodo": {{ todo["dodo coin"] }}</div>


            </el-collapse-item>

        
        </el-collapse>
    </el-card>


</template>
  
<script setup>
import {defineProps, toRefs} from 'vue'

const props = defineProps(['todo'])
const {todo} = toRefs(props)



</script>

  <style>
  .card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .text {
    font-size: 14px;
  }
  
  .item {
    margin-bottom: 18px;
  }
  
  .box-card {
    width: 480px;
  }
  </style>
  