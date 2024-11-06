import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

// eslint-disable-next-line react/prop-types
function PlayerForm({ setPlayers, setDiceCount }) {
  const [playerNames, setPlayerNames] = useState(["", "", "", ""]);
  const [dice, setDice] = useState(1);
  const navigate = useNavigate();

  const startGame = () => {
    setPlayers(playerNames.map((name, index) => ({ id: index, name, score: 0, rolls: 0 })));
    setDiceCount(dice);
    navigate('/game');
  };

  return (
    <div>
    <table>
        <thead>
        <tr>  
            <h1>Black Jack</h1>
            <label>Number of Dice:</label>
            <input type="number" min="1" max="3" value={dice} onChange={(e) => setDice(parseInt(e.target.value))} />
        </tr>
        </thead> 

        <tbody>
        {playerNames.map((name, index) => (
        <input
          key={index}
          type="text"
          placeholder={`Nom ${index + 1} du joueur`}
          value={name}
          onChange={(e) => {
            const newNames = [...playerNames];
            newNames[index] = e.target.value;
            setPlayerNames(newNames);
          }}
        />
        ))}
        </tbody>


      <button onClick={startGame}>Start Game</button>
    </table>
    </div>
  );
}

export default PlayerForm;
