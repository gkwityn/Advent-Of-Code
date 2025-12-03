


let readInput = () =>{

    const fs = require('fs');

    const filePath = process.argv[2];

    if(!filePath){
        console.error("Please provide the input file path as a command line argument.");
        console.log(`\n--- Reading data from: ${filePath} ---`);
        console.log('File Content:');
        console.log(fileContent);
        console.log('--------------------------------------\n');
        process.exit(1);
    }

    try{
        const data = fs.readFileSync(filePath, 'utf8');
        return data;
    }
    catch(err){
        console.error("Error reading the file:", err);
        process.exit(1);
    }
};
