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

const parseMul = (expr) =>{
    const [a, b] = expr.match(/[0-9]{1,3}/gm);
    return [a, b];
}

const multiply = (a, b) => a * b;



function main(){
    const path = require('path');
    const filePath = path.join(__dirname, 'data_final.txt');
    const lines = readFileLines(filePath);

    const matched = getMultiplyPaterns(lines);    
    const parsed = matched.map(parseMul);
    const sum = parsed.reduce((acc, pair) => {
        acc + multiply(...pair)
    }, 0);

    console.log(`The total is: ${sum}`);
}

main();