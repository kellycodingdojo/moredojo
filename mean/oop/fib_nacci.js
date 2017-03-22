// function fib(num) {
//   this.fibby = 0;
//   this.runner = 1;
//   function nacci() {
//    console.log(runner)
//    	var temp = fibby;
//    	fibby =runner;
//    runner = runner + temp
//   }
//   return nacci
// }
// var fibCounter = fib();
// fibCounter() // should console.log "1"
// fibCounter() // should console.log "1"
// fibCounter() // should console.log "2"
// fibCounter() // should console.log "3"
// fibCounter() // should console.log "5"
// fibCounter() // should console.log "8"
// fibCounter()
// fibCounter()




//<---------------------------------------------------------
// bonus
function ninjaBelt(ninja){
  return function belt(beltColor){ //note the closure here!
    console.log("Ninja "+ ninja + " has earned a " + beltColor +" belt.");
  }
}

ninjaBelt('Eileen')('black');





//<<---------------------------------dojo solution

// function fib() {
//  var prev = 0;
//  var curr = 1;
//  function nacci() {
//    console.log(curr);
//    var temp = prev;
//    prev = curr;
//    curr = curr + temp;
//  }
//  return nacci
// }
// var fibCounter = fib();
// fibCounter() // should console.log "1"
// fibCounter() // should console.log "1"
// fibCounter() // should console.log "2"
// fibCounter() // should console.log "3"
// fibCounter() // should console.log "5"
// fibCounter() // should console.log "8"

