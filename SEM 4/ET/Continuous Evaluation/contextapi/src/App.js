import './App.css';
import College from './College';
import { SubjectContext } from './Context';
import { useState } from "react";

function App() {
  const [subject, setSubject] = useState('ET');
  return (
    <div style={{ backgroundColor: 'yellow', padding: 10 }} >
      <SubjectContext.Provider value={subject}>
        <select onChange={(event) => setSubject(event.target.value)}>

          <option value="">Select Subject</option>

          <option value="ET">ET</option>
          <option value="AIOT">AIOT</option>
          <option value="CF">CF</option>
          <option value="RP">RP</option>

        </select>


        <h1>Context API Practical</h1>
        <button onClick={() => setSubject('')}>Clear Button</button>


        <College />
      </SubjectContext.Provider>

    </div>
  );
}

export default App;
