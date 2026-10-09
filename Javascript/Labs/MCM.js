function smallestCommons(nums) {
    const min = nums[0] < nums[1] ? nums[0] : nums[1]
    const max = nums[0] > nums[1] ? nums[0] : nums[1]

    function gcd(a, b) {
        return b === 0 ? a : gcd(b, a % b);
    }

    function lcm(a, b) {
        return (a * b) / gcd(a, b);
    }

    let multiple = min;
    for (let i = min + 1; i <= max; i++) {
        multiple = lcm(multiple, i);
    }

    return multiple;
}

console.log(smallestCommons([1, 5]));
console.log(smallestCommons([5, 1]));
console.log(smallestCommons([2, 10]));
console.log(smallestCommons([1, 13]));
console.log(smallestCommons([23, 18]));
