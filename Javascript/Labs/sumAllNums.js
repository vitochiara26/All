function sumAll(nums) {
    let sum = 0
    const lowest = nums[0] < nums[1] ? nums[0] : nums[1]
    const highest = nums[0] > nums[1] ? nums[0] : nums[1]
    for (let i = lowest; i <= highest; i++) {
        sum += i
    }
    return sum
}

console.log(sumAll([4, 1]));
console.log(sumAll([1, 4]));
console.log(sumAll([5, 10]));
console.log(sumAll([10, 5]));
