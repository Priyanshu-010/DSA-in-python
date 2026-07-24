def gcd(a, b):
    """
    Calculate the greatest common divisor (GCD) of two numbers using recursion.
    what is a GCD? The GCD of two integers is the largest positive integer that divides both numbers without leaving a remainder.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The GCD of the two numbers.
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    """
    Calculate the least common multiple (LCM) of two numbers using the GCD.
    what is a LCM? The LCM of two integers is the smallest positive integer that is divisible by both numbers.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The LCM of the two numbers.
    """
    return a * b // gcd(a, b)


print(gcd(48, 18))  # Output: 6
print(lcm(4, 5))    # Output: 20