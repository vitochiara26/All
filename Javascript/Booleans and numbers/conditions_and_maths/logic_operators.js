let result = true && 'hello';
console.log(result); // hello

result = 'hello' && true;
console.log(result); // true

result = 0 && 3;
console.log(result); // 0

result = 3 && 0;
console.log(result); // 0

result = false && 0;
console.log(result); // false

result = 0 && false;
console.log(result); // 0

if (2 < 3 && 3 < 4) {
    console.log('The if block runs');
} else {
    console.log('The else block runs');
}

result = 'This is truthy' || false;
console.log(result); // This is truthy

result = false || 'This is truthy';
console.log(result); // This is truthy

result = null ?? 'default';
console.log(result); // default

const userSettings = {
    theme: null,
    volume: 0,
    notifications: false,
};

let theme = userSettings.theme ?? 'light';
console.log(theme); // light