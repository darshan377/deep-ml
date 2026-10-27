import numpy as np

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	
	a = np.array(a)
	b = np.array(b)

	shape_of_a = a.shape

	if shape_of_a[1] != b.size:
		return -1

	dot_product = np.dot(a,b).tolist()

	return dot_product

