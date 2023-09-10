export function getRandomInt(max) {
    let num = Math.floor(Math.random() * max)
    if(num==0){
        num+=1
    }
    return num;
  }