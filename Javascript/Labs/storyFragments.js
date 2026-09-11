const shuffledFragments = [
    { id: 15, text: "and, after a time, passed the place where the Hare was sleeping." },
    { id: 12, text: "he lay down beside the course to take a nap" },
    ,
    { id: 11, text: "and to make the Tortoise feel very deeply how ridiculous it was for him to try a race with a Hare," },
    { id: 7, text: "but for the fun of the thing he agreed." },
    { id: 19, text: "The Hare now ran his swiftest," },
    ,
    { id: 1, text: "A Hare was making fun of the Tortoise one day for being so slow." },
    { id: 14, text: "The Tortoise meanwhile kept going slowly but steadily," },
    { id: 9, text: "marked the distance and started the runners off." },
    ,
    { id: 5, text: "I'll run you a race and prove it.\"" },
    { id: 17, text: "and when at last he did wake up," },
    { id: 2, text: '"Do you ever get anywhere?" he asked with a mocking laugh.' },
    { id: 12, text: "he lay down beside the course to take a nap" },
    ,
    { id: 8, text: "So the Fox, who had consented to act as judge," },
    { id: 20, text: "but he could not overtake the Tortoise in time." },
    { id: 5, text: "I'll run you a race and prove it.\"" },
    { id: 6, text: "The Hare was much amused at the idea of running a race with the Tortoise," },
    ,
    { id: 13, text: "until the Tortoise should catch up." },
    { id: 10, text: "The Hare was soon far out of sight," },
    { id: 12, text: "he lay down beside the course to take a nap" },
    { id: 18, text: "the Tortoise was near the goal." },
];

function compactFragments(fragments) {
    const notUndefined = [];
    for (let i = 0; i < fragments.length; i++) {
        if (fragments[i]) {
            notUndefined.push(fragments[i]);
        } else {
            console.log("[COMPACTED]")
        }
    }
    return notUndefined;
}

const compactedShuffledFragments = compactFragments(shuffledFragments);

function sortFragments(compactedFragments) {
    const sortedFragments = compactedFragments.slice();
    let auxBox;
    for (let i = 0; i < sortedFragments.length; i++) {
        for (let j = i + 1; j < sortedFragments.length; j++) {
            if (sortedFragments[i].id > sortedFragments[j].id) {
                auxBox = sortedFragments[j];
                sortedFragments[j] = sortedFragments[i];
                sortedFragments[i] = auxBox;
            }
        }
    }
    return sortedFragments;
}

const sortedFragments = sortFragments(compactedShuffledFragments);

function dedupeFragments(fragments) {
    const dedupedFragments = []
    const ids = []
    for (let i = 0; i < fragments.length; i++) {
        if (!ids.includes(fragments[i].id)) {
            dedupedFragments.push(fragments[i]);
            ids.push(fragments[i].id);
        } else {
            console.log("[DEDUPED]")
        }
    }
    return dedupedFragments;
}

const dedupedFragments = dedupeFragments(sortedFragments);

function fillMissingFragments(fragments) {
    const filledArr = fragments.slice();
    const fragmentsIds = [];
    for (let i = 0; i < fragments.length; i++) {
        fragmentsIds.push(fragments[i].id);
    }

    const lowId = fragments[0].id;
    const highId = fragments[fragments.length - 1].id;
    const totalIds = [];
    for (let i = lowId; i <= highId; i++) {
        totalIds.push(i);
    }

    for (let i = 0; i < totalIds.length; i++) {
        if (!fragmentsIds.includes(totalIds[i])) {
            filledArr.push({ id: i + 1, text: "[...]" })
            console.log("[FILLED]")
        }
    }

    return sortFragments(filledArr);
}

const filledFragments = fillMissingFragments(dedupedFragments);

function assembleStory(filledFragments) {
    let story = "";
    for (let i = 0; i < filledFragments.length - 1; i++) {
        story += `${filledFragments[i].text}\n`;
    }
    story += filledFragments[filledFragments.length - 1].text;
    return story;
}

console.log(assembleStory(filledFragments));
