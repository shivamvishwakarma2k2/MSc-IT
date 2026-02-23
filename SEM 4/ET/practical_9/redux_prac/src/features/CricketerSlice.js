import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  list: [
    "Virat Kohli",
    "MS Dhoni",
    "Jasprit Bumrah",
    "Rohit Sharma",
    "Hardik Pandya",
    "Shikhar Dhawan",
    "Yuzvendra Chahal",
    "Ravindra Jadeja",
    "KL Rahul",
    "Bhuvneshwar Kumar",
  ],
  searchTerm: "",
};

const cricketersSlice = createSlice({
  name: "cricketers",
  initialState,
  reducers: {
    setSearchTerm: (state, action) => {
      state.searchTerm = action.payload;
    },
  },
});

export const { setSearchTerm } = cricketersSlice.actions;
export default cricketersSlice.reducer;

