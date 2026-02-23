// 1. Object
console.log("\n1. OBJECT");

let person = { name: "Shivam Vishwakarma", age: 23 };
console.log("Object Output:", person);

// 2. Array
console.log("\n2. ARRAY");

let colors = ["red", "yellow", "blue", "green", "cyan"];

console.log("Array Output:", colors);
console.log("Accessing 1st element:", colors[0]); // red
console.log("Accessing 2nd element:", colors[1]); // yellow
console.log("Accessing 5th element:", colors[4]); // cyan
console.log("Accessing 6th element:", colors[5]); // undefined

// 3. Date
console.log("\n3. DATE");

let today = new Date();
console.log("Date Output:", today);

// 4. Regular Expression (RegExp)
console.log("\n4. REGEXP");

let regex = /hello/;
let result = regex.test("hello world");
console.log("RegExp Output:", result);

// 5. Map
console.log("\n5. MAP");
{
    let personMap = new Map();

    personMap.set("name", "Shivam Vishwakarma");
    personMap.set("age", 23);

    console.log("Map Output:");
    console.log("Name:", personMap.get("name"));
    console.log("Map Size:", personMap.size);

    console.log("\nFull Map Entries:");
    for (let [key, value] of personMap) {
        console.log(`${key} => ${value}`);
    }
}

// 6. Set
console.log("\n6.SET");
{
    let arr = [1, 2, 2, 3, 4, 4, 5];
    let uniqueArr = [...new Set(arr)];

    console.log("Set Output:", uniqueArr);
}