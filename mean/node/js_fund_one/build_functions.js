function runningLogger(){
	console.log('I am running');
}

// function multiplyByTen(num){
// 	(num = num* 10)
// 	return num
// }
// console.log(multiplyByTen(5));

// var one = 'This is the first string';
// var two = 'This is the second string';

// function stringReturnOne(){
// 	console.log('This is the first string');
// }
// stringReturnOne();

// function stringReturnTwo(){
// 	console.log('This is the second string');
// }
// stringReturnTwo();

// function caller(func){
// }

// caller(runningLogger());

// function myDouble(fun1,fun2){	
// }

// myDouble(stringReturnOne(),stringReturnTwo());

// function callerTwo(arg){
// 	console.log('stating')
// 	var x = setTimeout(function(){
// 	if(typeof(arg) == 'function'){	
// 	}
// }, 6000);
// 	console.log('ending')
// 	return 'Interesting'
// }

// callerTwo(myDouble());


//<-------------------------------------
//JS fundamentals II
//<--------------------------------------
var sum =0;
function sumlimit(x,y){
	for(var i = x; i <= y; i++){
		sum = sum += i;
	}
	console.log(sum);
}
sumlimit(3,13);

//<---------------------------------------
var arr = [2,5,7,-4,-7,9];
var min = 0;

function lowest(arg){
	for(var i = 0; i < arr.length; i++){
		if (arr[i] < min){
			min = arr[i];
			
		}
		
	}
	return min;
}
console.log(lowest(arr));

//<-------------------------------------------
var arrayTwo = [2,5,7,-4,-7,9];
var avg = 0;
var sum = 0;
function average(arg){
	for(var i = 0; i < arg.length; i++){
		sum = sum += arg[i];
	}
	return avg = sum/arg.length;
}

console.log(average(arrayTwo));

//<----------------------------
var sum =0;
var sumlimit = function(x,y){
	for(var i = x; i <= y; i++){
		sum = sum += i;
	}
	console.log(sum);
}
sumlimit(3,13);

//<---------------------------------
var arr = [2,5,7,-4,-7,9];
var min = 0;

var lowest = function(arg){
	for(var i = 0; i < arr.length; i++){
		if (arr[i] < min){
			min = arr[i];
			
		}
		
	}
	return min;
}
console.log(lowest(arr));
//<--------------------------------

var avg = 0;
var sum = 0;
var avgFunction = function(arg){
	for(var i = 0; i < arg.length; i++){
		sum = sum += arg[i];
	}
	return avg = sum/arg.length;
}

console.log(avgFunction(arrayTwo));

//<------------------------------------
var arr = [2,5,7,-4,-7,9];
var objectWith = {
	limit: function(x,y){
		sum = 0;
	for(var i = x; i <= y; i++){
		 sum += i;
	}
	console.log(sum);
	},
	avgFunction:function(arg){
		sum = 0;
	for(var i = 0; i < arg.length; i++){
		 sum += arg[i];
	}
	return avg = sum/arg.length;
	},
	lowest: function(arg){
		min = 0;
	for(var i = 0; i < arr.length; i++){
		if (arr[i] < min){
			min = arr[i];	
		}
	}
	return min;
	}
	}

// objectWith.limit(4, 7);
// console.log(objectWith.avgFunction(arr));
// console.log(objectWith.lowest(arr));


var myObject = {
	name: 'Kelly',
	distance: 0,
	say_name:function(){
		console.log(myObject.name)
	},
	say_somthing:function(arg){
		if (arg = "I am cool"){
			console.log(myObject.name + " says " + arg);
		}
	},
	walk:function(){
		console.log('third function');
		(myObject.say_name());
		(myObject.distance += 3);
		console.log(myObject.name+ " walked "+ myObject.distance);
	},
	run:function(){
		console.log('forth function');
		(myObject.say_name());
		(myObject.distance += 10);
		console.log(myObject.name+ " ran "+ myObject.distance);
	},
	crawl:function(){
		console.log('fifth function');
		(myObject.say_name());
		(myObject.distance += 1);
		console.log(myObject.name+ " crawled "+ myObject.distance);
	}
}

// myObject.say_name();
// myObject.say_somthing('I am cool');
// myObject.walk();
// myObject.run();
myObject.crawl();

