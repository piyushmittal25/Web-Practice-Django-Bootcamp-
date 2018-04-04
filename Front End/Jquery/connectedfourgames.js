var playerone=prompt("Player One: Enter Your Name,you will be Blue");
var playertwo=prompt("Player Two: Enter Your Name,you will be Red");
$("h3").text(playerone+":it is your turn,please pick a column to drop your blue chip.");
var color=["blue","red"]
var lastcolor=1
var matrix=[[null,null,null,null,null,null,null],[null,null,null,null,null,null,null],[null,null,null,null,null,null,null],[null,null,null,null,null,null,null],[null,null,null,null,null,null,null],[null,null,null,null,null,null,null]]
var currentposition=[5,5,5,5,5,5,5]
var move_count=0
var stop_game=false

function horizontal(row,column)
{
  var flag;
  for(var i=0;i<4;i++)
  {
    flag=true
    if(matrix[row][i]===null)
      flag=false
    for(var j=i;j<i+4;j++)
    {
      if(matrix[row][i]!==matrix[row][j])
        {
          flag=false;
          break;
        }
    }
    if(flag===true)
      break
  }
  return flag
}
function vertical(row,column)
{
  var flag
  for(var i=0;i<3;i++)
  {
    flag=true
    if(matrix[i][column]===null)
      flag=false
    for(var j=i;j<i+4;j++)
    {
      if(matrix[i][column]!==matrix[j][column])
        {
          flag=false;
          break;
        }
    }
    if(flag===true)
      break
  }
  return flag
}

function square_check(row,column)
{
  var flag=false
  if(column-1>=0 && column+1<7 && row+2<6 && matrix[row+1][column-1]===matrix[row][column] && matrix[row+1][column+1]===matrix[row][column] && matrix[row+2][column]===matrix[row][column])
      flag=true;
  if(column-2>=0 && row+1<6 && row-1>=0 && matrix[row+1][column-1]===matrix[row][column] && matrix[row-1][column-1]===matrix[row][column] && matrix[row][column-2]===matrix[row][column])
      flag=true;
  if(column+2<7 && row+1<6 && row-1>=0 && matrix[row+1][column+1]===matrix[row][column] && matrix[row-1][column+1]===matrix[row][column] && matrix[row][column+2]===matrix[row][column])
      flag=true;
//  console.log(row,column,flag)
  return flag
}

function checkForResult(row,column,move_count)
{
  var winning_flag=horizontal(row,column) || vertical(row,column) || square_check(row,column);

  if(winning_flag)
  {
    var refreshmessage="Refresh your browser to play again!!"
    if(move_count%2==1)
      $(".container").html("<h1> "+playerone+" has won! "+refreshmessage + " </h1>")
    else
      $(".container").html("<h1> "+playertwo+" has won! "+refreshmessage + " </h1>")
    stop_game=true
  }
  else {
      if(move_count==42)
        {
          $(".container").html("<h1> Match Draw! "+refreshmessage + " </h1>")
          stop_game=true
        }
      else if(move_count%2==1)
        $("h3").text(playertwo+":it is your turn,please pick a column to drop your red chip.");
      else
       $("h3").text(playerone+":it is your turn,please pick a column to drop your blue chip.");
  }
}
for(var i=0;i<6;i++)
{
  for(var j=0;j<7;j++)
  {
    //console.log("cel"+i+j)
    $("#cel"+i+j).click(function()
    {
      //console.log(parseInt(this.id[4]))
      if(!stop_game)
      {
        if(currentposition[parseInt(this.id[4])]==-1)
        {
            var previous=$("h3").text();
            $("h3").text("Invalid Move!! "+previous)
        }
        else {
          move_count++;
          lastcolor=(lastcolor+1)%2
          $("#cel"+currentposition[parseInt(this.id[4])]+parseInt(this.id[4])).css('background-color',color[lastcolor])
          //console.log("cel"+currentposition[parseInt(this.id[4])]+parseInt(this.id[4]),parseInt(this.id[4]))
          matrix[currentposition[parseInt(this.id[4])]][parseInt(this.id[4])]=lastcolor
          checkForResult(currentposition[parseInt(this.id[4])],parseInt(this.id[4]),move_count)
          currentposition[parseInt(this.id[4])]-=1
        }
      }
    })
  }
}
