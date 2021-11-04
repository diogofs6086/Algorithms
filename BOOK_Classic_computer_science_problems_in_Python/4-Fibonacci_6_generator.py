def fib6(n):
	yield 0
	if n > 0:
		yield 1
	last = 0
	next = 1
	for _ in range(1, n):
		last, next = next, last + next
		yield next

if __name__ == "__main__":
	for i in fib6(9):
		print(i)
