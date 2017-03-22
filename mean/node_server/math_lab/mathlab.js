
var mylib = require("./apps")();
var math =  mylib; 

a = 1;
b = 35;

console.log(math)
console.log("\nSum of " + a + " and " + b + " is: ", mylib.add(a, b));
console.log("Product of " + a + " and " + b + " is: ", mylib.multiply(a, b));
console.log("Square of " + a + " is: ", mylib.square(a));
console.log("Random number between " + a + " and " + b + ": ", mylib.random(a, b));


