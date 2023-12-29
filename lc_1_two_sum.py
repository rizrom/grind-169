"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""
from typing import List

from utils.random_num_generator import get_list, get


def two_sum(nums: List[int], target: int) -> List[int]:
    lut = {}
    result: List[int] = []
    for index, item in enumerate(nums):
        if target-item in lut:
            result = [lut[target-item], index]
            break
        else:
            lut.update({item: index})
    return result


if __name__ == "__main__":
    nums = get_list(get(2, 104), -109, 109)
    target = 6
    result = two_sum(nums, target)

    print("nums: ", nums)
    print("target: ", target)
    
    if len(result) > 1:
        print(nums[result[0]], nums[result[1]])
    else:
        print("Not Found")
