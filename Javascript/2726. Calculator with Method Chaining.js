class Calculator {
    constructor(value) {
        this.total = value;
    }

    add(value) {
        this.total += value;
        return this;
    }

    subtract(value) {
        this.total -= value;
        return this;
    }

    multiply(value) {
        this.total *= value;
        return this;
    }


    divide(value) {
        if (value === 0) {
            throw new Error("Division by zero is not allowed");
        }
        this.total /= value;
        return this;
    }


    power(value) {
        this.total **= value;
        return this;
    }

    getResult() {
        return this.total;
    }
}

const cal = new Calculator(10);

cal.add(10);
cal.subtract(5);

console.log(cal.getResult()); // 15
