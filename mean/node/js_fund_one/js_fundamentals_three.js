function personContructor(name){
	var newObject = {
	name : name,
	distance: 0,
	say_name: function(stuff){
		if( arg = " Is Cool")
		console.log(newObject.name + stuff);
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
		return newObject;
}
personContructor("Kelly").say_name(' Is Cool');



function ninjaContructor(name, cohort){
	var ninjaObject = {
		name: name,
		cohort: cohort,
		levels : ['white','yellow','red','brown','black'],
		curr_level: 0,
		

		levelUp:function(){
			if(ninjaObject.curr_level == ninjaObject.levels.length-1){
				console.log('you a bad mo-fo!');
			}
			else{
				ninjaObject.curr_level++;
			}
		}
	}
	return ninjaObject;
}
console.log(ninjaContructor('Noah', "ramrod" ));

var noah = ninjaContructor('Noah', "ramrod" );
console.log(noah.curr_level);
noah.levelUp();
console.log(noah.curr_level);
console.log(noah.levels[noah.curr_level]);

//<--------------------------------------------- Dojos solution
var person = {
  name : "Charlie",
  distance_traveled : 0,
  say_name : function(){
    console.log(person.name);
  },
  say_something : function(phrase){
    console.log(`${person.name} says: ${phrase}`);
  },
  walk : function(){
    console.log(`${person.name} is walking!`);
    person.distance_traveled += 3;
    return person;
  },
  run : function(){
    console.log(`${person.name} is running!`);
    person.distance_traveled += 10;
    return person;
  },
  crawl : function(){
    console.log(`${person.name} is crawling!`);
    person.distance_traveled += 1;
    return person;
  },
  chewGum:function(){
    console.log("I can walk and chew gum, but I can't chew gum and walk...");
  }
}

/* This is not the only way to do this.
  Specifically: the beltArray, and the levelUp strategy.
  Notice that the function returns an object literal and to reference/update internal object pieces we call the object by name.
*/
function ninjaConstructor(name, cohort){
  var ninja = {}
  var belts = ["yellow", "red", "black"]
  ninja.name = name;
  ninja.cohort = cohort;
  ninja.beltLevel = 0;
  ninja.levelUp = function(){
    if (ninja.beltLevel < 2){
      ninja.beltLevel += 1;
      ninja.belt = belts[ninja.beltLevel];
    }
    return ninja
  }
  ninja.belt = belts[ninja.beltLevel];
  return ninja;
}

