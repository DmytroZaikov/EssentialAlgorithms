# Find the greatest common divisor of a and b.
# GCD(a, b) = GCD(b, a Mod b).

# One way to find the GCD is to factor the two numbers
# and see which factors they have in common.
# However, the Greek mathematician Euclid recorded a faster method
# in his treatise Elements circa 300 BC. Because it is based on Euclid's work
# this algorithm is called the Euclidian algorithm or Euclid's algorithm:


def gcd(a, b):
    while b != 0:
        reminder = a % b
        a = b
        b = reminder
    return a


print(gcd(100, 15))
