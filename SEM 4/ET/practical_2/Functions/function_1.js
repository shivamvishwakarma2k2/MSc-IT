// Default Parameter

function calculateTotal(price, discount = 0.1) {
    let discountedPrice = price - (price * discount) / 100;
    return discountedPrice;
}

console.log("Calculate Total with Custom Parameter:");
console.log(calculateTotal(1000, 0.5));

console.log("\nCalculate Total with Default Parameter:");
console.log(calculateTotal(1000));