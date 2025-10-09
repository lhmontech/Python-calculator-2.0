import './App.css';

function App() {
  return (
    <div className='App'>
      <div className='Menu'>
        <header>
          <h1>MENU</h1>
          <p>
            Hello, welcome to lhmontech calculator!
            Select the option you want to calculate:
          </p>
        </header>
        <div className='Menu_buttons'>
          <div className='Left_buttons'>
            <p>
              Common Calculations
            </p>
            <p>
              Fibonacci sequence
            </p>
            <p>
              Factorial calculation
            </p>
            <p>
              Perfect squares sequence
            </p>
            <p>
              Prime numbers sequence
            </p>
            <p>
              Conversion of decimal ↔ binary
            </p>
          </div>
          <div className='Right_buttons'>
            <p>
              Geometric sequence
            </p>
            <p>
              Tribonacci sequence
            </p>
            <p>
              Alternating sequence
            </p>
            <p>
              Cubes sequence
            </p>
            <p>
              Triangular numbers sequence
            </p>
            <p>
              Conversion of decimal ↔ hexadecimal
            </p>
          </div>
        </div>
      </div>
      <div className='Result_area'>
        <div className='Monitor'>
          <h2>
            The instructions and results will appear here! 
          </h2>
          <h4>
            Below you can enter numbers directly into the available inputs or use the numeric keypad.
          </h4>
          <p>
            Result:
          </p>
        </div>
        <div className='Forms'>

        </div>
        <div className='Keypad'>
          <div>
            <p>1</p>
            <p>4</p>
            <p>7</p>
            <p>0</p>
          </div>
          <div>
            <p>2</p>
            <p>5</p>
            <p>8</p>
            <p className='Clean_but'>Clean</p>
          </div>
          <div>  
            <p>3</p>
            <p>6</p>
            <p>9</p>
            <p className='Calc_but'>Calculate</p>
          </div>  
        </div>
      </div>
    </div>
  );
}

export default App;
