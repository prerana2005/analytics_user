def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def complex_function(x):
    if x > 0:
        for i in range(x):
            if i % 2 == 0:
                print(factorial(i))
            else:
                for j in range(i):
                    print(j)
                    
# re-triggering workflow
