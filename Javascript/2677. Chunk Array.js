/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    if (arr.length==0){
        return arr
    }
    var data = []
    var ematy = []
    arr.forEach((items)=>{
    ematy.push(items)
    if (ematy.length == size){
        data.push(ematy)
        ematy = []
    }
    })
    if(ematy.length !== 0){
    data.push(ematy)

    } 
    return data
};

arr = [1,2,3,4,5]
size = 1

ans = chunk(arr,size)
console.log(ans)