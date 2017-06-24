import timing

n = 40
memo = {}

def fib( n ):
	if memo.has_key(n):
		f = memo[n]
	if n <= 2:
		f= 1
	else:
		f = fib(n-1) + fib(n-2)
		memo[n] = f
	return f

print("Memoised Fibonacci("+str(n)+") = "+str(fib(n)))
