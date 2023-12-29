"""
https://leetcode.com/problems/valid-palindrome/description/

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters
and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


Constraints:
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""


def is_palindrome(p_str) -> bool:
	# p_str = p_str.replace(" ", "").lower()
	# length = len(p_str)//2
	# first_half = p_str[:length]
	# second_half = p_str[length:] if len(p_str) % 2 == 0 else p_str[length+1:]
	# second_half = second_half[::-1]
	# return second_half == first_half
	clean_str = ''.join(char.lower() for char in p_str if char.isalnum())
	return clean_str == clean_str[::-1]


if __name__ == "__main__":
	print(is_palindrome("amanaplanacanalpanama"))
	print(is_palindrome("raceacar"))
	print(is_palindrome(" "))

