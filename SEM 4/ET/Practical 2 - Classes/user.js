import Person  from "./person.js"; 

class User extends Person {
    constructor(name, birthdate, email, password)
    {
        super(name, birthdate);
        this.email = email;
        this._password = password; // Private Password
        this.accountBalance = 0;

    }

    setPassword(password)
    {
        this._password = password; // Method to set the Password
    }

    checkPassword(password)
    {
        return this._password === password; // Method to check the Password
    }

    deposit(amount)
    {
        this.accountBalance += amount; // Money into the account
    }

    withdraw(amount)
    {
        if(this.accountBalance >= amount)
        {
            this.accountBalance -= amount; // withdrw money
        }
        else{
            console.log("Insuffient balance amount");
        }
    }

    getBalance()
    {
        return this.accountBalance;
    }

    getInfo()
    {
        return `Name: ${this.name} Email:${this.email} Balance:${this.accountBalance}`;
    }
}

export default User;
