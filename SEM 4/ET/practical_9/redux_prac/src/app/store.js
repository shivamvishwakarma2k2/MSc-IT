import { configureStore } from "@reduxjs/toolkit";
import cricketersReducer from "../features/CricketerSlice";

export const store = configureStore({
  reducer: {
    cricketers: cricketersReducer,
  },
});

export default store;