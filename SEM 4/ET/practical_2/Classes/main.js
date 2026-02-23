import User from "./user.js";
import Product from "./product.js";
import Order from "./order.js";
import Cart from "./cart.js";
import MathOperations from "./mathOperations.js";

//Create a user

let user1 = new User("Shivam Vishwakarma", "2002-12-06", "Shivam@abc.com", "1234678");
user1.deposit(2000);
console.log(user1.getInfo());
console.log();

// Create a products 
let product1 = new Product("Laptop", 500, 10);
let product2 = new Product("Phone", 300, 20);

let order1 = new Order(1, user1.email);
order1.addProduct(product1, 1);
order1.addProduct(product2, 2);
console.log("Total order amount", order1.calculateTotal());
console.log();

// Apply discount to total amount
let discountedPrice = MathOperations.applyDiscount(order1.calculateTotal(), 10);
console.log("Discounted Price: ", discountedPrice);
console.log();

//Complete the order]
order1.completeOrder(user1);
console.log(user1.getInfo());
console.log();

//View uupdated stock price

console.log(`Updated stock of ${product1.name}: ${product1.getStock()}`);
console.log(`Updated stock of ${product2.name}: ${product2.getStock()}`);
console.log();

//Create a shopping cart and add/remove items
let cart = new Cart(user1.email);
cart.addItem(product1, 1);
cart.addItem(product2, 2);
console.log("Items added to cart");
console.log(cart.viewCart());
cart.removeItem(product1);
console.log();
console.log("Updated !!!");
console.log(cart.viewCart());
