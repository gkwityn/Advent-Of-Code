const increasingIndex =(line) =>{
    if(line === undefined || line === null){
        return 0;
    }

    let result = -1;

    let prev = line[0];
    for(let i = 1; i < line.length; i++){
        let curr = line[i];
        if(curr > prev && curr - prev <= 3){
            result = -1;
        }
        else{
            return i;
        }
        prev = curr;
    }
    return result;
}

module.exports = increasingIndex;