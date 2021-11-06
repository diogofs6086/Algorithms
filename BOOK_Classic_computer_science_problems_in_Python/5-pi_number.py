def calculate_pi(n_terms):
	numerator = 4
	denominator = 1
	operation = 1
	pi = 0
	for _ in range(n_terms):
		pi += operation * (numerator / denominator)
		denominator += 2
		operation *= -1
	return pi

if __name__ == "__main__":
	print(calculate_pi(100000000))
