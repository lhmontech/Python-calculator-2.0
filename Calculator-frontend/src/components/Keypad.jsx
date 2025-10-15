import '../App.css';
import { useState } from "react";

function Keypad({setCurrentValue, setValues, values, operation}) {
  
  function onKeyPress(num) {
    setCurrentValue(prev => prev + num);
  }
  
  function handleDelete() {
    setValues([]);
    setCurrentValue("");
  }

  function handleCalculate() {
    const endpoint = `http://localhost:5000/${operation}`;

    fetch(endpoint, {
      method: "POST",
      headers: { "Content-Type": "application/json"},
      body: JSON.stringify({ values: values}),
    })
      .then((res) => res.json())
      .then((data) => {
        console.log("Result:", data);
        setResult(data);
      })
      .catch((err) => console.log("Error:", err));
  }

  return (
        <div className='Keypad'>
      <div>
        <button onClick={() => onKeyPress('1')}>1</button>
        <button onClick={() => onKeyPress('4')}>4</button>
        <button onClick={() => onKeyPress('7')}>7</button>
        <button onClick={() => onKeyPress('0')}>0</button>
      </div>
      <div>
        <button onClick={() => onKeyPress('2')}>2</button>
        <button onClick={() => onKeyPress('5')}>5</button>
        <button onClick={() => onKeyPress('8')}>8</button>
        <button className='Clean_but' onClick={handleDelete}>Clean</button>
      </div>
      <div>
        <button onClick={() => onKeyPress('3')}>3</button>
        <button onClick={() => onKeyPress('6')}>6</button>
        <button onClick={() => onKeyPress('9')}>9</button>
        <button className='Calc_but' onClick={handleCalculate}>Calculate</button>
      </div>
    </div>
    );
}

export default Keypad;