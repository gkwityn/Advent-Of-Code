function returnSpecialCharsIndex(inputString){
    const regex = /[$@*#+%&=/-]+/g;
    const charIndices = [];

    let match;
    while ((match = regex.exec(inputString)) !== null) {
        charIndices.push(match.index);
    }

    return charIndices;
}

module.exports = returnSpecialCharsIndex;