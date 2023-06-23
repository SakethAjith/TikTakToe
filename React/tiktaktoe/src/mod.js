import { useEffect,useState } from 'react'

// function GetReq(){
//   return (fetch('https://jsonplaceholder.typicode.com/todos/1').
//   then(response=>response.json()).
//   then(data => console.log(data)))
// }


function Square({ value, onSquareClick }) {
  return (
    <button className="Square" onClick={onSquareClick}>{value}</button>
  );
}

export default function Board() {
  const [square, setSquare] = useState(Array(9).fill('_'))
  const [xIsNext, setXIsNext] = useState(true)
  const [users,setUsers] = useState([])


  const result = () => {
    fetch('http://localhost:30').then(response => {return response.json()})
    .then(data => setUsers(data))//setting users with API response
  }

    useEffect(() => {
      result()
    }, [])// calling result only once


  function handleClick(i) {
    const nextSquares = square.slice();

    if (nextSquares[i] == '_') {
      if (xIsNext) {
        nextSquares[i] = 'X'
        setXIsNext(false)
      } else {
        nextSquares[i] = 'O'
        setXIsNext(true)
      }
    }

    setSquare(nextSquares)
  }

  return (
    <>
      {/* <h1>?</h1> */}
      <div className='BoardRow'>
        <Square value={square[0]} onSquareClick={() => handleClick(0)} />
        <Square value={square[1]} onSquareClick={() => handleClick(1)} />
        <Square value={square[2]} onSquareClick={() => handleClick(2)} />
      </div>
      <div className='BoardRow'>
        <Square value={square[3]} onSquareClick={() => handleClick(3)} />
        <Square value={square[4]} onSquareClick={() => handleClick(4)} />
        <Square value={square[5]} onSquareClick={() => handleClick(5)} />
      </div>
      <div className='BoardRow'>
        <Square value={square[6]} onSquareClick={() => handleClick(6)} />
        <Square value={square[7]} onSquareClick={() => handleClick(7)} />
        <Square value={square[8]} onSquareClick={() => handleClick(8)} />
        {users.board}
      </div>
    </>
  );
}