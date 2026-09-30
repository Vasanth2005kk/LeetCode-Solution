/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let Count =  n -1
    return function() {
        Count ++;
        return Count
    };
};

 
const counter = createCounter(10)
console.log(counter()) // 10
console.log(counter()) // 11
console.log(counter()) // 12
