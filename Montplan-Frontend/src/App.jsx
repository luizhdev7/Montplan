import { useState, useEffect } from 'react'
import api from './utils/api' // deixa como você tinha

function App() {
  const [count, setCount] = useState(0)
  const [usuarios, setUsuarios] = useState([])

  useEffect(() => {
    api.get('/usuarios')
      .then(res => setUsuarios(res.data)) // salvar no estado
      .catch(err => console.error(err))
  }, [])

  return (
    <>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((c) => c + 1)}>
          count is {count}
        </button>
        <p>Usuários do backend:</p>
        <ul>
          {usuarios.map(u => (
            <li key={u.id}>{u.nome}</li>
          ))}
        </ul>
      </div>
    </>
  )
}

export default App
