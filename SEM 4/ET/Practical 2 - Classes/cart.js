class Cart
{
    constructor(userId)
    {
        this.userId = userId;
        this.items = [];
    }

    addItem(product, quantity)
    {
        this.items.push({product, quantity});
    }

    removeItem(product)
    {
        this.items = this.items.filter(item => item.product !== product);
    }
    clearCart()
    {
        this.items = [];
    }

    viewCart ()
    {
        return this.items;
    }
}

export default Cart;
