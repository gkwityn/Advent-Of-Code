const { count } = require('console');
const fs = require('fs');
const { argv } = require('process');

function readFileLines(filePath) {
  const fileContent = fs.readFileSync(filePath, 'utf-8');
  const lines = fileContent.split('\n');
  return lines;
}

const extractNumbersfromLine = (lines) =>{
    let leftNums = [];
    let rightNums = [];
    
    lines.forEach((line, i) => {
        let nums = line.split('   ');

        leftNums.push(parseInt(nums[0]) );
        rightNums.push(parseInt(nums[1]) );
    });
    

    return [leftNums, rightNums];
};



const main = () =>{
    const lines = readFileLines('./data_test.txt');
    const nums = extractNumbersfromLine(lines);

    const left = nums[0];
    const right = nums[1];
    
    let results = [];
    
    for (const item in left){
        let count = right.filter((item)=> left.includes(item)).length;
         results.push(item * count);
    }

    console.log(results);
    let final = results.reduce((total, num) => total + num, 0);
    
    console.log(final);




};

main();