import { NavLink } from "react-router-dom";
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
            <NavLink to="/" className={({ isActive }) => isActive ? "btn active" : "button"}>
              Common Calculations
            </NavLink>
            <NavLink to="/fibonacci" className={({ isActive }) => isActive ? "btn active" : "button"}>
              Fibonacci sequence
            </NavLink>
            <NavLink to="/" className={({ isActive }) => isActive ? "btn active" : "button"}>
              Factorial calculation
            </NavLink>
            <NavLink to="/" className={({ isActive }) => isActive ? "btn active" : "button"}>
              Perfect squares sequence
            </NavLink>
            <NavLink to="/" className={({ isActive }) => isActive ? "btn active" : "button"}>
              Prime numbers sequence
            </NavLink>
            <NavLink to="/" className={({ isActive }) => isActive ? "btn active" : "button"}>
              Conversion of decimal ↔ binary
            </NavLink>
          </div>
          <div>
            <NavLink to="/" className={({ isActive }) => isActive ? "btn active" : "button"}>
              Geometric sequence
            </NavLink>
            <NavLink to="/tribonacci" className={({ isActive }) => isActive ? "btn active" : "button"}>
              Tribonacci sequence
            </NavLink>
            <NavLink to="/" className={({ isActive }) => isActive ? "btn active" : "button"}>
              Alternating sequence
            </NavLink>
            <NavLink to="/" className={({ isActive }) => isActive ? "btn active" : "button"}>
              Cubes sequence
            </NavLink>
            <NavLink to="/" className={({ isActive }) => isActive ? "btn active" : "button"}>
              Triangular numbers sequence
            </NavLink>
            <NavLink to="/" className={({ isActive }) => isActive ? "btn active" : "button"}>
              Conversion of decimal ↔ hexadecimal
            </NavLink>
          </div>
        </div>
      </div>
  );
}

export default Menu;
