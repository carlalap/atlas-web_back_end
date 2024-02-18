// const { isTypedArray } = require('util/types');
const calculateNumber = require('./1-calcul');
const assert = require('assert');


describe('calculateNumber', function() {
    it('should return the result of two numbers', function() {
        assert.equal(calculateNumber('SUM', 3, 3), 6);
        assert.equal(calculateNumber('SUBTRACT', 10, 3), 7);
        assert.equal(calculateNumber('DIVIDE', 15, 3), 5);
    });

    it('returns Error', function() {
        // assert.equal(calculateNumber('SUM', 0, 3), 'Error');
        // assert.equal(calculateNumber('SUBTRACT', 6, 0), 'Error');
        assert.equal(calculateNumber('DIVIDE', 0, 0), 'Error');
        assert.equal(calculateNumber('DIVIDE', 3.5, 0), 'Error');
      });
});
