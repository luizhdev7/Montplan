import { useState } from "react";
import axios from "axios";

export default function UserForm() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post("http://127.0.0.1:8000/users", {
        name,
        email
      });
      alert("Usuário criado!");
      setName("");
      setEmail("");
    } catch (err) {
      console.error(err);
      alert("Erro ao criar usuário");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Nome"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <button type="submit">Adicionar Usuário</button>
    </form>
  );
}
