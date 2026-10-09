const now = new Date();
const date = now.getDate();
const month = now.getMonth();
const year = now.getFullYear();
console.log(now);
console.log(date); 
console.log(month);
console.log(year); 

const dateFromArguments = new Date(1776, 6, 4, 12, 0, 0, 0);
console.log(dateFromArguments);
