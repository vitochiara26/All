function spinalCase(str) {
    return str
        .replace(/([a-z])([A-Z])/g, '$1 $2')
        .replace(/[\s_]+/g, '-')
        .toLowerCase();
}

console.log(spinalCase("ProductLanding page")); // "product-landing-page"
console.log(spinalCase("This Is Spinal Tap"));  // "this-is-spinal-tap"
console.log(spinalCase("thisIsSpinalTap"));     // "this-is-spinal-tap"
console.log(spinalCase("The_Andy_Griffith_Show")); // "the-andy-griffith-show"
console.log(spinalCase("Teletubbies say Eh-oh")); // "teletubbies-say-eh-oh"