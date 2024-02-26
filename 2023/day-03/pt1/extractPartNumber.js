
const extractPartNumber = (line) =>{
    

    

    let partNubersArray = [];
    
    if(line.length == 0 || line == undefined || line == null){
        return undefined;
    }

    //Remove split string on delimiter(.) and remove empty strings
    let tokenArray = line.split(/([$@*#+%&=/.-])/).filter(el => el);



    const result = tokenArray.map(item => {
        return item.replace(/[$@*#+%&=/.-]/, '');
    }).filter(el => el);
    
    return result;
}


module.exports = extractPartNumber;
