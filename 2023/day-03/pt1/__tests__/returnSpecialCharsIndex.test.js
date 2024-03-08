const returnSpecialCharsIndex = require('../returnSpecialCharsIndex');

describe('Function to find and return array of instances of special characters',()=>{
    // test('',()=>{
    // });

    test('no symbols found returns undefined', ()=>{
        const line = '467..114..';
        expect(returnSpecialCharsIndex(line)).toEqual([]);
    });

    test('%67..114..',()=>{
        const line = '%67..114..';
        expect(returnSpecialCharsIndex(line)).toEqual([0]);

    });

    test('%67..114..',()=>{
        const line = '%67..114..';
        expect(returnSpecialCharsIndex(line)).toEqual([0]);

    });

    test('%67.$.114.*.',()=>{
        const line = '%67.$.114.*.';
        expect(returnSpecialCharsIndex(line)).toEqual([0,4,10]);
    });

    test('%67.$.1%14.*.',()=>{
        const line = '%67.$.1%14.*.';
        expect(returnSpecialCharsIndex(line)).toEqual([0,4,7,11]);
    });

    test('67..114*',()=>{
        const line = '67..114*';
        expect(returnSpecialCharsIndex(line)).toEqual([7]);
    });

    

    // test('',()=>{
    // });
})
