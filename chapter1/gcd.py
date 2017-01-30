# Find the greatest common divisor of a and b.
# GCD(a, b) = GCD(b, a Mod b).

def gcd(a, b):
    while b != 0:
        reminder = a % b
        a = b
        b = reminder
    return a


print(gcd(100, 15))
