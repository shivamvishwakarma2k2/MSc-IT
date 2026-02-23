import React from "react";
import { useSelector, useDispatch } from "react-redux";
import { setSearchTerm } from "../features/CricketerSlice";
const CricketerList = () => {
  const dispatch = useDispatch();
  const { list, searchTerm } = useSelector((state) => state.cricketers);

  const filteredList = list.filter((name) =>
    name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div>
      <h2>Cricketer Search</h2>

      <input
        type="text"
        placeholder="Search cricketer..."
        value={searchTerm}
        onChange={(e) => dispatch(setSearchTerm(e.target.value))}
      />

      <ul>
        {filteredList.map((name, index) => (
          <li key={index}>{name}</li>
        ))}
      </ul>
    </div>
  );
};

export default CricketerList;

