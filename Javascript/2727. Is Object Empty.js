/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj){
    return Array.isArray(obj) ? obj.length === 0 ? true : false : Object.keys(obj).length === 0 ? true : false;
};

ans =  isEmpty(obj = {"x": 5, "y": 42})

console.log(ans)