from .solution import  overlap

def test_overlap():
	assert overlap((1, 5), (2, 6))
	assert overlap((2, 6), (1, 5))

def test_not_overlap():
	assert not overlap((1, 5), (6, 8))
	assert not overlap((6, 8), (1, 5))

def test_double_overlap():	
	assert overlap((1., 5.), (2., 6.))
	assert overlap((2., 6.), (1., 5.))

def test_double_not_overlap():
	assert not overlap((1., 5.), (6., 8.))
	assert not overlap((6., 8.), (1., 5.)) 

def test_starting_at_the_end():
	assert not overlap((1, 5), (5, 10))