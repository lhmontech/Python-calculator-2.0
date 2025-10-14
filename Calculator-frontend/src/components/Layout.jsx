import Menu from "./Menu";
import { Outlet } from "react-router-dom";
import '../App.css';

function Layout() {
  return (
    <div className="App">
      <Menu />
      <main className="Result_area">
          <Outlet />
      </main>
    </div>
  );
}

export default Layout;