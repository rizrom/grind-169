"""
https://leetcode.com/problems/valid-parentheses/description/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false


Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

from utils.stack import Stack


def check_valid_parenthesis(p_string) -> bool:
	stack = Stack()
	opening_bracket = ['{', '[', '(']
	closing_bracket =  ['}', ']', ')']
	for c in p_string:
		if c in opening_bracket:
			stack.push(c)
		else:
			stack.pop()
	return stack.is_empty()


if __name__ == "__main__":
	print(check_valid_parenthesis("()"))
	print(check_valid_parenthesis("()[]{}"))
	print(check_valid_parenthesis("()[{}]"))
	print(check_valid_parenthesis("("))
	
