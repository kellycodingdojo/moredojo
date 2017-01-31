var hour = 9;
var minute = 20;
var period = "PM";

if(minute < 30 && period == "AM"){
	console.log("It's just after " + hour + " in the morning");
}

if(minute > 30 && period == "AM"){
	console.log("It's almost " + hour + " in the morning");
}

if(minute < 30 && period == "PM"){
console.log	("It's just after " + hour + " in the evening");

}

if(minute > 30 && period == "PM"){
console.log	("It's almost " + hour + " in the evening");

}