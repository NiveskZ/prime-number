print("Hello World")

# %%
benchmark_comparisons = 0

# Start from 2, because that the first prime number.
prime_numbers = [2]

for i in range(3, 1000, 2):

    # skip all numbers already divisible by any prime number already identified.
    is_prime_number = True

    for prime_number in prime_numbers:
        benchmark_comparisons = benchmark_comparisons + 1
        if i % prime_number == 0:
            is_prime_number = False

    if is_prime_number:
        prime_numbers.append(i)


print(prime_numbers)
print(benchmark_comparisons)
# %%
