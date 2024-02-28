const isAdjacentLeftRight = require('../isAdjacentLeftRight');

describe('Function checks if a part number is valid if a special char is adjacent left or right of given string ', ()=>{
    
    test('Returns false for empty, undefined, or null partNumber string', ()=>{
        const nullStr = null;
        const undefinedStr = undefined;
        const emptyStr = '';

        const line = '467..114..';

        expect(isAdjacentLeftRight(line, nullStr)).toEqual(false); 
        expect(isAdjacentLeftRight(line, undefinedStr)).toEqual(false); 
        expect(isAdjacentLeftRight(line, emptyStr)).toEqual(false); 
    });

    test('Returns false for empty, undefined, or null line string', ()=>{
        const partNum = '467';
        const nullStr = null;
        const undefinedStr = undefined;
        const emptyStr = '';


        expect(isAdjacentLeftRight(nullStr, partNum)).toEqual(false); 
        expect(isAdjacentLeftRight(undefinedStr, partNum)).toEqual(false); 
        expect(isAdjacentLeftRight(emptyStr, partNum)).toEqual(false); 
    });

    test('If partNumber IS NOT in line -- return false', ()=>{
        const line = '......#...';
        const partNum = '123';
        expect(isAdjacentLeftRight(line, partNum)).toEqual(false);
    });

    test.skip('If partNumber IS in line -- return true', ()=>{
        const line = '...123#...';
        const partNum = '123';
        expect(isAdjacentLeftRight(line, partNum)).toEqual(true);
    });


    test('If symbol is adjacent left of partNum -- return true', ()=>{
        const line0 = '87.114.';
        const partNum0 = 87;
        expect(isAdjacentLeftRight(line0, partNum0)).toEqual(false);

        const line = '*67..114..';
        const partNum = '67';
        expect(isAdjacentLeftRight(line, partNum)).toEqual(true);

        const line2 = '...*87.114.';
        const partNum2 = '89';
        expect(isAdjacentLeftRight(line2, partNum2)).toEqual(true);

        const line3 = '...*87.*114';
        const partNum3 = '144';
        expect(isAdjacentLeftRight(line3, partNum3)).toEqual(true);

    });
});