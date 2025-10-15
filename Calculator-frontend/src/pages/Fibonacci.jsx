import Keypad from "../components/Keypad";
import { useState } from "react";
import '../App.css';

function Fibonacci() {
  const [currentValue, setCurrentValue] = useState("");
  const [values, setValues] = useState([]);
  const maxValues = 3;
  const isAddDisabled = values.length >= maxValues;
  const [result, setResult] = useState(null);
  
  function handleAdd() {
    if (currentValue.trim() === "") return;
    setValues(prev => [...prev, Number(currentValue)]);
    setCurrentValue("");
  }
  return (
    <div className='Result_area'>
        <div className='Monitor'>
          <p>Welcome to the Fibonacci sequence!</p>   
          <p>Enter two initial values and a limit value to obtain the sequence. 
            Remember that the initial values cannot be 0 and the limit value must 
            be greater than the initial ones.</p>
          <ul>
            {values.map((v, i) => <li key={i}>Value{i+1} = {v}</li>)}
          </ul>
          <p>Result:</p>
          {result?.sequence.error ? (
              <p style={{ color: '#ff513aff' }}>{result.sequence.error}</p>
            ) : (
              <p>{result?.sequence?.sequence?.join(", ")}</p>
          )}
        </div>
        <div className='Forms'>
                Enter here the values:<br />
                <input type="number" value={currentValue} onChange={(e) => setCurrentValue(e.target.value)}/>
                <button onClick={handleAdd} disabled={isAddDisabled}>Add</button>
                
        </div>
        <Keypad 
          setCurrentValue={setCurrentValue} 
          setValues={setValues}
          setResult={setResult} 
          values={values}
          operation="fibonacci"
        />
    </div>
  );
}
export default Fibonacci;