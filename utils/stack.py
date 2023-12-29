import sys


class Stack:
	def __init__(self, max_size=100):
		self.__stack = []
		self.max_size = max_size
		
	def push(self, item):
		if self.is_overflow():
			return
		self.__stack.append(item)
	
	def pop(self):
		return self.__stack.pop() if not self.is_empty() else None

	def is_overflow(self) -> bool:
		return len(self.__stack) == self.max_size
	
	def is_empty(self) -> bool:
		return len(self.__stack) == 0
	
	def show_items(self):
		print(self.__stack)

	def peek(self) -> int:
		return self.__stack[-1] if not self.is_empty() else None
