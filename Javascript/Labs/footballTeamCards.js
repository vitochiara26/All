const footballTeam = {
    team: "Argentina",
    year: 1986,
    headCoach: "Carlos Bilardo",
    players: [
        { name: "Diego Maradona", position: "midfielder", isCaptain: true },
        { name: "Sergio Batista", position: "midfielder", isCaptain: false },
        { name: "Jorge Valdano", position: "forward", isCaptain: false },
        { name: "Oscar Ruggeri", position: "defender", isCaptain: false },
        { name: "Nery Pumpido", position: "goalkeeper", isCaptain: false }
    ],
};

const teamSpanElem = document.getElementById('team');
const yearSpanElem = document.getElementById('year');
const headCoachSpanElem = document.getElementById('head-coach');
const playersDropdown = document.getElementById('players');
const playersCards = document.getElementById('player-cards');

teamSpanElem.textContent = footballTeam.team;
yearSpanElem.textContent = footballTeam.year;
headCoachSpanElem.textContent = footballTeam.headCoach;

const setPlayersCards = (arr = footballTeam.players) => {
    playersCards.innerHTML = arr
        .map(({ name, position, isCaptain }) => `
  <div class="player-card">
    <h2>${isCaptain ? "(Captain) " : ""}${name}</h2>
    <p>Position: ${position}</p>
  </div>
  `)
        .join("");
};

setPlayersCards();

playersDropdown.addEventListener('change', (e) => {
    const selectedPosition = e.target.value;

    if (selectedPosition === 'all') {
        setPlayersCards(footballTeam.players);
    } else {
        const filteredPlayers = footballTeam.players.filter(
            (player) => player.position === selectedPosition
        );
        setPlayersCards(filteredPlayers);
    }
});