function readFile(){
    const fs = require('fs');
    const contents = fs.readFileSync('./data-final.txt', 'utf8');
    const lines = contents.split('\n');
    return lines;
}

function isNumber(str) {

    let getDigits = "";
    let firstLast = "";
    
    for (let i = 0; i < str.length; i++) {
      if (!isNaN(str[i])) {
        getDigits += str[i]; 
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

console.log(numArray);
console.log(numArray[numArray.length-1]);

const sum = numArray.reduce((a,b) => a+b);
console.log(`Total Sum: ${sum}`);