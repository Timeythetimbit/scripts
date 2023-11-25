
//www.w3schools.com/js/js_intro.asp
//www.w3schools.com/js/js_whereto.asp
//www.w3schools.com/js/js_output.asp

var text = "";
var cards = ["spade", "heart", "club", "diamond"];
var number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
//var x = Math.random();
var x = Math.floor(Math.random() * 4);
var y = Math.floor(Math.random() * 13);

for (let i = 1; i < 20; i++) {
    text += "The " + i + " type of the card is " + number[y] + " " + cards[x] + "<br>";
    x = Math.floor(Math.random() * 4);
    y = Math.floor(Math.random() * 13);
}
document.getElementById("demo").innerHTML = text;