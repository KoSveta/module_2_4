numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        primes.append(i)
    else:
        not_primes.append(i)


print(primes)
print(not_primes)