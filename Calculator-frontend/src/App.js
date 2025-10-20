import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from "./components/Layout";
import { Home, Alternating, Tribonacci, Fibonacci, Primes, Binary, Common, Cubes, Factorial, Geometric, Hexadecimal, Squares } from './pages/pages';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="alternating" element={<Alternating />} />
          <Route path="fibonacci" element={<Fibonacci />} />
          <Route path="tribonacci" element={<Tribonacci />} />
          <Route path="primes" element={<Primes />} />
          <Route path="binary" element={<Binary />} />
          <Route path="common" element={<Common />} />
          <Route path="cubes" element={<Cubes />} />
          <Route path="factorial" element={<Factorial />} />
          <Route path="geometric" element={<Geometric />} />
          <Route path="hexadecimal" element={<Hexadecimal />} />
          <Route path="squares" element={<Squares />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
