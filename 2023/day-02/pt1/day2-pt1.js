const { green } = require('color-name');

function readFile(){
    const fs = require('fs');
    try{
        const contents = fs.readFileSync('./data-test.txt', 'utf8');
        const lines = contents.split('\n');
        return lines;
    }
    catch(error){
        console.log(`FNF: ${error}`);
        process.exit(1);
    }
    
}

function playGame(line){
    //Remove the "Game #" preceeding str 
    const split = line.split(':');
    console.log('\n******************');
    console.log(`${split[0]}`);
    
    //Remove whitespace &
    //Split the game into each of the bag pulls
    const rounds = split[1].trim().split(';');
    // console.log(bagPulls);

    roundResults = {
        blue: 0,
        red: 0,
        green: 0
    };

    for(let round of rounds){
        
        // for(let pull of round.trim()){
        //     console.log(pull);
        // };



        console.log(round);
        // let colors = pull.split(',');
        // console.log(colors);
    }
   
    
}


function main(){
    if (process.argv.length === 2 ) {
        console.error('Expected data file!');
        process.exit(1);
    }
    else if(process.argv.length > 3){
        console.error('Expected 1 data file argv!');
        process.exit(1);
    }

    const lines = readFile(process.argv[2]);
    
    for(const line of lines){
        playGame(line);
    }


}

main();
