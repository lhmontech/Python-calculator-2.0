import '../App.css';

function Tribonacci() {
  return (
    <div className='Result_area'>
        <div className='Monitor'>
          <p>Welcome to the Tribonacci sequence!</p>   
          <p>Below you can enter numbers directly into the available inputs or use the numeric keypad.</p>  
          <p>Result:</p>
        </div>
        <div className='Forms'>
            <div>
                <label>Enter the first value:<br />
                <input type="number" /></label>
                <label>Enter the second value:<br />
                <input type="number" /></label>
            </div>
            <div>
                <label>Enter the thirst value:<br />
                <input type="number" /></label>
                <label>Enter the limit:<br />
                <input type="number" /></label>
            </div>
        </div>
    </div>
  );
}
export default Tribonacci;