// Rotating the array

function rotateArray(arr, steps) {
    steps = steps % arr.length;
    return arr.slice(-steps).concat(arr.slice(0, -steps));
}

let array = [6, 7, 0, 4];
let rotateArrayVal = rotateArray(array, 2);

console.log("Original Array:", array);
console.log("Rotated Array:", rotateArrayVal);