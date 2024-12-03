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
    const lines = readFileLines('./data_final.txt');
    const nums = extractNumbersfromLine(lines);

    const left = nums[0];
    const right = nums[1];
    
    let results = [];

    //Find number of each value of left array is in right array
    for(item of left){
        //filter and the right array base on left item and count
        let countItem = right.filter(rightItem => rightItem === item ).length;
        results.push(item * countItem );
    }
    
    // console.log(results);
    
    let final = results.reduce((total, num) => total + num, 0);    
    console.log(final);




};

main();