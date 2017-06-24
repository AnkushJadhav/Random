import timing

n = 40

def fib( n ):
	if n <= 2:
		f = 1
	else:
		f = fib(n-1) + fib(n-2)
	return f

print("Fibonacci("+str(n)+") = "+str(fib(n)))
