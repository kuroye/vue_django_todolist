import { defineStore } from "pinia";

import axios from "axios";

import {BASEURL} from '@/store/urls'



// You can name the return value of `defineStore()` anything you want,
// but it's best to use the name of the store and surround it with `use`
// and `Store` (e.g. `useUserStore`, `useCartStore`, `useProductStore`)
// the first argument is a unique id of the store across your application
export const useCard = defineStore("card", {
    state: () => ({
        cards: [],
      }),
      actions: {
        async getAllCard() {
            try {
              const data = await axios.get(BASEURL+'lottery/' 
            ,   {
                params:{
                  id: user_id
                }
              }
              )
              this.cards = data.data
              
            } catch (error) {
              alert(error)
              console.log(error);
            }
          },
      }
});
