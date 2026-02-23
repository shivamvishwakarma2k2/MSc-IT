let person = {
    firstName: "Shivam",
    lastName: "Vishwakarma",
    age: 23,
    hobbies: ["Coding", "Reading", "Traveling", "Music"],
    address: {
        area: "Vikhroli(W)",
        city: "Mumbai",
        zip: 400083
    }
};

console.log("\nUsing Dot notation for accessing\n");
console.log("Name:" + person.firstName + " " + person.lastName);
console.log("Address:" + person.address.area + " " + person.address.city + " " + person.address.zip);

console.log("\nUsing Square for accessing\n");
console.log("Name:" + person["firstName"] + " " + person["lastName"]);
console.log("Address:" + person["address"]["area"] + " " + person["address"]["city"] + " " + person["address"]["zip"]);