const fs = require('fs');

function readFileLines(filePath) {
  const fileContent = fs.readFileSync(filePath, 'utf-8');
  const lines = fileContent.split('\n');
  return lines;
}

function substractNumbers (leftNums, rightNums){
    return rightNums.map((num, index) => num -leftNums[index] );
}

const extractNumbersfromLineAndSort = (lines) =>{
    let leftNums = [];
    let rightNums = [];
    
    lines.forEach((line, i) => {
        let nums = line.split('   ');

        leftNums.push(parseInt(nums[0]) );
        rightNums.push(parseInt(nums[1]) );
    });
    
    leftNums = leftNums.sort();
    rightNums = rightNums.sort();

    return [leftNums, rightNums];
};


const filePath = './data_final.txt';
const lines = readFileLines(filePath);

let nums = extractNumbersfromLineAndSort(lines);

let results = substractNumbers(nums[0], nums[1]);
 console.log(results);

let final = results.reduce((total, num) => total + num, 0);

console.log(final);