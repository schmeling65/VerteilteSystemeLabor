<script lang="ts">
import WelcomeItem from "./WelcomeItem.vue";
import { defineComponent } from "vue";
import {GETEntries, PUTEntry,POSTEntry,DELETEEntry, jsondecode,jsonencode} from "../router/RESTController";
import type {transportobjekt} from "../router/objectinterface"
export default defineComponent({
  data() {
    return {
      items: [] as transportobjekt[],
    }
  },
  mounted() {
    console.log(import.meta.env)
    GETEntries().then((result)=> {
        console.log(result)
        //this.items = jsondecode(result.data)
        this.items = result.data
      })
  },
  methods: {
    SendPost(_ID:transportobjekt) {
      POSTEntry(_ID)
    },
    SendPut(_ID:transportobjekt) {
      PUTEntry(_ID)
      GETEntries().then((result)=> {
        //this.items = jsondecode(result.data)
        this.items = result.data
      })
      //PUTEntry(transobjekt as transportobjekt)
    },
    SendPutPost() {
      let stringinput = document.getElementById("NewText")?.innerHTML
      let prioinput = document.getElementById("NewPriority")?.innerHTML
      let transobjekt = {todo: stringinput?.replace("<br>","") as string, priority: parseInt(prioinput?.replace("<br>","") as string)}
      for (let item of this.items) {
        console.log(item.todo)
        console.log(transobjekt.todo)
        console.log("--------")
        if (item.todo == transobjekt.todo) {
          this.SendPut(transobjekt)
          GETEntries().then((result)=> {
        //this.items = jsondecode(result.data)
        this.items = result.data
      })
          return
        }
      }
      this.SendPost(transobjekt)
      //this.items.push(transobjekt)
      //this.items = GetEntries()
      GETEntries().then((result)=> {
        //this.items = jsondecode(result.data)
        this.items = result.data
      })

    },
    SendDelete(_ID:transportobjekt) {
      DELETEEntry(_ID)
      GETEntries().then((result)=> {
        //this.items = jsondecode(result.data)
        this.items = result.data
      })
    }
  }
})
</script>

<style scroped>
li {
list-style-type: none; /* Remove bullets */
  padding: 0; /* Remove padding */
  margin: 0; /* Remove margins */
}

.object {
  position: relative;
  display: flex;
  border: 3px solid white;
}
.priority {
  position: relative;
  float: left;
  margin: 5px;
  font-size: 35px;
  margin-right: 50px;
}
.text {
  position: relative;
  margin: 5px;
  font-size: 35px;
  margin-right: 35px
}

button {
  margin: auto;
  margin-right: 10px;
  font-size: 40px;
  color: white;
  background: none;
  border: none;
}
button:hover {
  cursor: pointer;
}

#add {
  font-size: 70px;
  color: white;
  margin: 0 auto;
  display: block;
}

#NewText{
  font-size:20px;
color:black;
background-color: white;
margin:auto;
margin-top: 5px;
}

#NewPriority{
  font-size:20px;
color:black;
background-color: white;
margin:auto;
margin-top: 5px;
}

#EditField{
  font-size:20px;
color:black;
background-color: white;
margin:auto;
margin-top: 5px;
display:flex;
}

</style>

<template>
  <WelcomeItem>
  <li>
    <div class="object" v-for="item in items">
    <div class="priority">{{item.priority}}</div>
    <div class="text">{{item.todo}}</div>
    <!--<button @click="SendPost(item)">
      Edit
    </button>-->
    <button @click="SendDelete(item)">
      Delete
    </button>
  </div>
</li>
<div id="NewText" contenteditable="true">ToDo-Element</div>
<!--<div id="EditField" contenteditable="true">ToDo-Element-Edit</div>-->
<div id="NewPriority" contenteditable="true">Priorität</div>
<button id="add" @click="SendPutPost()">
  Add/Edit
</button>
</WelcomeItem>
</template>
