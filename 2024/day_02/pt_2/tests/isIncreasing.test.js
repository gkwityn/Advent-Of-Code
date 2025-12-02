const isIncreasing = require("../isIncreasing.js");

describe("isIncreasing",() =>{

    test("Check for null or undefined", () =>{
        const line = undefined;
        expect(isIncreasing(line)).toBe(false);    
    });

    test("Empty array returns false", () =>{
        const line = [];
        expect(isIncreasing(line)).toBe(false);    
    });

    test("Return true for simple increasing array", ()=>{
        const line = [0, 1 , 3, 4];
        expect(isIncreasing(line)).toBe(true);
    });

    test('Return true for simple increasing array', () => {
        const line = [2,5,6,7,8,9,12,13];
        expect(isIncreasing(line)).toBe(true);
    });

    test("Return true for arrays increase by 2", ()=>{
        const line = [1, 3 , 5, 7];
        expect(isIncreasing(line)).toBe(true);
    });

    test("Return true for arrays increase by 3", ()=>{
        const line = [1, 4 , 7, 10];
        expect(isIncreasing(line)).toBe(true);
    });

    test("Return false for arrays with repeating value", ()=>{
        const line = [1, 4 , 4, 10];
        expect(isIncreasing(line)).toBe(false);
    });

    test("Return false for array with repeating decreasing value", ()=>{
        const line = [1, 4 , 3, 10];
        expect(isIncreasing(line)).toBe(false);
    });

    test("Return true for array with varying increasing values", ()=>{
        const line = [1, 4 , 5, 8, 10, 11, 13, 15];
        expect(isIncreasing(line)).toBe(true);
    });

    test("Return false for array with 1 value", ()=>{
        const line = [1];
        expect(isIncreasing(line)).toBe(false);
    });

});