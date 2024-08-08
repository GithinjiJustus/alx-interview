#!/usr/bin/python3
def minOperations(n):
    """
    Calculates the minimum number of operations needed to get n 'H' characters
    using only 'Copy All' and 'Paste' operations.
    """
    if n <= 1:
        return 0
    operations = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    return operations

if __name__ == "__main__":
    # Main file for testing
    n = 4
    print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

    n = 12
    print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))
