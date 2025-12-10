// Finding element in array 

function findElementIndex(array, element) {
    for (let i = 0; i < array.length; i++) {
        if (array[i] === element)
            return i;
    }
    return -1;
}

let arr = [10, 20, 67, 104, 50];
console.log("Original Array:", arr);
console.log("104 is present at index: ", findElementIndex(arr, 104));
console.log("100 is present at index: ", findElementIndex(arr, 100));
