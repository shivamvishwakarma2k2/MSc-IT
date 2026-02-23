class MathOperations {
    static applyDiscount(price , percentage)
    {
        return price - (price * (percentage / 100));  // after discount price
    }
}

export default MathOperations;
