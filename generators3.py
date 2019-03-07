def odd_numbers():
    n = 1
    while True:
        yield n
        n += 2


def pi_series():
    odds_pi = odd_numbers()
    approximation = 0
    while True:
        approximation += (4 / next(odds_pi))
        yield approximation
        approximation -= (4 / next(odds_pi))
        yield approximation


odds = odd_numbers()

print("*" * 80)
for i in range(50):
    print(next(odds))
print("*" * 80)

approx_pi = pi_series()
for x in range(1000000):
    print(next(approx_pi))

