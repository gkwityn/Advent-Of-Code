const { EOF } = require('dns');

require('console'); 
console

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

let main = () => {
    data = readInput();
    
    // handles \n and \r\n
    const readLines = (data) => data.split(/\r?\n/); 
    const lines = readLines(data); 

    let lineNum = 0
    for (const line of lines) {
        console.log(`Line ${lineNum++}:`);
        console.log(line);
    }
};

main();







