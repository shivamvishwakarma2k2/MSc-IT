import MathOperations from "./mathOperations.js";

class Order {
    constructor(orderID, userID){
        this.orderID = orderID;
        this.userID = userID;
        this.products = [];
        this.totalAmount = 0;
    }

    addProduct(product, quantity)
    {
        if(product.quantity >= quantity)
        {
            this.products.push({product, quantity});
            this.totalAmount += product.price * quantity; // calculate total order amount
            product.quantity -= quantity; // Reduce the stock after adding
        }
        else{
            console.log("out of stock");
        }
    }

    calculateTotal()
    {
        return this.totalAmount;
    }

    completeOrder(user)
    {
        let discountedPrice = MathOperations.applyDiscount(this.totalAmount, 10);
        if (user.getBalance()>= discountedPrice)
        {
            user.withdraw(discountedPrice); // money withdraw from user acc
            console.log(`Order ${this.orderID} completed with discounted price: ${discountedPrice}`);

        }
        else
        {
            console.log("Insuffient balance amount after discount");
        }

    }
}

export default Order;
