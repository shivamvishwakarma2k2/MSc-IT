class Person {

        constructor(name, birthdate) {
        this.name = name;
        this.birthdate = new Date(birthdate); // Convert to Date object
    }

    calculateAge()
    {
        let currentYear = new Date().getFullYear();
        return currentYear = this.birthdate.getFullYear(); // Age based on birth year
    }

    getPerson()
    {
        return `Name: ${this.name}, Age: ${this.calculateAge()}`;
    }
}

export default Person; // Exporting this class for using in other files.
