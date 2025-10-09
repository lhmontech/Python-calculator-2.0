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
              Conversion of decimal - binary
            </p>
          </div>
          <div className='Right_buttons'>
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
              Conversion of decimal - binary
            </p>
          </div>
        </div>
      </div>
      <div className='Result_area'>
        <div className='Monitor'>

        </div>
        <div className='Forms'>

        </div>
        <div className='Keypad'>

        </div>
      </div>
    </div>
  );
}

export default App;
