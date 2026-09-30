/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    var value = init;
    var increment = function(){
        return ++value ;
    }
    var reset = function(){
        value = init;
        return value;
    }

    var decrement = function(){
        return --value;

    }
    
    return {
        increment : increment,
        reset : reset,
        decrement : decrement 
    }
};

const counter = createCounter(5)
ans = counter.increment(); // 6
console.log(ans)

ans = counter.reset(); // 5
console.log(ans)

ans = counter.decrement(); // 4
console.log(ans)
