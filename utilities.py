def is_palindrome(n):
    return str(n) == str(n)[::-1]

def reverse_number(n):
    return int(str(n)[::-1])

def is_armstrong(n):
    return n == sum(int(digit) ** len(str(n)) for digit in str(n))
