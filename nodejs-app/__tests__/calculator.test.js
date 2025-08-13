// __tests__/calculator.test.js
const { add, subtract } = require('../src/calculator');

describe('Calculator', () => {
  test('should add two numbers', () => {
    expect(add(3, 4)).toBe(7);
  });

  test('should subtract two numbers', () => {
    expect(subtract(5, 2)).toBe(3);
  });

  test('should handle negative numbers correctly', () => {
    expect(add(-1, -1)).toBe(-2);
  });

  test('should return 0 when subtracting a number from itself', () => {
    expect(subtract(7, 7)).toBe(0);
  });
});