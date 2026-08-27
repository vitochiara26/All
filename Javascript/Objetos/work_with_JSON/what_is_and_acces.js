// {
//   "name": "Alice",
//   "age": 30,
//   "isStudent": false,
//   "list of courses": ["Mathematics", "Physics", "Computer Science"]
// }

import data from "./example.json" with { type: "json" };

console.log(data.age);

import data from "./example.json" with { type: "json" };

console.log(data["list of courses"]);