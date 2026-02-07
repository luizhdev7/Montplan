import { useState, useEffect } from 'react'
import api from './utils/api' // seu axios configurado





function App() {
  const [count, setCount] = useState(0)
  const [usuarios, setUsuarios] = useState([])

  console.log("Montplan frontend rodando 🚀");
  
  
  useEffect(() => {
    // Buscar usuários do backend
    const fetchUsuarios = async () => {
      try {
        const res = await api.get('/usuarios') // endpoint correto
        setUsuarios(res.data) // salva no estado
      } catch (err) {
        console.error("Erro ao buscar usuários:", err)
      }
    }

    fetchUsuarios()
  }, [])

  return (
    <div>
      <h1>Montplan - Usuários</h1>
      
      <div className="card">
        <button onClick={() => setCount(c => c + 1)}>
          count is {count}
        </button>

        <p>Usuários do backend:</p>
        <ul>
          {usuarios.map(u => (
            <li key={u.id}>{u.nome}</li> // usa "nome" se o backend retorna esse campo
          ))}
        </ul>
      </div>
    </div>
  )
}




export default App
