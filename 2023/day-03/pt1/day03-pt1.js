const { linen } = require('color-name');
const extractPartNumber = require('./extractPartNumber');

function readFile(args){
    console.log("\n--Running Day3-pt1--\n");
    
    console.log(`args: ${args}`);

    if (args.length === 2 ) {
        console.error('Expected data file!');
        process.exit(1);
    }
    else if(args.length > 3){
        console.error('Expected 1 data file argv!');
        process.exit(1);
    }
    

    const file = args[2];
    const fs = require('fs');

    try{
        const contents = fs.readFileSync(file, 'utf8');
        const lines = contents.split('\n');
        return lines;
    }
    catch(error){
        console.log(`FNF: ${error}`);
        process.exit(1);
    }
    
}

function checkPartNumber(){

}


function main(args){
    const input = readFile(args);
    // console.log(input);


    for(const line of input){
        console.log(`${line}`);
        console.log(extractPartNumber(line));
        console.log();

        // for(item of line){
        //     console.log(`\t ${extractPartNumber(line)}`);
        // }
    }

    
}


main(process.argv)

