
let readInput = () =>{

    const fs = require('fs');
    const filePath = process.argv[2];

    if(!filePath){
        console.error("Please provide the input file path as a command line argument.");
        process.exit(1);
    }
    else{        
        try{
            const data = fs.readFileSync(filePath, 'utf8');
            return data;
        }
        catch(err){
            console.error("Error reading the file:", err);
            process.exit(1);
        }
    }        
};

const parseLine = (line) => {
    //example line: "L68"
    const parts = [line.charAt(0), line.slice(1)];
    const direction = parts[0];
    const amount = parseInt(parts[1], 10);

    return { direction, amount };
};

const moveDial = (currentPosition, move) => {
    let newPosition = currentPosition + move;

    if (newPosition > 100) {
        newPosition = 100 - (newPosition - 100);
    } else if (newPosition < 0) {
        newPosition = -newPosition;
    }

    return newPosition;
};


let main = () => {
    data = readInput();
    
    // handles \n and \r\n
    const readLines = (data) => data.split(/\r?\n/); 
    const lines = readLines(data); 


    let dialPosition = 50; 

    for (const line of lines) {
        console.log(`Line ${lineNum++}:`);
        console.log(line);
    }
};

main();


module.exports = {
    parseLine,
    moveDial
};






