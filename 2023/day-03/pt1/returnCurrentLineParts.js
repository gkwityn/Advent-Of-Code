const returnCurrentLinePart = (line, specialCharIndex) =>{
    
    let partNumbers = [];
    for (const index of specialCharIndex) {

        //check left
        let leftNum = '';
        let i = index - 1;

        while (i >= 0 && !isNaN(parseInt(line[i], 10))) {
            leftNum += line[i];
            i--;
        }
        if(leftNum.length != 0){
            partNumbers.push(parseInt(leftNum.split('').reverse().join(''), 10));
        }
        

        //check right
        i = index + 1;
        let rightNum = '';
        while (i < line.length-1 && !isNaN(parseInt(line[i], 10))) {
            rightNum += line[i];
            i++;
        }
        if(rightNum.length != 0){
            partNumbers.push(parseInt(rightNum));
        }
        
    }



    
    // for (index of SpecialCharIndex){
    //     //Check left of special character
    //     let leftNum = '';
    //     index--;

    //     while(index >= 0 && !isNaN(parseInt(line[index], 10))){
    //         leftNum += line[index];
    //     }
    //     partNumbers.push(leftNum);
    //     //Check right of special character
    // }

    return partNumbers;
}

module.exports = returnCurrentLinePart;