
function howMany(days){
	for(var i = days; i >= 0; i--){
		if(i > 30){
			console.log(i, "days until my birthday. Such a long time... :()");
		}
		 if(i < 30 && i > 5){
			console.log(i, "Days, Getting CLoser!");
		}
		 if( i < 5 && i > 0){
			console.log(i, "DAYS UNTIL MY BIRTHDAY!!!");
		}
		if( i == 0){
			console.log("Happy Birthday");
		}
	}
}