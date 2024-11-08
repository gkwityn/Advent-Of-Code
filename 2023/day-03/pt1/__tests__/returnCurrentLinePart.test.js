const returnCurrentLinePart = require('../returnCurrentLineParts');

describe("Tests to extract part numbers from current line", ()=>{
    test('Test to return no part number',()=>{
        const line = '467..114..';
        const specialCharIndex = [];
        expect(returnCurrentLinePart(line, specialCharIndex)).toEqual([]);
    });

    test('Test special char to right of first part',()=>{
        const line = '467#.114..';
        const specialCharIndex = [3];
        expect(returnCurrentLinePart(line, specialCharIndex)).toEqual([467]);
    });

    test('Test special char to right of first part',()=>{
        const line = '.67#.114..';
        const specialCharIndex = [3];
        expect(returnCurrentLinePart(line, specialCharIndex)).toEqual([67]);
    });

    test('Test special char to right of first part',()=>{
        const line = '.....114%.';
        const specialCharIndex = [8];
        expect(returnCurrentLinePart(line, specialCharIndex)).toEqual([114]);
    });

    test('Test special char to left of first part',()=>{
        const line = '$144.....';
        const specialCharIndex = [0];
        expect(returnCurrentLinePart(line, specialCharIndex)).toEqual([144]);
    });

    
    test('Test special char to left of first part',()=>{
        const line = '$144%....';
        const specialCharIndex = [0, 4];
        expect(returnCurrentLinePart(line, specialCharIndex)).toEqual([144]);
    });



    // test("", ()=>{
    // });
});
