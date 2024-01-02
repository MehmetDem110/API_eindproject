import React, { useState, useEffect } from 'react';

function App() {
  const [users, setUsers] = useState([]);
  const [items, setItems] = useState([]);
  const [locations, setLocations] = useState([]);

  const fetchData = async (url, setter) => {
    try {
      const response = await fetch(url);
      if (response.ok) {
        const data = await response.json();
        setter(data);
      } else {
        console.error(`Failed to fetch ${url}`);
      }
    } catch (error) {
      console.error(`Error fetching ${url}:`, error);
    }
  };

  useEffect(() => {
    fetchData('http://127.0.0.1:8000/users', setUsers);
    fetchData('http://127.0.0.1:8000/items', setItems);
    fetchData('http://127.0.0.1:8000/locations', setLocations);
  }, []);

  return (
    <div className="App">
      {/* Users Section */}
      <div>
        <h1>Users</h1>
        <ul>
          {users.map(user => (
            <li key={user.id}>{user.email}</li>
          ))}
        </ul>
        <button onClick={() => fetchData('http://127.0.0.1:8000/users', setUsers)}>
          Refresh Users
        </button>
      </div>

      {/* Items Section */}
      <div>
        <h1>Items</h1>
        <ul>
          {items.map(item => (
            <li key={item.id}>{item.title}</li>
          ))}
        </ul>
        <button onClick={() => fetchData('http://127.0.0.1:8000/items', setItems)}>
          Refresh Items
        </button>
      </div>

      {/* Locations Section */}
      <div>
        <h1>Locations</h1>
        <ul>
          {locations.map(location => (
            <li key={location.id}>{location.address}</li>
          ))}
        </ul>
        <button onClick={() => fetchData('http://127.0.0.1:8000/locations', setLocations)}>
          Refresh Locations
        </button>
      </div>
    </div>
  );
}

export default App;