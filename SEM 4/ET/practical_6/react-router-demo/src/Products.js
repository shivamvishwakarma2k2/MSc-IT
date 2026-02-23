import { Link, Outlet } from "react-router-dom";

function Products() {
    return (
        <div style={{ textAlign: "center" }}>
            <h3>Products Page</h3>

            <Link to="car" style={{ margin: "10px" }}>Car</Link>
            <Link to="bike" style={{ margin: "10px" }}>Bike</Link>

            <Outlet />
        </div>
    );
}

export default Products;