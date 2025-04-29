import React, { useState, useEffect } from 'react'
import './App.css'

// memoize users
const UsersList = React.memo(({ users }) => (
  <ul>
    {users.map(user => (
      <li key={user.id}>
        {user.username} - {user.email}
      </li>
    ))}
  </ul>
))

// component
function App() {
  const serverConnUrl = import.meta.env.VITE_SERVER_CONN_URL
  // users state
  const [users, setUsers] = useState([])
  const [hasError, setHasError] = useState(false)
  console.log(serverConnUrl)

  // fetch users on mount
  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const response = await fetch(`${serverConnUrl}/users/`)
        const users = await response.json()
        setUsers(users)
        return users
      } catch (err) {
        console.error('Error fetching users: ', err)
        setHasError(true)
      }
    }
    fetchUsers()
  }, [serverConnUrl])

  return (
    <>
      <h1>Users</h1>
      {!hasError ? <UsersList users={users} /> : <h2>Error loading users.</h2>}
    </>
  )
}

export default App
