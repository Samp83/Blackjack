
export default function useCreateGame(){
    const createGame = () => {
        fetch(`http://localhost:8000/api/game/start_game/`, {
            method: "POST",
            headers: {
                Accept: "application/json",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                name: "name",
                players: ["str"]
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

    return { createGame };
}