// Pass by value : Double the each element of array

function doubleValue(array) {
    var result = [];
    for (let i = 0; i < array.length; i++) {
        result.push(array[i] * 2);
    }
    return result;
    // OR  
    // return array.map(value => value * 2);
}

var arr = [2, 4, 6, 4];
console.log("Original Array:", arr);
console.log("Doubled Array:", doubleValue(arr))