import { add, subtract, PI } from './export.js';

console.log(add(5, 3));        // Outputs: 8
console.log(subtract(10, 4));  // Outputs: 6
console.log(PI);               // Outputs: 3.14159

import * as Math from './export.js';

console.log(Math.add(5, 3));        // Outputs: 8
console.log(Math.subtract(10, 4));  // Outputs: 6
console.log(Math.PI);               // Outputs: 3.14159 

import multiply from './export.js';
console.log(multiply(4, 5));  // Outputs: 20
