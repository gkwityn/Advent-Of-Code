const increasingIndex = require('../increasingIndex');

describe('increasingIndex', () =>{
    test('test basic array', () => {
        const line = [1, 2, 6, 7];
        expect(increasingIndex(line)).toBe(2);
    });

    test('test basic array2', () => {
        const line = [1, 5, 6, 7];
        expect(increasingIndex(line)).toBe(1);
    });

    test('test basic array3', () => {
        const line = [1, 2, 2, 7];
        expect(increasingIndex(line)).toBe(2);
    });

    test('test basic array3', () => {
        const line = [1, 2, 2, 7];
        expect(increasingIndex(line)).toBe(2);
    });

    test('test for okay array', () => {
        const line = [1, 2, 3, 5];
        expect(increasingIndex(line)).toBe(-1);
    });

    test('test for okay array', () => {
        const line = [1, 3, 5, 7];
        expect(increasingIndex(line)).toBe(-1);
    });
});