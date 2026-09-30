/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */

var addTwoPromises = async function(promise1, promise2) {
    let val1 =  await promise1;
    let val2 =  await promise2;

    return val1 + val2;

};


ans = addTwoPromises(Promise.resolve(2), Promise.resolve(2)).then(console.log); // 4

console.log(ans)