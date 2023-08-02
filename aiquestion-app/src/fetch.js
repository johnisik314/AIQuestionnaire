import axios from 'axios';

// Define the myFunction
export function myFunction() {
  alert('Hello from myFunction()!');
}

// Define the fetchDataFromBackend function
export async function fetchDataFromBackend() {
  try {
    const response = await axios.get('https://your-python-backend-api.com/data');
    return response.data;
  } catch (error) {
    console.error('Error:', error);
    return [];
  }
}

// You can define other functions or components in this file if needed
