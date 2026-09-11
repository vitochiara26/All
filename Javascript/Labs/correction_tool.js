function isPalindrome(word) {
    const lowerWord = word.toLowerCase();
    const reversedWord = lowerWord.split("").reverse().join("");
    return lowerWord === reversedWord;
}

function findPalindromeBreaks(words) {
    const breaks = [];
    for (let i = 0; i < words.length; i++) {
        if (!isPalindrome(words[i])) {
            breaks.push(i);
        }
    }
    return breaks;
}

function findRepeatedPhrases(words, phraseLength) {
    if (phraseLength >= words.length) {
        return [];
    }

    const phraseDict = {};

    for (let i = 0; i <= words.length - phraseLength; i++) {
        const phrase = words.slice(i, i + phraseLength).join(" ");

        if (!phraseDict[phrase]) {
            phraseDict[phrase] = [];
        }
        phraseDict[phrase].push(i);
    }

    const repeatedIndices = [];
    for (const phrase in phraseDict) {
        if (phraseDict[phrase].length > 1) {
            for (let i = 0; i < phraseDict[phrase].length; i++) {
                repeatedIndices.push(phraseDict[phrase][i]);
            }
        }
    }

    return repeatedIndices.sort((a, b) => a - b);
}

function analyzeTexts(texts, phraseLength) {
    const results = [];
    if (texts.length === 0) {
        return results;
    }

    for (let i = 0; i < texts.length; i++) {
        const text = texts[i];

        results.push({
            repeatedPhrases: findRepeatedPhrases(text, phraseLength),
            palindromeBreaks: findPalindromeBreaks(text)
        });
    }

    return results;
}

const phraseLength = 2;
const texts = [
    ["level", "the", "cat", "sat", "the", "cat", "radar"], // Tiene palíndromos y repeticiones
    ["hello", "world"]                                     // Texto 2: Sin palíndromos
];

const finalResult = analyzeTexts(texts, phraseLength);
