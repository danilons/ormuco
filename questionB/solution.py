"""
The goal of this question is to write a software library that accepts 2 version string as input and
returns whether one is greater than, equal, or less than the other. As an example: “1.2” is
greater than “1.1”. Please provide all test cases you could think ok
"""
def is_greater(str1, str2):
	"""
	check if str1 is greater than str2

	@param str str1 - first string
	@param str str2 - second string
	@return bool is_greater
	"""
	try:
		number1 = float(str1)
		number2 = float(str2)
		return number1 > number2
	except ValueError:
		pass
	return str1 > str2