//Square Initialization with empty values
var squares = Array(9).fill('');
//Predefined winner position
var winnerCondition = [
  [0,1,3],
  [3,4,5],
  [6,7,8],
  [0,3,6],
  [1,4,7],
  [2,5,8],
  [2,4,6],
  [0,4,8]
];
//Squares Html variable
var squareHtml  = '<div className="board-row">';
var xIsNext = true;
var winner  = false;
// Render squares
for(let i=0; i<squares.length;i++){
  if(i % 3 === 0 && i > 0){
    squareHtml += '</div><div className="board-row">';
    squareHtml += buildSquare(i);
  }else{
    squareHtml += buildSquare(i);
  }
}
squareHtml += '</div>';
document.getElementById('board').innerHTML = squareHtml;
/*
 * Render square 
 * @param int
 */
function buildSquare(j){
  return '<button class="square" onClick="handleClick('+j+')" id="sq_'+j+'">'+squares[j]+'</button>';
}

/*
 * Square box click handler
 * @param int
 */
function handleClick(index){
  //if the winner is there or square already marked : return
  if(winner || squares[index]){
    return ;
  }
  squares[index] = xIsNext ? 'X' : 'O';
  const sqs = squares.slice();
  var elementId = "sq_"+index;
  document.getElementById(elementId).innerHTML = xIsNext ? 'X' : 'O';
  xIsNext = xIsNext ? false : true;
  document.getElementById('status').innerHTML  = xIsNext ? 'X' : 'O';
  calculateWinner(sqs);
}
/*
 * Calculate the winner by passing marked square
 * @param array
 */
function calculateWinner(sqs){
  for(let i=0;i<winnerCondition.length;i++){
    const [p1,p2,p3] = winnerCondition[i];
    if(sqs[p1] && sqs[p1] === sqs[p2] && sqs[p1] === sqs[p3]){
      winner = sqs[p1];
      document.getElementById('status').innerHTML   = winner+ " is winner.";
      return winner;
    }
  }
  //Get marked square 
  var filtered = sqs.filter(function(e){
    return e != '';
  });
  //Check for the game draw
  if(filtered.length === 9 && !winner){
    document.getElementById('status').style.color = "red";
    document.getElementById('status').innerHTML   = "Match Draw"; 
  }
  return false;
}
