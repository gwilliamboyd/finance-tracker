import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [users, setUsers] = useState([])

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const response = await fetch('http://localhost:8000/users')
        const users = await response.json()
        console.log(users)
        setUsers(users)
        return users
      } catch (err) {
        console.error('Error fetching users: ', err)
      }
    }
    fetchUsers()
  }, [])

  return (
    <>
      <h1>Users</h1>
      {users.map(user => (
        <li key={user.id}>
          {user.username} - {user.email}
        </li>
      ))}
    </>
  )
}

export default App
