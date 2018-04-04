var cell00=document.querySelector("#tt00");
var cell01=document.querySelector("#tt01");
var cell02=document.querySelector("#tt02");
var cell10=document.querySelector("#tt10");
var cell11=document.querySelector("#tt11");
var cell12=document.querySelector("#tt12");
var cell20=document.querySelector("#tt20");
var cell21=document.querySelector("#tt21");
var cell22=document.querySelector("#tt22");
var move=['O','X']
var last
var count
var tictac
var delayInMilliseconds = 4;
reset()
function check_winner()
{
  count+=1
  flag=false
  row1=tictac[0][0]+tictac[0][1]+tictac[0][2]
  row2=tictac[1][0]+tictac[1][1]+tictac[1][2]
  row3=tictac[2][0]+tictac[2][1]+tictac[2][2]
  col1=tictac[0][0]+tictac[1][0]+tictac[2][0]
  col2= tictac[0][1]+tictac[1][1]+tictac[2][1]
  col3=tictac[0][2]+tictac[1][2]+tictac[2][2]
  d1=tictac[0][0]+tictac[1][1]+tictac[2][2]
  d2=tictac[0][2]+tictac[1][1]+tictac[2][0]
   console.log(tictac)
   console.log(d2)
  flag=(row1==3 || row1==0||row2==3 || row2==0||row3==3 || row3==0)
  flag=flag||(col1==3 || col1==0 || col2==3 || col2==0 || col3==3 || col3==0)
  flag=flag||(d1==3||d1==0 ||d2==3||d2==0)
  if(flag)
  {
    if(count%2==1)
      alert("Congrats player 1!!!")
    else {
      alert("Congrats player 2!!!")
    }
    reset();
  }
  else if(count==9)
  {
    alert("match draw");
    reset()
  }
}
function reset()
{
  cell00.textContent='';
  cell01.textContent='';
  cell02.textContent='';
  cell10.textContent='';
  cell11.textContent='';
  cell12.textContent='';
  cell20.textContent='';
  cell21.textContent='';
  cell22.textContent='';
  count=0;
  last=1;
  tictac=[[4,4,4],[4,4,4],[4,4,4]];
}
cell00.addEventListener('click',function(){
  if(cell00.textContent.length==0)
      {
          last=(last+1)%2
        cell00.textContent=move[last];
        tictac[0][0]=last
        setTimeout(check_winner,delayInMilliseconds)
      }
})
cell01.addEventListener('click',function(){
  if(cell01.textContent.length==0)
    {
      last=(last+1)%2
      cell01.textContent=move[last];
      tictac[0][1]=last
      setTimeout(check_winner,delayInMilliseconds)
    }
})
cell02.addEventListener('click',function(){
  if(cell02.textContent.length==0)
    {
       last=(last+1)%2
        cell02.textContent=move[last];
        tictac[0][2]=last
        setTimeout(check_winner,delayInMilliseconds)
    }
})

cell10.addEventListener('click',function(){
  if(cell10.textContent.length==0)
    {
      last=(last+1)%2
      cell10.textContent=move[last];
      tictac[1][0]=last
        setTimeout(check_winner,delayInMilliseconds)
    }
})
cell11.addEventListener('click',function(){
  if(cell11.textContent.length==0)
    {
        last=(last+1)%2
       cell11.textContent=move[last];
      tictac[1][1]=last
      setTimeout(check_winner,delayInMilliseconds)
    }
})
cell12.addEventListener('click',function(){

  if(cell12.textContent.length==0)
    {
        last=(last+1)%2
        cell12.textContent=move[last];
      tictac[1][2]=last
      setTimeout(check_winner,delayInMilliseconds)
    }
})
cell20.addEventListener('click',function(){
  if(cell20.textContent.length==0)
    {
        last=(last+1)%2
        cell20.textContent=move[last];
      tictac[2][0]=last
      setTimeout(check_winner,delayInMilliseconds)
    }
})

cell21.addEventListener('click',function(){
  if(cell21.textContent.length==0)
    {
      last=(last+1)%2
      cell21.textContent=move[last];
      tictac[2][1]=last
      setTimeout(check_winner,delayInMilliseconds)
    }
})
cell22.addEventListener('click',function(){
  if(cell22.textContent.length==0)
    {
      last=(last+1)%2
        cell22.textContent=move[last];
        tictac[2][2]=last
      setTimeout(check_winner,delayInMilliseconds)
    }
})
document.querySelector("button").addEventListener('click',reset)
