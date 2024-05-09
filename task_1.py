def caching_fibonacci():
    cache ={}

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci

fib = caching_fibonacci()

print(fib(28))  
print(fib(30))   
print(fib(5))  
print(fib(7)) 
        
       

