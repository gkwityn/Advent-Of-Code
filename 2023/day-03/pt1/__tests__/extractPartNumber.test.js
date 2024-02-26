const { exportAllDeclaration } = require('@babel/types');
const extractPartNumber = require('../extractPartNumber')


describe('extract Part Numbers from input line', ()=>{

    test('empty,undefined,null line/str', () => {
        const line = '';
        expect(extractPartNumber(line)).toEqual(undefined);
    });

    test('basic test case', () => {
        const line = '...11111......2313.....776868';

        expect(extractPartNumber(line)).toEqual(['11111', '2313', '776868']);
    });

    test('basic test case 2', () => {
        const line = '11111......2313.....776868....';

        expect(extractPartNumber(line)).toEqual(['11111', '2313', '776868']);
    });

    test('strip symbol from front of str', () => {
        const line = '#11111......%2313.....&776868....';

        expect(extractPartNumber(line)).toEqual(['11111', '2313', '776868']);
    });


    test('strip symbol from between strings of str', () => {
        const line = '#11111..%....%2313..#...&776868....';

        expect(extractPartNumber(line)).toEqual(['11111', '2313', '776868']);
    });

    test('Delimit with special character', () => {
        const line = '#11111%2313..#...&776868....';

        expect(extractPartNumber(line)).toEqual(['11111', '2313', '776868']);
    });
    
    

});