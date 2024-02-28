def prime_factors(n):
    factors = []
    # Handle edge cases
    if n < 2:
        return factors
    # Divide by 2 until n is odd
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # Check odd factors from 3 to square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    # If n is prime and greater than 2
    if n > 2:
        factors.append(n)
    return factors

def main():
    while True:
        try:
            # Ask the user to input a positive integer
            num = int(input("Enter a positive integer (or '0' to exit): "))
            if num == 0:
                print("Exiting the program.")
                break
            elif num < 0:
                print("Please enter a positive integer.")
                continue
            # Compute and print the prime factorization of the input integer
            factors = prime_factors(num)
            print(f"Prime factorization of {num}: {factors}")
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")

if __name__ == "__main__":
    main()
