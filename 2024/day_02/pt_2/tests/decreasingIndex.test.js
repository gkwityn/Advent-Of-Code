const decreasingIndex = require('../decreasingIndex');

describe('', ()=>{

    test('test simple array', () => {
        const line = [10, 5, 1];
        expect(decreasingIndex(line)).toBe(1);
    });

    test('test simple array', () => {
        const line = [10, 9, 8, 4];
        expect(decreasingIndex(line)).toBe(3);
    });


    test('test simple array', () => {
        const line = [10, 7, 4, 0];
        expect(decreasingIndex(line)).toBe(3);
    });

    test('test simple array', () => {
        const line = [10, 9, 8, 7];
        expect(decreasingIndex(line)).toBe(-1);
    });
});