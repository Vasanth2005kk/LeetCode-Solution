/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
let myPromise = new Promise((resolve, reject) => {
    setTimeout(resolve,millis);
});
return myPromise; 
}

let t = Date.now()
ans = sleep(100).then(() => console.log(Date.now() - t)) // 100
console.log(ans)