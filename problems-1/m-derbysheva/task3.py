import math
import bitarray


def checkprime (n):
    if n % 2 == 0:
        return (n == 2)
    d = 3
    while d * d <= n and n % d != 0:
           d += 2
    return d * d > n


def list_eratosthen(n):
    list = [True for _ in range(n)]

    for i in range(2, int(math.sqrt(n)) + 1):
        if list[i]:
            for j in range(i * 2, n, i):
                list[j] = False
    answer = []
    for i in range(2, n):
        if list[i]:
            answer.append(i)
    return answer


def bitarray_eratosthen(n):
    bitarr = bitarray.bitarray(n)
    bitarr.setall(True)

    for i in range(2, int(math.sqrt(n)) + 1):
        if bitarr[i]:
            for j in range(i * 2, n, i):
                bitarr[j] = False

    answer = []
    for i in range(2, n):
        if bitarr[i]:
            answer.append(i)
    return answer

def set_eratosthen (n):
    set_sieve = set(range(2, n))

    for i in range(2, int(math.sqrt(n)) + 1):
        for j in range(i * 2, n, i):
            if j in set_sieve: set_sieve.remove(j)

    return set_sieve


n = int(input("Enter number: "))

print(list_eratosthen(n))
print(bitarray_eratosthen(n))
print(set_eratosthen(n))


