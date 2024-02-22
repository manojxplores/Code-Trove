// promises --->For parallel execution

let p = new Promise(function(resolve, reject){
    let a = 1 + 1
    if(a == 2){
        resolve('success')
    }else{
        reject('failed')
    }
})

p.then((message) => {
    console.log('in then ' + message)
}).catch((message)=>{
    console.log('in catch ' + message)
})