const { log } = require('console');
const fs = require('fs');
const { getSystemErrorMap } = require('util');

const isIncreasing = require('./isIncreasing.js');
const isDecreasing = require('./isDecreasing.js');

function readFileLines(filePath) {
    
    const fileContent = fs.readFileSync(filePath, 'utf-8');
    const lines = fileContent.split('\n');
    return lines;
}

function checkLevels(stringArray){
    const line = stringArray.map(Number);

    let count = 0;

    let output = '';
    if(isIncreasing(line) || isDecreasing(line)){
        output = `Safe: ${line}`
        count++;
    }  
    else {
        output = `Unsafe: ${line}`
    }
    console.log(output);

    return count;
}



function main(){
    // const filePath = './data_test.txt';

    const path = require('path');
    const filePath = path.join(__dirname, 'data_final.txt');
    const lines = readFileLines(filePath);


    let finalCount = 0;
    lines.forEach(line => {
        finalCount += checkLevels(line.split(' '));
    });

    console.log(`\nFinal count: ${finalCount}`);
}

main();