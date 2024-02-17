function isNumberWord(str, numbers) {
    // Ensure numbers is a valid object and handle potential errors
    if (!numbers || typeof numbers !== 'object') {
      throw new TypeError('Invalid numbers object provided.');
    }
  
    const keys = Object.keys(numbers);
  
    return keys.some(key => str.indexOf(key) !== -1);
  }



const wordToNumber = (str, numbers) =>{
    return numbers[str];
};





function getSumOfString(str) {
    let line = str.trim();
    let firstNumber = undefined;
    let secondNumber = undefined;

    const numbers = {'one': "1", 'two': "2", 'three': "3", 'four':"4", 'five':"5", 'six':"6", 'seven':"7", 'eight':"8", 'nine':"9"
    };

    for(let i = 0; i < line.length; i++){
    
        let substr = '';
        for(let j = i; j < line.length; j++){
            
            if( !isNaN(line[j]) ) {
                
                if(firstNumber == undefined){
                    firstNumber = line[j];
                }
                else{
                    secondNumber = line[j];
                }
                break;
            }
            else{
                substr += line.charAt(j);
                if(isNumberWord(substr, numbers)){
    
                    if(firstNumber == undefined){
                        firstNumber = wordToNumber(substr, numbers);
                    }
                    else{
                        secondNumber = wordToNumber(substr, numbers);
                    }
                    break;
                }
            }
    
            
    
        }
    }
    
    if(secondNumber == undefined){
        secondNumber = firstNumber;
    }
    console.log('***********************')
    console.log(`${line}`);
    console.log(`first: ${firstNumber}, second: ${secondNumber}`);
    let returnStr = firstNumber+secondNumber;
    console.log(`concat: ${returnStr}`);
    
    return parseInt(returnStr);
    
}

let str = 'abcone2threexyz';
getSumOfString(str);