const decreasingIndex = (line) =>{

    if(line === undefined || line === null || line.length <= 1){
        return 0;
    }
    
    let prev = line[0];

    for(let i = 1; i < line.length; i++){
        let curr = line[i];
        if (curr >= prev || prev - curr > 3) {
            return i;
        }      
        prev = curr;
    }
    return -1;
}

module.exports = decreasingIndex;