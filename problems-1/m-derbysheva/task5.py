def checkprime (n):
    if n % 2 == 0:
        return (n == 2)
    d = 3
    while d * d <= n and n % d != 0:
           d += 2
    return d * d > n

n = int(input("print a number: "))
list = [1]
answer = [i for i in range(2, n) if checkprime(i)]
list.extend(answer)

print(list)
