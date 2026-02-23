import { Routes, Route, Link } from "react-router-dom";
import Home from "./Home";
import Products from "./Products";
import Contact from "./Contact";
import Car from "./Car";
import Bike from "./Bike";

function App() {
  return (
    <div>
      <h2 style={{ textAlign: "center", background: "lightblue", padding: "10px" }}>
        React Router Demo
      </h2>

      <div style={{ textAlign: "center", marginBottom: "15px" }}>
        <Link to="/" style={{ margin: "10px" }}>Home</Link>
        <Link to="/products" style={{ margin: "10px" }}>Products</Link>
        <Link to="/contact" style={{ margin: "10px" }}>Contact</Link>
      </div>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/contact" element={<Contact />} />

        <Route path="/products" element={<Products />}>
          <Route path="car" element={<Car />} />
          <Route path="bike" element={<Bike />} />
        </Route>
      </Routes>
    </div>
  );
}

export default App;