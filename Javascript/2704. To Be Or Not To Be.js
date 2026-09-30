/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {

    var ftoBe = function(n) {
        if (val === n) {
            return true;
        } else {
            throw new Error("Not Equal");
        }
    };

    var fnotToBe = function(n) {
        if (val !== n) {
            return true;
        } else {
            throw new Error("Equal");
        }
    };

    return {
        toBe: ftoBe,
        notToBe: fnotToBe
    };
};

ans = expect(5).toBe(5); // true
console.log(ans)

ans = expect(5).notToBe(5); // throws "Equal"
console.log(ans)
