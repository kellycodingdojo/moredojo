var winnings = Math.random() * 50;
winnings = Math.floor(winnings);
console.log(winnings);

var walk = 7;


function spin(coins) {


    while (coins > 0) {
        if (coins === walk) {
            console.log("you want to walk away with some change in your pocket!!");
            return;
        }
        coins--;

        var temp = Math.floor(Math.random() * 100);
        var attempt = Math.floor(Math.random() * 100);
        if (temp == attempt) {
            coins += winnings;
            console.log("You now have" + coins + "coins");
        } else {
            console.log("the number was " + temp + " and you guessed " + attempt + " you have " + coins + " coins left");
        }
        if (coins == 0) {
            console.log("You are out of coins");
            return;
        }
    }
}
spin(6);
