import { Link, Outlet } from 'react-router-dom';

function Products() {
  return (
    <div>
      <h2>Products Page</h2>
      <nav>
        <Link to="car">Car</Link> |{" "}
        <Link to="bike">Bike</Link>
      </nav>

      <Outlet />
    </div>
  );
}

export default Products;