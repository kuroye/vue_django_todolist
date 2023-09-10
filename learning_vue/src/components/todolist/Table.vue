<template>
  <div v-if="tableData == 0" style="transform: translate(0,50px)">
    <el-empty description="No todo yet" />
  </div>

  <div v-if="tableData != 0">
    <div class="table-container">
      <el-table :data="filterTableData" style="width: 50%">
        <el-table-column label="Title" prop="title" />
        <el-table-column label="DoDo" prop="dodo" />
        <!-- <el-table-column label="Status" prop="id" > -->
        <el-table-column label="Action" prop="">
          <template #default="scope">
            <div v-if="scope.row.is_finished == false">
              <el-button
                type="primary"
                size="big"
                @click="
                  handler(scope.row.id);
                  drawer = true;
                "
                ><el-icon><FullScreen /></el-icon
              ></el-button>

              <el-button
                size="big"
                @click="statusChange(scope.row.id, scope.row.is_finished)"
                ><el-icon><Check /></el-icon
              ></el-button>

              <el-button
                size="big"
                type="danger"
                @click="handleDelete(scope.row.id)"
                ><el-icon><Delete /></el-icon
              ></el-button>
            </div>
            <div v-if="scope.row.is_finished == true">
              <el-button
                type="primary"
                size="big"
                @click="
                  handler(scope.row.id);
                  drawer = true;
                "
                ><el-icon><FullScreen /></el-icon
              ></el-button>

              <el-button
                type="info"
                size="big"
                @click="statusChange(scope.row.id, scope.row.is_finished)"
                ><el-icon><Close /></el-icon
              ></el-button>

              <el-button
                size="big"
                type="warning"
                @click="handleReward(user_id,scope.row.dodo, scope.row.id, scope.row.subject.subject_id)"
                ><el-icon><Medal /></el-icon
              ></el-button>
            </div>
          </template>
        </el-table-column>
        <el-table-column align="center">
          <template #header>
            <el-input
              v-model="search"
              size="small"
              placeholder="Type to search"
            />
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>

  <el-drawer v-model="drawer" :with-header=false>
    <div>
      <h4>Title</h4>
      <span>{{ result.todo.title}}</span>
      <el-divider/>
      <h4>Status</h4>
      <span>{{ result.todo.is_finished}}</span>
      <el-divider></el-divider>
      <h4>DoDo</h4>
      <span>{{ result.todo.dodo}}</span>
      <el-divider>
        <el-icon><star-filled /></el-icon>
      </el-divider>
      <h4>Subject</h4>
      <span>{{ result.subject.subject_in_letter }}</span>
      <el-divider content-position="right">你最棒</el-divider>
    </div>
  </el-drawer>
</template>

<script setup>
import { computed, onMounted, ref, reactive, inject} from "vue";
import {
  Delete,
  Check,
  Close,
  Medal,
  FullScreen,
} from "@element-plus/icons-vue";


const do_reload = inject('reload');

const search = ref("");
const filterTableData = computed(() =>
  tableData.value.filter(
    (data) =>
      !search.value ||
      data.title.toLowerCase().includes(search.value.toLowerCase())
  )
);

import { useTodo } from "@/store/todo";
import useUserStore from "@/store/user";

const userStore = useUserStore();

const user_id = userStore.user.id

const todo = useTodo();

const tableData = computed(() => {
  return todo.todos;
});

onMounted(() => {
  console.log("I AM ID", userStore.user.id);
  // location.reload();
  todo.getTodolist(user_id);
});

const handleDelete = (id) => {
  console.log("这是id", id);
  todo.deleteTodo(id);
  do_reload();
  // location.reload();
};

const statusChange = (id, is_finished) => {
  if (is_finished == false) {
    todo.changeStatusTodo(id, true);
  } else {
    todo.changeStatusTodo(id, false);
  }

  do_reload();
  // location.reload();
};

const handleReward = (user_id, dodo, todo_id, ability) => {

    userStore.changeUserAbility(user_id, ability)
    userStore.changeUserDoDo(user_id, dodo) 
    todo.deleteTodo(todo_id);
    // location.reload();
    
    do_reload();
  

}
const drawer = ref(false);

let result = reactive({ todo: {},
                        subject: {} });
async function handler(id) {
  // await 后面的函数返回的是一个promise对象，我们只需要其中data属性的值，所以做了解构
  let { data } = await todo.getTodo(id);
  result.todo = data;
  result.subject = data.subject;
  console.log("I AM DATA", data);
}



// const test = computed(() => {
//   try {
//     return result.todo.subject.subject_in_letter
//   } catch (error) {
//     alert(error)
//     console.log(error);
//     return 0;
//   }
  
// });

// console.log("I AM TEST", test);

import { StarFilled } from "@element-plus/icons-vue";

</script>


 <style scoped>
.table-container {
  display: flex;
  justify-content: center;
  align-items: center;
  transform: translate(0, 100px);
}
</style>