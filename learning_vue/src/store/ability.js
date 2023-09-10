import { defineStore } from "pinia";

import axios from "axios";

import {BASEURL} from '@/store/urls'


export const useAbilityStore = defineStore("ability", {
  state: () => ({
    abilities: [],
    // single: [],
  }),
  // getters: {
  //   getAbilities(state){
      
  //     return state.abilities
  //   }
  // },
  actions: {
    async fetchAbilities(user_id) {
      try {
        const data = await axios.get(BASEURL+'ability/group-with-ability/', {
          params: {
            user_id:user_id
          }
        })
        this.abilities = data.data
      } catch (error) {
        alert(error)
        console.log(error);
      }
    },

    async postAbilitiyGroup(group_data) {
      // console.log("I AM NAME AND ID", group_data.name);

      try {
      
      const data = await axios.post(BASEURL+'ability/group/', {
        "name": group_data.name,
        "user": group_data.user_id
      })
      console.log(data.data);
       
      } catch (error) {
        alert(error)
        console.log(error);
      }
    },

    async postAbilitiy(ability_data) {
      try {
      const data = await axios.post(BASEURL+'ability/', {
        "subject": ability_data.subject,
        "group": ability_data.group_id
      })
      console.log(data.data);
       
      } catch (error) {
        alert(error)
        console.log(error);
      }
    },

    async getAbilities(user_id) {
      try {
        const data = await axios.get(BASEURL+'ability/', {
          params:{
            user_id:user_id
          }
        })
        this.abilities = data.data
      } catch (error) {
        alert(error)
        console.log(error);
      }
    }

    // async retrieveAbilityGroup(id) {
    //   try {
    //     const data = await axios.get(BASEURL+'ability/group-with-ability/'+ id)

    //     this.single = data.data
    //     console.log(data.data);
        
        

    //     } catch (error) {
    //       alert(error)
    //       console.log(error);
    //     }
    // }

  },
});
