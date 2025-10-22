import Keypad from "../components/Keypad";
import { useState, useEffect } from "react";
import '../App.css';

function Common() {
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
          <p>Welcome to the Common Calculations!</p>   
          <p>Enter the calculation.
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
          operation="common"
        />
    </div>
  );
}
export default Common;