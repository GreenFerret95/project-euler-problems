import Utils

primeListLength = 10001
primes = [0]*primeListLength

prime_index = 0
count = 2   # skip checking 0 and 1 for prime
while(prime_index < len(primes)):
    if(Utils.is_prime(count)):
        primes[prime_index] = count
        prime_index += 1
    count += 1

print(primes[len(primes)-1])

