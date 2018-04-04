
var fname=prompt("Enter your first name")
var lname=prompt("Enter your last name")
var age=prompt("Enter your age")
var height=prompt("Enter your height(in cm)")
var petname=prompt("Enter your Pet name")
if (fname[0]===lname[0] && (20<age<30) && (height>=170) && petname[petname.length-1]==="y")
{
  console.log("You passed your spy test")
}
else {
  console.log("Fuck yourself")
}
