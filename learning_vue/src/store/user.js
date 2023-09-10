import { defineStore } from "pinia";

import axios from "axios";

import {BASEURL} from '@/store/urls';
import router from "@/router";

// 创建 store
const useUserStore = defineStore('user', {

    persist: {
        enabled: true, // 开启数据缓存
    },

    // 定义状态：一个函数，返回一个对象
    state: () => ({
        user: localStorage.getItem('user') ?? '' ,
        token: localStorage.getItem('token') ?? ''
      }),

    // 定义 getters，等同于组件的计算属性
    getters: {
        // getter 函数接收 state 作为参数，推荐使用箭头函数
        // username: state => state.user.username,
        // dodo: state => state.user.dodo
        
    },

    // 定义 actions，有同步和异步两种类型
    actions: {
        // 异步 action，一般用来处理异步逻辑
        async login(userData) {
            const result = await axios.post(BASEURL + 'token/', userData)
            const { access, user, code } = result.data
            if (code===0) {
                // action 中修改状态
                this.user = user
                this.token = access
                localStorage.setItem('user',user)
                localStorage.setItem('token',access)
                
            }

         
        },
        async changeUserDoDo(user_id, my_dodo) {
            try {
            const data = await axios.post(BASEURL+'user/dodo', {
              "user_id": user_id,
              "dodo": my_dodo
            })
            console.log(data.data);
            const { dodo, code} = data.data

            if (code===0) {
                this.user.dodo = dodo
                
            }

            // try {
            //    const delete_data = await axios.delete(BASEURL+'todo/' + todo_id)
            //    console.log(delete_data.data);
            // } catch (error) {
            //     alert(error)
            //     console.log(error);
            // }
            } catch (error) {
              alert(error)
              console.log(error);
            }
          },
          async changeUserAbility(user_id, my_ability) {
            try {
            const data = await axios.post(BASEURL+'user/ability', {
              "user_id": user_id,
              "ability": my_ability
            })
            console.log(data.data);

            
            } catch (error) {
              alert(error)
              console.log(error);
            }
          },

        // 同步 action
        logout() {
            this.token = ''
            this.user = ''
            localStorage.removeItem('user')
            localStorage.removeItem('token')
        },



    },

    
})

export default useUserStore
