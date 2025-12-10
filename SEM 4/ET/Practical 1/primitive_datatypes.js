// 1. String
console.log("\n1. STRING");

let fullName = "Shivam Vishwakarma";

console.log("Name:", fullName);
console.log("typeof Name:", typeof fullName);

// 2. Number
console.log("\n2. NUMBER");

let rollNo = 6709;
let CGPA = 9.23;

console.log("rollNo:", rollNo, "\nCGPA:", CGPA);
console.log("typeof rollNo:", typeof rollNo, "\ntypeof CGPA:", typeof CGPA);

// 3. Boolean
console.log("\n3. BOOLEAN");

let isStudent = true;
let isMarried = false;

console.log("Is Student:", isStudent);
console.log("Is Married:", isMarried);
console.log("typeof isStudent:", typeof isStudent);
console.log("typeof isMarried:", typeof isMarried);

// 4. Undefined
console.log("\n4. UNDEFINED");

let notAssigned;
console.log("var notAssigned:", notAssigned); // undefined
console.log("typeof notAssigned:", typeof notAssigned);

// 5. Null
console.log("\n5. NULL");

let emptyValue = null;
console.log("var emptyValue:", emptyValue);
console.log("typeof emptyValue:", typeof emptyValue); // object (this is a known quirk in JavaScript)

// 6. BigInt
console.log("\n6. BIGINT");

let bigNum = 123456789012345678901234567890n;

console.log("Big Int:", bigNum);
console.log("typeof bigNum:", typeof bigNum);

// 7. Symbol
console.log("\n7. SYMBOL");

let id1 = Symbol("id");
let id2 = Symbol("id");

console.log("Symbol 1:", id1);
console.log("Symbol 2:", id2);
console.log("Are both symbols equal? (id1 === id2):", id1 === id2); // false
console.log("typeof id1:", typeof id1);