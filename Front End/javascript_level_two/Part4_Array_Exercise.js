// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = []

// Create the functions for the tasks
// alert("Fuck off")
// ADD A NEW STUDENT
function add(data,roster){
  roster.push(data)
}


// REMOVE STUDENT
function remove(student,roster){
  le=roster.length
  for(i=0;i<le;i++)
  {
    if(roster[i]==student)
        break;
  }
  if(i==le)
    console.log("Not Found")
  else
  roster=roster.splice(i,1)
}
// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//

// DISPLAY ROSTER
function display(roster){
  console.log(roster)
}
// Create a function called display that prints out the orster to the console.


// Start by asking if they want to use the web app
var use=prompt("Want to use roster web app(yes/now)")
if(use=="yes")
{
  while(true){
    choice=prompt("Please select an option:add,remove,print,exit")
    if(choice=="add")
    {
      var name=prompt("Enter name to add:")
      add(name,roster)
    }
    else if(choice=="remove")
    {
      var name=prompt("Enter name to remove:")
      remove(name,roster)
    }
    else if(choice=="print")
    {
      display(roster)
    }
    else if(choice=="exit")
        {
          alert("Thanks for using roster app")
          break
        }
    else {
      alert("Choose valid option")
    }
  }
}
else{
  alert("Thank you")
}
// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.
