// 1. Arithmetic Operators
console.log("\n1. Arithmetic Operators");

const sum = 5 + 3;       // Addition
const diff = 10 - 2;     // Subtraction
const p = 4 * 2;         // Multiplication
const q = 8 / 2;         // Division

console.log("Arithmetic Output:", sum, diff, p, q);

// 2. Assignment Operators
console.log("\n2. Assignment Operators");

let n = 10;
n += 5;      // n = n + 5 → 15
n *= 2;      // n = n * 2 → 30
console.log("Assignment Output:", n);

// 3. Comparison Operators
console.log("\n3. Comparison Operators");

console.log("is 10 > 5 : ", 10 > 5);        // true
console.log("is 10 === '10' : ", 10 === "10");   // false (strict check)
console.log("is 10 == '10' : ", 10 == "10");   // true (not a strict check)

// 4. Logical Operators
console.log("\n4. Logical Operators");

const a = true, b = false;

console.log(a && b);   // Logical AND  → false
console.log(a || b);   // Logical OR   → true
console.log(!a);       // Logical NOT  → false

// 5. Bitwise Operators
console.log("\n5. Bitwise Operators");

const res1 = 5 & 1;   // Bitwise AND
const res2 = 5 | 1;   // Bitwise OR
const res3 = ~5;      // Bitwise NOT
const res4 = 5 ^ 1;   // Bitwise XOR

console.log("Bitwise Output:", res1, res2, res3, res4);

// 6. Ternary Operator
console.log("\n6. Ternary Operator");

const age = 18;
const status = age >= 18 ? "Adult" : "Minor";
console.log("Ternary Output:", status);

// 7. Comma Operator
console.log("\n7. Comma Operator");

let n1, n2;
const res = (n1 = 1, n2 = 2, n1 + n2);
console.log("Comma Operator Output:", res);

// 8. Unary Operators
console.log("\n8.Unary Operators");

let x = 5;
console.log(++x);   // Pre-increment → 6
console.log(x--);   // Post-decrement → prints 6, becomes 5

// 9. Relational Operators
console.log("\n9. Relational Operators");

const obj = { length: 10 };

console.log("length" in obj);       // true
console.log([] instanceof Array);   // true

// 10. BigInt Operators
console.log("\n10. BigInt Operators");
{
  const big1 = 123456789012345678901234567890n;
  const big2 = 987654321098765432109876543210n;

  console.log(big1 + big2);
}

// 11. String Operators
console.log("\n11. String Operators");
{
  const s = "Hello" + " " + "World";
  console.log(s);
}

// 12. Chaining Operator
console.log("\n12.Chaining Operator (?.)");
{
  const obj = { 
    name: "Aman", 
    address: { city: "Delhi" } 
  };

  console.log(obj.address?.city);     // Delhi
  console.log(obj.contact?.phone);    // undefined
}