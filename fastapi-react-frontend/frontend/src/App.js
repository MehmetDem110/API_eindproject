import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [users, setUsers] = useState([]);
  const [items, setItems] = useState([]);
  const [locations, setLocations] = useState([]);

  const fetchUsers = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/users');
      if (response.ok) {
        const userData = await response.json();
        setUsers(userData);
      } else {
        console.error('Failed to fetch users');
      }
    } catch (error) {
      console.error('Error fetching users:', error);
    }
  };

  // Implement fetchItems and fetchLocations in a similar way...

  useEffect(() => {
    fetchUsers();
    // Call fetchItems() and fetchLocations() here if needed
  }, []); // Empty dependency array ensures this runs only once on component mount

  return (
    <div className="App">
      <div className="container">
        <div>
          <h1>Users</h1>
          <ul>
            {users.map((user) => (
              <li key={user.id}>{user.email}</li>
            ))}
          </ul>
          <button onClick={fetchUsers}>Refresh Users</button>
        </div>

        {/* Implement Items and Locations sections similarly */}
      </div>
    </div>
  );
}

export default App;
