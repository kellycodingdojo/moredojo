function prtRange(start,end,skip){
	for(var i = start; i < end; i++){
		if(skip == undefined){
			skip = 1;
		}
		if(end == undefined){
			end = start;
		}	
		if(i != skip){
			console.log(i);
		}
		
	}
}

prtRange(4,8,6);