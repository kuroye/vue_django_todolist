<template>
  <div>Checked: {{ ability.abilities }}</div>

  <div v-for="_ability in abilities" :key="_ability.id">
    <input
      :id="_ability.id"
      type="checkbox"
      :value="_ability"
      v-model="ability.abilities"
      @click="onClick"
    />
    <label :for="_ability.id">
      {{ _ability.subject }}
    </label>
  </div>
</template>

<script setup>
import abilities from "../../mock_data/abilities.json";
// import {  watch } from "vue";
import { useAbility } from "@/store/ability";

const ability = useAbility();

function onClick() {
  console.log("hi", );
}

</script>

<!-- <script>
import abilities from '../../mock_data/abilities.json'

export default {
    data() {
        return {
            abilities: abilities,
            checkedAbility: []
        }
    },

    methods: {
        onClick() {
            console.log("hi", this.checkedAbility);
        }
        
    }

}

export const getCheckedAbility = () => {
    return this.checkedAbility
}
export const getAbilities = () => {
    return abilities;
}



</script> -->
