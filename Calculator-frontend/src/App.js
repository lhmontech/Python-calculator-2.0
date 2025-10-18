import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from "./components/Layout";
import { Home, Tribonacci, Fibonacci, Primes } from './pages/pages';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="fibonacci" element={<Fibonacci />} />
          <Route path="tribonacci" element={<Tribonacci />} />
          <Route path="primes" element={<Primes />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;