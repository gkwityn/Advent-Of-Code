const { linen } = require('color-name');

function readFile(args){
    console.log("Running Day3-pt1");
    console.log(args);

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
    console.log(input);


    for(let line = 0; line < input.length; i++){
        if(line == 0){
            
        }
    }

    
}


main(process.argv)

