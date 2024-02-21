const calculateNumber = require("./0-calcul.js")
const assert = require('assert');

describe('calculateNumber', function() {
    it('Returns the sum of two rounded numbers.', function () {
        assert.equal(calculateNumber(1, 3), 4);
        assert.equal(calculateNumber(1, 3.7), 5);
        assert.equal(calculateNumber(1.2, 3.7), 5);
        assert.equal(calculateNumber(4.6, 5.7), 11);
    });

    it('Returns the sum of two negative rounded numbers.', () => {
        assert.strictEqual(calculateNumber(-1, -10), -11);
        assert.strictEqual(calculateNumber(-11.4, -38.7), -50);
      });
});    
