let greetings = (name) => {
    console.log("Hello, " + name + "!");
};

greetings = name => {
    console.log("Hello, " + name + "!");
};

greetings = () => {
    console.log("Hello");
};

greetings = name => console.log("Hello, " + name + "!");

let calculateArea = (width, height) => {
    const area = width * height;
    return area;
};
console.log(calculateArea(5, 3)); // 15

calculateArea = (width, height) => {
  return width * height;
}; 
console.log(calculateArea(5, 3)); // 15

calculateArea = (width, height) => width * height;