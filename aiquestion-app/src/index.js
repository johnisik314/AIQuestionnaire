import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { fetchDataFromBackend, myFunction } from './fetch'; // Import fetchDataFromBackend and myFunction from fetch.js

const handleClick = () => {
  fetchDataFromBackend()
    .then(data => {
      console.log('Fetched data:', data);
    })
    .catch(error => {
      console.error('Error:', error);
    });

  myFunction(); // Now ESLint will recognize 'myFunction'
};

ReactDOM.render(
  <React.StrictMode>
    <div>
      <button onClick={handleClick}>Click Me</button>
    </div>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
