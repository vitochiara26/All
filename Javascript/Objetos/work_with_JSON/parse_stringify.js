const user = {
    name: "John",
    age: 30,
    isAdmin: true
};

const jsonString = JSON.stringify(user);
console.log(jsonString);

const developerObj = {
    firstName: "Jessica",
    isAwesome: true,
    isMusician: true,
    country: "USA",
};

// result: {"firstName":"Jessica","country":"USA"}
console.log(JSON.stringify(developerObj, ["firstName", "country"]));

const developerObj2 = {
    firstName: "Jessica",
    isAwesome: true,
    isMusician: true,
    country: "USA",
};

console.log(JSON.stringify(developerObj2, null, 2));

/* result
{
    "firstName": "Jessica",
    "isAwesome": true,
    "isMusician": true,
    "country": "USA"
}
*/

const jsonString2 = '{"name":"John","age":30,"isAdmin":true}';
const userObject = JSON.parse(jsonString2);
console.log(userObject);

// Result:
// { name: 'John', age: 30, isAdmin: true }