
def count_cond(condition):
    return lambda x: sum(condition(x, i) for i in range(1,x+1))



count_factors = count_cond(lambda n, i: n % i == 0)
print(count_factors(12))
is_prime = lambda n, i: count_factors(i) == 2
count_primes = count_cond(is_prime)
print(count_primes(20))