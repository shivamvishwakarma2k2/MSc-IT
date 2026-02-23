// Flatten the nested array

function flattenArray(nestedArray) {
    let result = [];

    for (let element of nestedArray) {
        if (Array.isArray(element)) {
            result = result.concat(flattenArray(element));
        }
        else {
            result.push(element);
        }

    }
    return result;
}

let nestedArray = [1, [2, 3], [4, [5]]];
let flattenArrayResult = flattenArray(nestedArray);

console.log("Original Array:", nestedArray);
console.log("Flatten Array:", flattenArrayResult);
