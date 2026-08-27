const config1 = {
    fault: false,
    phases: [
        { color: "green", duration: 5 },
        { color: "yellow", duration: 2 },
        { color: "red", duration: 4 }
    ]
};

const config2 = {
    fault: false,
    phases: [
        { color: "red", duration: 3 },
        { color: "yellow", duration: -2 },
        { color: "green", duration: 6 }
    ]
};

const config3 = {
    fault: true,
    phases: [
        { color: "green", duration: 5 },
        { color: "yellow", duration: 2 },
        { color: "red", duration: 6 }
    ]
};

const config4 = {
    fault: false,
    phases: []
};

function runSequence(config, cycles) {
    if (config.phases.length === 0) {
        console.log("No phases found");
        return;
    }
    if (config.fault) {
        console.log("Faulted phase!")
        return;
    }
    for (let cycle = 0; cycle < cycles; cycle++) {
        for (const phase of config.phases) {
            if (phase.duration <= 0) {
                console.log("Invalid phase detected");
            } else {
                console.log(`Switching to ${phase.color} for ${phase.duration} s`);
            }
        }
    }
}

function generateTimeline(config, cycles) {
    const timeline = [];
    let seconds = 0
    for (let cycle = 0; cycle < cycles; cycle++) {
        for (const phase of config.phases) {
            seconds += phase.duration;
            timeline.push(seconds);
        }
    }
    return timeline;
}

runSequence(config1, 1);
console.log();
runSequence(config1, 2);
console.log();
runSequence(config2, 1);
console.log();
runSequence(config3, 2);
console.log();
runSequence(config4, 5);
console.log();

console.log(generateTimeline(config1, 1));
console.log(generateTimeline(config1, 2));
console.log(generateTimeline(config2, 2));
console.log(generateTimeline(config3, 1));
console.log(generateTimeline(config4, 1));
