import { useState } from 'react'
import { Routes, Route } from 'react-router-dom'
import './App.css'
import PlayerForm from './components/PlayerForm';

    function App() {
      const [setPlayers] = useState([]);
      const [setDiceCount] = useState(1);
    
      return (
          <Routes>
            <Route path="/" element={<PlayerForm setPlayers={setPlayers} setDiceCount={setDiceCount} />} />
          </Routes>

          
      );
    }
export default App
