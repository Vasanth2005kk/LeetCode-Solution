/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    let count  = 0 
    args.forEach((values)=>{
        count++
    })
    return count
};

console.log(argumentsLength(1, 2, 3)); // 3
