const { match } = require('assert');
const fs = require('fs');

function readFileLines(filePath) {
    
    const fileContent = fs.readFileSync(filePath, 'utf-8');
    const lines = fileContent.split('\n');
    return lines;
}

const getMultiplyPaterns = (lines) =>{
    let matched = [];

    lines.forEach(line => {
        const mul = line.match(/mul\([0-9]{1,3}\,[0-9]{1,3}\)/gm);
        matched = matched.concat(mul);
    });
    return matched;
};



// const parseMul = (expr) =>{
//     expr.match(/d{3})
// };

function main(){
    const path = require('path');
    const filePath = path.join(__dirname, 'data_final.txt');
    const lines = readFileLines(filePath);

    const matched = getMultiplyPaterns(lines);
    // console.log(matched);
    
    // matched.forEach(expr => {

    // });




}

main();