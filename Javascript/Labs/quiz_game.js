const questions = [
    { category: "Cine",
    question: ("¿De qué color es la píldora que tomaNeo para descubrir la verdad en The Matrix?"),
    choices: ["Roja", "Azul", "Verde"],
    answer: "Roja" },

    { category: "Ciencia",
    question: "¿Cuál es el elemento químico más abundante en el universo observable?", 
    choices: ["Helio", "Hidrógeno", "Oxígeno"], 
    answer: "Hidrógeno" },

    { category: "Videojuegos", 
    question: "¿Cuál es la mascota oficial de la franquicia Pokémon?", 
    choices: ["Charmander", "Pikachu", "Eevee"], 
    answer: "Pikachu" },

    { category: "Geografia", 
    question: "¿En qué continente se encuentra el desierto de Atacama?", 
    choices: ["África", "América", "Asia"], 
    answer: "América" },

    { category: "Tecnologia", 
    question: "¿Qué animal representa a la mascota oficial del sistema operativo Linux?", 
    choices: ["Pingüino", "Perro", "Dragón"], 
    answer: "Pingüino" },
];

function getRandomQuestion(questions) {
    const question = Math.floor(Math.random() * questions.length);
    return questions[question];
}

function getRandomComputerChoice(choices) {
    const choice = Math.floor(Math.random() * choices.length);
    return choices[choice];
}

function getResults(question, choice) {
    if (question.answer === choice) {
        return "The computer's choice is correct!"
    } else {
        return `The computer's choice is wrong. The correct answer is: ${question.answer}`
    }
}

const pregunta = getRandomQuestion(questions);
console.log(`La pregunta es: ${pregunta.question}`)
console.log(`La opciones son: ${pregunta.choices}`)

const eleccionCPU = getRandomComputerChoice(pregunta.choices);
console.log(`El CPU escogió: ${eleccionCPU}`)

console.log(getResults(pregunta, eleccionCPU));
