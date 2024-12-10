const isDecreasing = (line) =>{

    if(line === undefined || line === null || line.length <= 1){
        return false;
    }
    
    let result = false;
    let prev = line[0];

    for(let i = 1; i < line.length; i++){
        let curr = line[i];
        if (curr >= prev || prev - curr > 3) {
            return false;
        }      
        prev = curr;
    }
    return true;
}

module.exports = isDecreasing;