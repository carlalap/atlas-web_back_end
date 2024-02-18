// const { isTypedArray } = require('util/types');
const chai = require('chai');
const expect = chai.expect;

const calculateNumber = require('./2-calcul_chai.js');


describe('calculateNumber', function() {
    it('should return the result of two numbers', function() {
        expect(calculateNumber('SUM', 3, 3)).to.equal(6);
        expect(calculateNumber('SUBTRACT', 10, 3)).to.equal(7);
        expect(calculateNumber('DIVIDE', 15, 3)).to.equal(5);
    });

    it('returns Error', function() {
        // assert.equal(calculateNumber('SUM', 0, 3), 'Error');
        // assert.equal(calculateNumber('SUBTRACT', 6, 0), 'Error');
        expect(calculateNumber('DIVIDE', 0, 0)).to.equal('Error');
        expect(calculateNumber('DIVIDE', 3.5, 0)).to.equal('Error');
    });
});
