 const isAdjacentLeftRight = (line, key) =>{

    //Defensive check if line or key are invalid passed parameters.
    if(key == null || key == undefined || key == ''){
        return false;
    }
    else if(line == null || line == undefined || line == ''){
        return false;
    }

    //If key is in line...
    if (line.includes(key) ){
        
        //Check if symbol is adjacent left of partNum
        if(line.indexOf(key) === 0){
            return false;
        }
        else{
            const regex = new RegExp('/[$@*#+%&=/-]/');
            if( regex.test( line.charAt(line.indexOf(key)-1)) ){
                return true;
            }
                
        }

    }


    return false;
};

module.exports = isAdjacentLeftRight;