import { defineStore } from "pinia";

import axios from "axios";

import {BASEURL} from '@/store/urls'


export const useAuthentication = defineStore("auth", {
//   state: () => ({
//     abilities: [],
//     // single: [],
//   }),
//   // getters: {
//   //   getAbilities(state){
      
//   //     return state.abilities
//   //   }
//   // },
  actions: {
    // async fetchAbilities() {
    //   try {
    //     const data = await axios.get(BASEURL+'ability/group-with-ability')
    //     this.abilities = data.data
    //   } catch (error) {
    //     alert(error)
    //     console.log(error);
    //   }
    // },

    async registerUser(user_data) {
      try {
      const data = await axios.post(BASEURL+'user/register', {
        "username": user_data.username,
        "password": user_data.password
      })
      console.log(data.data);
      data['status'] = true
      return data
       
      } catch (error) {
        alert(error)
        console.log(error);
      }
    },

    async loginUser(user_data) {
        try {
        const data = await axios.post(BASEURL+'token/', {
          "username": user_data.username,
          "password": user_data.password
        })
        console.log(data.data);
        return data
         
        } catch (error) {
          alert(error)
          console.log(error);
        }
      },

    // async postAbilitiy(ability_data) {
    //   try {
    //   const data = await axios.post(BASEURL+'ability/', {
    //     "subject": ability_data.subject,
    //     "group": ability_data.group_id
    //   })
    //   console.log(data.data);
       
    //   } catch (error) {
    //     alert(error)
    //     console.log(error);
    //   }
    // },

    // async getAbilities() {
    //   try {
    //     const data = await axios.get(BASEURL+'ability/')
    //     this.abilities = data.data
    //   } catch (error) {
    //     alert(error)
    //     console.log(error);
    //   }
    // }

  },
});
