const isDecreasing = require('../isDecreasing.js');

describe('isDecreasing', () =>{
    test('Returns false for null or undefined array', () =>{
        const line = undefined;
        const line2 = null;
        expect(isDecreasing(line)).toBe(false);
        expect(isDecreasing(line2)).toBe(false);        
    });

    test('Returns false for empty array', () => {
        const line = []
        expect(isDecreasing(line)).toBe(false);
    });

    test('Returns false for array of value 1', () => {
        const line = [1]
        expect(isDecreasing(line)).toBe(false);
    });

    test('Returns true for simple decending array', () => {
        const line = [10, 9, 8, 7, 6];
        expect(isDecreasing(line)).toBe(true);
    });

    test('Returns true for simple decending array', () => {
        const line = [17,14,11,8,7];
        expect(isDecreasing(line)).toBe(true);
    });

    test('Returns true for array decreasing by 2', () => {
        const line = [10, 8, 6, 4];
        expect(isDecreasing(line)).toBe(true);
    });

    test('Returns true for array decreasing by 2', () => {
        const line = [4, 2, 0];
        expect(isDecreasing(line)).toBe(true);
    });

    test('Returns true for array decreasing by 3', () => {
        const line = [10, 7, 4, 1];
        expect(isDecreasing(line)).toBe(true);
    });

    test('Returns true for array decreasing by 3', () => {
        const line = [14, 11, 8, 5];
        expect(isDecreasing(line)).toBe(true);
    });

    test('Returns false for array decreasing by 4', () => {
        const line = [10, 8, 3, 1];
        expect(isDecreasing(line)).toBe(false);
    });

    test('Returns false for array decreasing then increases', () => {
        const line = [10, 8, 9, 1];
        expect(isDecreasing(line)).toBe(false);
    });

    test('Returns false for array with repeating value', () => {
        const line = [10, 9, 9, 1];
        expect(isDecreasing(line)).toBe(false);
    });


});