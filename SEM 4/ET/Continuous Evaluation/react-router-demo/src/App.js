// import { Routes, Route, Link } from 'react-router-dom';
// import Home from './components/Home';
// import Products from './components/Products';
// import Car from './components/Car';
// import Bike from './components/Bike';
// import Contact from './components/Contact';
// import './App.css'

// function App() {
//   return (
//     <div className='App'>
//       <nav>
//         <Link to="/">Home</Link> |{" "}
//         <Link to="/products">Products</Link> |{" "}
//         <Link to="/contact">Contact</Link>
//       </nav>


//       <Routes>
//         <Route path="/" element={<Home />} />
//         <Route path="/products" element={<Products />}>
//           <Route path="car" element={<Car />} />
//           <Route path="bike" element={<Bike />} />
//         </Route>
//         <Route path="/contact" element={<Contact />} />
//       </Routes>
//     </div>
//   );
// }

// export default App;





// Anothr task

import {
  BrowserRouter,
  Routes,
  Route,
  NavLink,
  Link,
  useParams,
  Outlet
} from "react-router-dom";

// Active NavLink styles
const navLinkStyles = ({ isActive }) => ({
  color: isActive ? "#007bff" : "#333",
  textDecoration: isActive ? "none" : "underline",
  fontWeight: isActive ? "bold" : "normal",
  padding: "5px 10px"
});

// Pages
function Home() {
  return <h1>Home Page</h1>;
}

function About() {
  return <h1>About Page</h1>;
}

function Contact() {
  return <h1>Contact Page</h1>;
}

function Products() {
  return (
    <div>
      <h1>Products Page</h1>
      <nav style={{ marginBottom: '20px' }}>
        <Link to="/products/car">Cars</Link> |{" "}
        <Link to="/products/bike">Bikes</Link>
      </nav>
      <Outlet />
    </div>
  );
}

function CarProducts() {
  return (
    <div>
      <h2>Cars</h2>
      <ul>
        <li>Audi</li>
        <li>BMW</li>
        <li>Volvo</li>
      </ul>
    </div>
  );
}

function BikeProducts() {
  return (
    <div>
      <h2>Bikes</h2>
      <ul>
        <li>Yamaha</li>
        <li>Suzuki</li>
        <li>Honda</li>
      </ul>
    </div>
  );
}

// Nested customer info
function CustomerInfo() {
  const { firstname } = useParams();
  return <h2>Hello, {firstname}!</h2>;
}

// Customers page (combined)
function Customers() {
  return (
    <>
      <h1>Customers</h1>

      <nav style={{ marginBottom: "15px" }}>
        <Link to="Shivam">Shivam</Link> |{" "}
        <Link to="Manish">Manish</Link> |{" "}
      </nav>

      {/* Nested route content renders here */}
      <Outlet />
    </>
  );
}

function App() {
  return (
    <BrowserRouter>
      <nav style={{ marginBottom: "20px" }}>
        <NavLink to="/" style={navLinkStyles}>Home</NavLink> |{" "}
        <NavLink to="/about" style={navLinkStyles}>About</NavLink> |{" "}
        <NavLink to="/contact" style={navLinkStyles}>Contact</NavLink> |{" "}
        <NavLink to="/products" style={navLinkStyles}>Products</NavLink> |{" "}
        <NavLink to="/customers" style={navLinkStyles}>Customers</NavLink>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="/products" element={<Products />}>
          <Route path="car" element={<CarProducts />} />
          <Route path="bike" element={<BikeProducts />} />
        </Route>
        {/* Nested routing */}
        <Route path="/customers" element={<Customers />}>
          <Route path=":firstname" element={<CustomerInfo />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;