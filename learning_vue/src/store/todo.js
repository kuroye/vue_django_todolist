import { defineStore } from "pinia";

import axios from "axios";

import {BASEURL} from '@/store/urls'



// You can name the return value of `defineStore()` anything you want,
// but it's best to use the name of the store and surround it with `use`
// and `Store` (e.g. `useUserStore`, `useCartStore`, `useProductStore`)
// the first argument is a unique id of the store across your application
export const useTodo = defineStore("todo", {
  state: () => ({
    todos: [],
    // single: [],
  }),
  actions: {
    // 返回属于用户的todo
    async getTodolist(user_id) {
      try {
        const data = await axios.get(BASEURL+'todo/', {
          params:{
            id: user_id
          }
        })
        this.todos = data.data
        
      } catch (error) {
        alert(error)
        console.log(error);
      }
    },
    async postTodo(todo_data) {
      try {
      const data = await axios.post(BASEURL+'todo/', {
        "title": todo_data.title,
        "subject": todo_data.subject,
        "dodo": todo_data.dodo,
        "user": todo_data.user_id
      })
      console.log(data.data);
       
      } catch (error) {
        alert(error)
        console.log(error);
      }
    },

    async getTodo(todo_id) {
      try {
      const data = await axios.get(BASEURL+'todo/' + todo_id)
      console.log(data.data);
      return data

      } catch (error) {
        alert(error)
        console.log(error);
      }
    },

    async changeStatusTodo(todo_id, todo_bool_data) {
      try {
      const data = await axios.patch(BASEURL+'todo/update/' + todo_id, {
        "is_finished": todo_bool_data
      })
      console.log(data.data);
       
      } catch (error) {
        alert(error)
        console.log(error);
      }
    },
    async deleteTodo(todo_id) {
      try {
      const data = await axios.delete(BASEURL+'todo/' + todo_id)
      console.log(data.data);
       
      } catch (error) {
        alert(error)
        console.log(error);
      }
    }
  }
});
