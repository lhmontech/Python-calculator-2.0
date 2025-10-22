import Keypad from "../components/Keypad";
import { useState } from "react";
import '../App.css';

function Tribonacci() {
  const [currentValue, setCurrentValue] = useState("");
  const [values, setValues] = useState([]);
  const maxValues = 4;
  const isAddDisabled = values.length >= maxValues;
  const [result, setResult] = useState(null);
  const [labelText, setLabelText] = useState("Enter the first value:");
  const labelSteps = [
    "Enter the first value:",
    "Enter the second value:",
    "Enter the third value",
    "Enter the limit value:"
  ];

  function handleAdd() {
    if (currentValue.trim() === "") return;
    setValues(prev => [...prev, Number(currentValue)]);
    setCurrentValue("");
    setResult(null);

    const nextIndex = values.length + 1;
    if (nextIndex < labelSteps.length) {
      setLabelText(labelSteps[nextIndex]);
    }
  }

  return (
    <div className='Result_area'>
        <div className='Monitor'>
          <p>Welcome to the Tribonacci sequence!</p> 
          <p>
            Enter three initial values and a limit value to obtain the sequence. 
            Remember that the initial values cannot be 0 and the limit value must 
            be greater than the initial ones.
          </p>   
          <ul>
            {values.map((v, i) => {
              const names = ["1° Value:", "2° Value:", "Limit:"];
              const label = names[i] || `value${i+1}`;
              return <li key={i}>{label} = {v}</li>;
            })}
          </ul>
          <p>Result:</p>
          {result?.error ? (
              <p style={{ color: '#ff513aff' }}>{result.error}</p>
            ) : (
              <p>{result?.sequence?.join(", ")}</p>
          )}
        </div>
        <div className='Forms'>
          <label>{labelText}</label><br />
          <input type="number" value={currentValue} onChange={(e) => setCurrentValue(e.target.value)}/>
          <button onClick={handleAdd} disabled={isAddDisabled}>Add</button>
        </div>
        <Keypad 
          setCurrentValue={setCurrentValue} 
          setValues={setValues}
          setResult={setResult} 
          values={values}
          operation="tribonacci"
        />
    </div>
  );
}
export default Tribonacci;