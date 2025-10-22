import Keypad from "../components/Keypad";
import { useState } from "react";
import '../App.css';

function Alternating() {
  const [currentValue, setCurrentValue] = useState("");
  const [values, setValues] = useState([]);
  const maxValues = 2;
  const isAddDisabled = values.length >= maxValues;
  const [result, setResult] = useState(null);
  const [labelText, setLabelText] = useState("Enter the first value:");
  const labelSteps = [
    "Enter the first value:",
    "Enter the number of terms:"
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
          <p>Welcome to the Alternating sequence!</p>
          <p>
            Enter the initial value and the number of terms to obtain the sequence.<br/> 
            The sequence alternates between positive and negative and doubles each term.<br/>
            Remember that the final value must be greater than the initial one, and the initial cannot be negative.
          </p>  
          <ul>
            {values.map((v, i) => {
              const names = ["1° Value:","N° Terms:"];
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
          operation="alternating"
        />
    </div>
  );
}
export default Alternating;