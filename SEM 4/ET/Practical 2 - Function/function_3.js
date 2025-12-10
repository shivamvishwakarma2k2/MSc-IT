// Write a function updatePersonImmutable(person) that takes an object as input, creates a copy of it, 
// updates a property, and returns a the new object without modifying the original.

function updatePersonImmutable(person, updates) {
    return { ...person, ...updates };
}

const person = { name: "Shivam Vishwakarma", age: 23 };

const updatedPerson = updatePersonImmutable(person, { city: "Mumbai" });
console.log("Original: ", person);
console.log("Updated: ", updatedPerson);