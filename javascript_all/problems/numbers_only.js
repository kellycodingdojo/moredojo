function onlyNums(arr){
	var numArr = [];
	for(var i = 0; i < arr.length; i++){
		if(typeof(arr[i]) === "number"){
			numArr.push(arr[i]);
}
	}
	console.log(numArr);
}

onlyNums([2,"hello",true,7]);


// without new array
function onlyNums(arr){
	for(var i = arr.length -1; i >= 0; i--){
		if(typeof(arr[i]) != "number"){
			arr.splice(arr[i],1);
}
	}
	console.log(arr);
}
onlyNums([2,"hello",true,7]);