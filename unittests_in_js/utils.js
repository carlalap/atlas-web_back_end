// utils.js
const Utils = {
    calculateNumber: function(type, a, b) {
      switch (type) {
        case 'SUM':
          return a + b;
        case 'SUBTRACT':
          return a - b;
        case 'DIVIDE':
          return a / b;
        default:
          return 'Error';
      }
    }
  };
  
  module.exports = Utils;
