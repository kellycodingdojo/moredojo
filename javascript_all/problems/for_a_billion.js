
// amount of money after (days)

function billion(days){
	var penny = .01;
	for(var i = 1; i <= days; i++){
		penny *= 2;
	}
	console.log(penny);
}

// how many days does it take 
// 21 to reach 10thousand
// 38 to reach 1billion

function tenThousand(){
	var penny = .01;
	for(var i = 1; penny <= 1000000000; i++){
		penny *= 2;
	}
	console.log(i);
	}


	// takes in infinty days to reach infinty money;