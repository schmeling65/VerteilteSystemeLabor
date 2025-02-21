import type {transportobjekt} from "./objectinterface"
import axios  from "axios"

export function jsonencode(toEncode:transportobjekt) {
    return JSON.stringify(toEncode)
}

export function jsondecode(toDecode:string) {
    return JSON.parse(toDecode)
}


export async function GETEntries(){
    //let teststuff = jsonencode({todo:"test1",priority:1})
    //console.log(teststuff)
    //console.log(jsondecode(teststuff))    
    //return [{todo:"test1",priority:1},{todo:"test2",priority:2}];
    const list = await axios.get(import.meta.env.VITE_REQUEST_URL+':'+import.meta.env.VITE_RQUEST_PORT+'/todos')
    /*.then((response) => {
        console.log(response)
        return jsondecode(response.data);
    } 
    )
    .catch((error) => {
        console.log(error)
        return [{todo:"test1",priority:1},{todo:"test2",priority:2}]
    }
    )*/
    return list

    
}

//Resource erstellen
export async function PUTEntry(objekt: transportobjekt){
    await axios.put(import.meta.env.VITE_REQUEST_URL+':'+import.meta.env.VITE_RQUEST_PORT+'/todos', {todo:objekt.todo,priority:objekt.priority})
    .then((response) => {
        console.log(response)
    }
    )
    .catch((error) => {
        console.log(error)
    })
}

export async function POSTEntry(objekt: transportobjekt) {
    await axios.post(import.meta.env.VITE_REQUEST_URL+':'+import.meta.env.VITE_RQUEST_PORT+'/todos/'+objekt.todo,jsonencode(objekt))
    .then((response) => {
        console.log(response)
    }
    )
    .catch((error) => {
        console.log(error)
    })

}

export async function DELETEEntry(objekt: transportobjekt) {
    await axios.delete(import.meta.env.VITE_REQUEST_URL+':'+import.meta.env.VITE_RQUEST_PORT+'/todos/'+objekt.todo)
    .then((response) => {
        console.log(response)
    }
    )
    .catch((error) => {
        console.log(error)
    })
}