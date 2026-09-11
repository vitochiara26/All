function getAverage(notes) {
    let sum = 0;
    for (let i = 0; i < notes.length; i++) {
        sum += notes[i];
    }
    return sum / notes.length
}

function getGrade(studNote) {
    if (studNote === 100) {
        return "A+";
    } else if (studNote >= 90 && studNote <= 99) {
        return "A";
    } else if (studNote >= 80 && studNote <= 89) {
        return "B";
    } else if (studNote >= 70 && studNote <= 79) {
        return "C";
    } else if (studNote >= 60 && studNote <= 69) {
        return "D";
    } else {
        return "F";
    }
}

function hasPassingGrade(studNote) {
    if (getGrade(studNote) === "F") {
        return false;
    }
    return true;
}

function studentMsg(notes, studNote) {
    if (hasPassingGrade(studNote)) {
        return `Class average: ${getAverage(notes)}.
        Your grade: ${getGrade(studNote)}. You passed the course.`
    } else {
        return `Class average: ${getAverage(notes)}.
        Your grade: ${getGrade(studNote)}. You failed the course.`
    }
}

console.log(getAverage([92, 88, 12, 77, 57, 100, 67, 38, 97, 89]));
console.log(getAverage([45, 87, 98, 100, 86, 94, 67, 88, 94, 95]));
console.log(getAverage([38, 99, 87, 100, 100, 100, 100, 100, 100, 100]));
console.log(getAverage([10, 20, 30, 40, 55, 65, 75, 83]));
console.log(getAverage([10, 20, 30, 40, 50, 60, 70, 97]));

console.log(studentMsg([92, 88, 12, 77, 57, 100, 67, 38, 97, 89], 37));
console.log(studentMsg([56, 23, 89, 42, 75, 11, 68, 34, 91, 19], 100));
console.log(studentMsg([12, 22, 32, 42, 52, 62, 72, 92], 85));
console.log(studentMsg([15, 25, 35, 45, 55, 60, 70, 60], 75));