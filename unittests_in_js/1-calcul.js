// 1. Combining descriptions
function calculateNumber(type, a, b) {
    if (typeof a === 'number' && typeof b === 'number') {
        a = Math.round(a);
        b = Math.round(b);
        if (type === 'SUM') {
            return a + b;
        } else if (type === 'SUBTRACT') {
            return a - b;
        } else if (type === 'DIVIDE') {
            if (a === 0 || b === 0) {
                return 'Error';
            }
            return a / b;
        }
    }
}
module.exports = calculateNumber;
