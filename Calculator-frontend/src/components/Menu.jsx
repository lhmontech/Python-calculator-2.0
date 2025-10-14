import { Link } from "react-router-dom";
import '../App.css';

function Menu() {
  return (
    <div className='Menu'>
        <header>
          <h1>MENU</h1>
          <p>
            Hello, welcome to lhmontech calculator!
            Select the option you want to calculate:
          </p>
        </header>
        <div className='Menu_buttons'>
          <div>
            <Link to="/">Common Calculations</Link>
            <Link to="/fibonacci">Fibonacci sequence</Link>
            <Link to="/">Factorial calculation</Link>
            <Link to="/">Perfect squares sequence</Link>
            <Link to="/">Prime numbers sequence</Link>
            <Link to="/">Conversion of decimal ↔ binary</Link>
          </div>
          <div>
            <Link to="/">Geometric sequence</Link>
            <Link to="/tribonacci">Tribonacci sequence</Link>
            <Link to="/">Alternating sequence</Link>
            <Link to="/">Cubes sequence</Link>
            <Link to="/">Triangular numbers sequence</Link>
            <Link to="/">Conversion of decimal ↔ hexadecimal</Link>
          </div>
        </div>
      </div>
  );
}

export default Menu;
