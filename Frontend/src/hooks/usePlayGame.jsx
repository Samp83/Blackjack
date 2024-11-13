
export default function usePlayGame(){
    const playGame = () => {
        fetch(`http://localhost:8000/api/play_game/{game_id}/`, {
            method: "POST",
            headers: {
                Accept: "application/json",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                action: "throw",  
                diceCount: int
            }),
        
        })
        .then((response) => {
            return response.json();
        })
        .then((response) =>{
            console.log(response)
        })
        .catch((reason) => {
            console.error(reason);
        });
    };
  
    return { playGame };
  }