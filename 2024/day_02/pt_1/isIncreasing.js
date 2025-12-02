const isIncreasing =(line) =>{
    if(line === undefined || line === null){
        return false;
    }

    let result = false;

    let prev = line[0];
    for(let i = 1; i < line.length; i++){
        let curr = line[i];
        if(curr > prev && curr - prev <= 3){
            result = true;
        }
        else{
            return false
        }
        prev = curr;
    }
    return result;
}

module.exports = isIncreasing;