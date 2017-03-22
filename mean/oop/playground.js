// var MyObjConstructor = function(name){
//   var myPrivateVar = "Hello"; // just to show that it is hard to see this private var easily
//   this.name = name; // but you can see the name!
//   this.method = function(){
//     console.log( "I am a method");
//   };
// }
// var obj1 = new MyObjConstructor('object1');
// var obj2 = new MyObjConstructor('object2');
// console.log(obj1);

//<<------------------------------------------------------------------------

// obj1.newProperty = "newProperty!";
// obj1.__proto__.anotherProperty = "anotherProperty!";
// console.log(obj1.anotherProperty); // anotherProperty!
// console.log(obj1.newProperty); // newProperty!
// // What about obj2?
// console.log(obj2.newProperty); // undefined
// console.log(obj2.anotherProperty); 


// //simulated really slow DB call.
// function getStuffFromDatabase(callback){
//   var data;
//   var myTimer = setTimeout(function(){
//     if (typeof(callback) == 'function'){
//       //it just got back from the DB!
//       data = [{name:'Todd'},{name:'Michael'},{name:'Portia'}];
//       callback(data);
//     }
//   }, 10000);
//   // it takes 10 seconds to get anything back <- you should fix your cloud server.!!!
//   return data;
// }    
// //simulated request (failing);
// function requestDataFromDatabase(){
//   var data = getStuffFromDatabase(); // this should return my data right??
//   console.log(data);
// }
// function catchFly(){
//   console.log('I just caught a fly!');
// }
// requestDataFromDatabase();
// // keep running my program!
// console.log('Hello');
// catchFly();
// //etc.

//simulated really slow DB call.
function getStuffFromDatabase(callback){
  var data;
  var myTimer = setTimeout(function(){
    if (typeof(callback) == 'function'){
      data = [{name:'Todd'},{name:'Michael'},{name:'Portia'}];
      callback(data);
    }
  }, 10000);
  return data;
}    
// ************CHANGES HERE **************
function requestDataFromDatabase(){
  var data = getStuffFromDatabase(function myCallback(data){ // ooh shiny callback!.. when is it invoked???
    console.log(data, "ASynchronous");
    for (var i = 0; i < data.length; i ++){
      console.log(data[i].name);
    }
  });
  console.log(data, "Synchronous");
}
//***************** END CHANGES **********************
function catchFly(){
  console.log('I just caught a fly!');
}
requestDataFromDatabase();
// keep running my program!
console.log('Hello');
catchFly();
//etc.