"""
Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the
x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5)
and (6,8).
"""

def overlap(line1, line2):
	"""
	lines are a tuple representing two values
	@param line1 tuple - (x1, x2)
	@param line2 tuple - (x3, x4)
	@return bool overlaps?
	"""
	x1, x2 = line1
	x3, x4 = line2
	onLeft = min(x1, x2) <= min(x3, x4)
	if onLeft:
		return max(max((x1, x2)) - min((x3, x4)), 0) > 0
	return max(max((x3, x4)) - min((x1, x2)),0) > 0