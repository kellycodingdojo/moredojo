function setColor(color){
  if(color = "blue"){
    return "red";
  }
  else{
    return "blue";
  }
}
$(document).ready(function(){
  $("button").click(function(){
    $(this).toggleClass("red");
  })
  $("button").hover(function(){
    $(this).addClass("green");
  }, function(){
    $(this).removeClass("green");
  })
})
