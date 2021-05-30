import time


start_number = 1
end_number = int(input("Find prime numbers up to: "))

start = time.time()
primes = []
no_primes = 0

print("Looking for prime numbers up to " + str(end_number))

for candidate_number in range(start_number, end_number, 1):
    found_prime = True
    for div_number in range(2, candidate_number):
        if candidate_number % div_number == 0:
            found_prime = False
            break
    if found_prime:
        primes.append(candidate_number)
        no_primes += 1

end = round(time.time() - start, 2)

print("Elapsed time: " + str(end) + " seconds")
print("Prime numbers found: " + str(len(primes)))
print(primes)
