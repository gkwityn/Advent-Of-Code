
function readFile(file){
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

function playGame(line){
    //Remove the "Game #" preceeding str 
    const split = line.split(':');
    console.log('\n******************');
    console.log(`${split[0]}`);
    
    //Remove whitespace &
    //Split the game into each of the bag pulls
    const rounds = split[1].trim().split(';');

    let roundResults = {
        blue: 0,
        red: 0,
        green: 0,
        reset: function(){
            this.blue = 0;
            this.red = 0;
            this.green = 0;
        }
    };

    let roundCount = 1;
    for(let round of rounds){
        
        console.log(`\nround ${roundCount}:`);

        //Break each round down to each color
        //ex. '1 blue, 2 green'
        let colors = round.trim().split(',');

        //Increment the relevant color roundResult value
        for(color of colors){

            let pull = color.trim().split(' ');
            
            let pullColor = pull[1];
            let pullNumber = parseInt(pull[0]);
            // console.log(`color: ${pullColor}, number: ${pullNumber}`)

            switch(pullColor){
                case 'blue':{
                    if(pullNumber > roundResults.blue){
                        roundResults.blue = pullNumber;
                    }
                    
                }
                case 'green':{
                    if(pullNumber > roundResults.green){
                        roundResults.green = pullNumber;
                    }
                }
                case 'red':{
                    if(pullNumber > roundResults.red){
                        roundResults.red = pullNumber;
                    }
                }
            }
        }

        console.log(roundResults);
        roundCount++;                
    }

    // 12 red cubes, 13 green cubes, and 14 blue
    if( roundResults.red <= 12 && 
        roundResults.green <= 13 && 
        roundResults.blue <= 14){
        return parseInt(split[0].split(' ')[1]);
    }
    else{
        return 0;
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

    let results = [];
    for(const line of lines){
        results.push(playGame(line));
    }


    let sum = results.reduce((a,b) =>{
        return a + b;
    });
    console.log(`\nFinal:`);
    console.log(results);
    console.log(`total sum: ${sum}`);


}

main();
