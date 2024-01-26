import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
// import './App.css'
import Navbar from './navbar.jsx';
import Home from './home.jsx'

function App() {
  const [count, setCount] = useState(0)
  // const name = "Don't Panic"
  // const num = 42
  const link = "https://www.goodreads.com/"
  //{name } returns some dynamic value
  // we cannot output booleans and objectss
  return (
    <div className='App'>
      {/* <Navbar></Navbar> */}
      <Navbar/>
      <div className="content">
        {/* <h1>{name}</h1>
        <p>Liked {num} times</p>
        <p>{"Hello World!"}</p>
        <p>{Math.floor(Math.random() * 10)}</p>
        <a href={link}>GoodReads</a> */}
        <Home></Home>

      </div>
    </div>
  )
}

export default App;


