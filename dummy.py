def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    seq = [0, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

def process_numbers(x):
    results = []
    if x < 10:
        for i in range(1, x + 1):
            if i % 3 == 0:
                results.append(i ** 2)
            else:
                results.append(i + 5)
    else:
        i = 0
        while i < x:
            if i % 4 == 0:
                results.append(i)
            i += 2
    return results

if __name__ == "__main__":
    print(fibonacci(7))
    print(process_numbers(12))
# retrigger workflow
# re trigger
