import React from 'react';
import logo from './logo.svg';
import './App.css';
import MarkdownEditor from './MarkdownEditor';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <p>Or not learn react :((</p>
        {/* <button onClick={MarkdownEditor.render}> link to another page</button> */}
      </header>
    </div>
  );
}

export default App;
