
const parseLine = require('./day01_pt1').parseLine;

test('parseLine correctly parses a line with direction and amount', () => {
    const line = "L68";
    const result = parseLine(line);
    expect(result).toEqual({ direction: "L", amount: 10 });
});