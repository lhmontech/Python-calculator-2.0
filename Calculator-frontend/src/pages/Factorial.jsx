import Keypad from "../components/Keypad";
import { useState, useEffect } from "react";
import '../App.css';

function Factorial() {
  const [currentValue, setCurrentValue] = useState("");
  const [values, setValues] = useState([]);
  const [result, setResult] = useState(null);

  useEffect(() => {
    if (currentValue.trim() !== "") {
      setValues([Number(currentValue)]);
      setResult(null);
    } else {
      setValues([]);
    }
  }, [currentValue]);

  return (
    <div className='Result_area'>
        <div className='Monitor'>
          <p>Welcome to the Factorial number!</p>   
          <p>Enter the value to obtain your factorial number.
            Remember that the value cannot be less than 1.
          </p>
          <p>Result:</p>
          {result?.error ? (
              <p style={{ color: '#ff513aff' }}>{result.error}</p>
            ) : (
              <p>{result?.result}</p>
          )}
        </div>
        <div className='Forms'>
          <label>Enter the value:</label><br />
          <input type="number" value={currentValue} onChange={(e) => setCurrentValue(e.target.value)}/>
        </div>
        <Keypad 
          setCurrentValue={setCurrentValue} 
          setValues={setValues}
          setResult={setResult} 
          values={values}
          operation="factorial"
        />
    </div>
  );
}
export default Factorial;