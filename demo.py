from math_helper.number_theory import is_prime, gcd
from math_helper.combinatorics import nCr
from math_helper.sequences import generate_fibonacci
from math_helper.utils import is_palindrome

print(is_prime(29))            # True
print(gcd(24, 36))             # 12
print(nCr(5, 2))               # 10
print(generate_fibonacci(7))   # [0, 1, 1, 2, 3, 5, 8]
print(is_palindrome(121))      # True
