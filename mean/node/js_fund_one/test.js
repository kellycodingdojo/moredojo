//console.log('yo yo yo');

// var my_first_variable;
// my_first_variable = 'Data';
// console.log(my_first_variable);
// console.log(typeof(my_first_variable));

// console.log(a);
// var a = 'weird';

// console.log(typeof(b));
// var b = 'weird too';
// console.log(typeof(b));

// <-----------------------------------
// var arr = [3,6];
// arr[2] = 'hi';
// console.log(arr.length);
// console.log(arr[34]);
// arr.length = 3;
// console.log(arr[34]);
// console.log(arr[234]);
// console.log(arr.length);
// arr.length = 500;
// console.log(arr[2]);
// console.log(arr.length);

//<--------------------------------------
// var ninja = {
//   name:'Susanna',
//   MEAN_belt:10,
//   iOS_belt:10,
//   python_belt:10,
//   php_belt:9, // she hadn't mastered deploying yet!
//   ruby_belt:9.75 // done in 1.5 hrs though!
// }
// for (var key in ninja) {
//   if (ninja.hasOwnProperty(key)) {
//     console.log(key);
//     console.log(ninja[key]);
//   }
// }


//<---------------------------------
// var array = [ function(){console.log('hello there');} ]
// console.log(array[0]())

// var object = { helloFunc: function(){console.log('hello there')}};
// console.log(object)



//<------------------------
// var dojo = {};                                 // creates an empty object
// dojo = {
//   name: 'Coding Dojo',                         // property can store a string
//   number_of_students: 25,                      // property can store a number
//   instructors: ['Andrew', 'Michael', 'Jay'],   // property can store arrays
//   location: {                                  // property can even store another object!
//     city: 'San Jose',
//     state: 'CA',
//     zipcode: 95112
//   }
// }                                              // access object properties with dot (.) notation
// console.log(dojo.name, dojo.number_of_students, dojo.instructors, dojo.location);
// console.log(dojo["name"]);                     // or bracket [] notation (note: specify key in quotes)
// dojo.number_of_students = 40;                  // we can reassign any of the properties
// dojo.location.city = "Bellevue";
// dojo.location.state = "Washington";
// dojo.location.zipcode = "unknown";             // note that we can change this from integer to string
// dojo.phone_number = 1234567890 ;
//<---------------------------------


var ninja = {
  name:'Susanna',
  MEAN_belt:10,
  iOS_belt:10,
  python_belt:10,
  php_belt:9, // she hadn't mastered deploying yet!
  ruby_belt:9.75 // done in 1.5 hrs though!
}
for (var key in ninja) {
  if (ninja.hasOwnProperty(key)) {
    console.log(key);
    console.log(ninja[key]);
  }
}



var array = [ function(){console.log('hello there');} ]
console.log(array[0]())

var object = { helloFunc: function(){console.log('hello there')}};
console.log(object)




"use strict" // you may (some interpreters do, some don't) require this statement before ES2015 is used.
var myVariable = () => { console.log('hello'); }
myVariable();

