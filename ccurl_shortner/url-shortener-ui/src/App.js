import logo from './logo.svg';
import './App.css';
import { useState } from 'react';

function App() {
  const [value, setvalue] = useState(10)
  return (
    <div className="App">
		<div className='value'> {value} </div>
		<button onClick={()=> {
			setvalue(value + 1)
		}}>Click me</button>
    </div>
  );
}

export default App;
