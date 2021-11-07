/**
 * @param {number[]} nums
 * @return {number}
 */
 var removeDuplicates = function(nums) {
    let i = 1;
    if (nums.length >= 2) {
        let j = 2;
        while (i < nums.length) {
            console.log("i =", i, ". j =", j);
            console.log("nums =", nums);
            if(nums[i - 1] >= nums[i]) {
                while (j < nums.length && nums[i] >= nums[j]) {j++;}
                if (j === nums.length) {
                    break;
                }
                temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
                if (i > j) {j = i;}
            } else {
                i++;
                if (i > j) {j = i;}
            }
        }
    } else {
        i = nums.length;
    }
    console.log("nums =", nums);
    return i;
};
