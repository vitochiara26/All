//AND devuelve 1 solo cuando ambos bits sean 1
let a = 5;  // Binary: 101
let b = 3;  // Binary: 011
console.log(a & b);  // 1 (Binary: 001)

//OR devuelve 1 si al menos uno de los dos bits son 1
console.log(a | b);  // 7 (Binary: 111)

//XOR devuelve 1 si solo un de los dos bits son 1 pero no ambos
console.log(a ^ b);  // 6 (Binary: 110)

//NOT ivierte cada bit, de 0 a 1 y de 1 a 0
console.log(~a);  // -6

//Dezplazamiento a la izquierda, mueve los bits un numero especificado de posiciones
console.log(a << 1);  // 10 (Binary: 1010)

//Dezplazamiento a la derecha, mueve los bits un numero especificado de posiciones
console.log(a >> 1);  // 2 (Binary: 10)