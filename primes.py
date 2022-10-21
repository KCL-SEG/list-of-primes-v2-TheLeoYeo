"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    if number_of_primes <= 0:
        raise ValueError(f"{number_of_primes} is too small")
    
    list.append(2)
    if number_of_primes == 1:
        return list

    current_num = 3
    while len(list) < number_of_primes:
        divisible = False
        length = len(list)
        for num in list[1:length//2]:
            if current_num % num == 0:
                divisible = True
                break
        if not divisible:
            list.append(current_num)
        current_num += 2
    return list

