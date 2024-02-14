const { default: test } = require("node:test");

const testStr = "h9onektwopfour";
const str2 = "two";


let firstNumber = undefined;
let secondNumber = undefined;

const numbers = {'one': 1, 'two': 2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9
};


const isNumberWord = (str, numbers) =>{
    if(str in numbers){
        return true;
    }
    else{
        return false;
    }
};

const wordToNumber = (str, numbers) =>{
    return numbers[str];
};


for(let i = 0; i < testStr.length; i++){
    
    let substr = '';
    for(let j = i; j < testStr.length; j++){
        
        if( !isNaN(testStr[j]) ) {
            
            if(firstNumber == undefined){
                firstNumber = testStr[j];
            }
            else{
                secondNumber = testStr[j];
            }
            continue;
        }

        substr += testStr.charAt(j);
        if(isNumberWord(substr, numbers)){
            // console.log(`${substr}: True`);
            if(firstNumber == undefined){
                firstNumber = wordToNumber(substr, numbers);
            }
            else{
                secondNumber = wordToNumber(substr, numbers);
            }
            continue;
        }

    }
}

if(secondNumber == undefined){
    secondNumber = firstNumber;
}
console.log(`${testStr}`);
console.log(`first: ${firstNumber}, second: ${secondNumber}`);
console.log(`sum: ${parseInt(firstNumber) + parseInt(secondNumber)}`);



// if(str in numbers){
//     console.log( "Found");
// }
// else{
//     console.log( "Not Found");
// }

// const one = parseInt(str);
// const two = Number.parseInt(str2);

// console.log(one);