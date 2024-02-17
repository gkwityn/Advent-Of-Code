function readFile(){
    const fs = require('fs');
    const contents = fs.readFileSync('./data-final.txt', 'utf8');
    const lines = contents.split('\n');
    return lines;
}

function isNumber(str) {

    let getDigits = "";
    let firstLast = "";

    const numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9};
    
    for (let i = 0; i < str.length; i++) {
      if (!isNaN(str[i])) {
        getDigits += str[i]; 
      }
      else{
        let mySubstr = '';
        for(let j = i; j <str.length; j++){
            if (isNaN(str[j])){
                mySubstr += str[j];
            }
            if( mySubstr in numbers){
                
            }
        }

      }
    }
    getDigits = getDigits.trim();

    if(getDigits.length == 1){
        firstLast =  getDigits + getDigits;
    }
    else{
        firstLast = getDigits.charAt(0) + getDigits.charAt(getDigits.length-1);
    }
   return Number(firstLast);
}
  

const lines = readFile();
let numArray = [];

for (const line of lines) {
    numArray.push(isNumber(line));
}


const sum = numArray.reduce((a,b) => a+b);
console.log(`Total Sum: ${sum}`);