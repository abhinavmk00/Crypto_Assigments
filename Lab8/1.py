def gcd_euclidean(a, b):
    """Calculate the Greatest Common Divisor of a and b using the Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a

def are_coprime(a, b):
    """Check if two numbers are co-prime."""
    return gcd_euclidean(a, b) == 1

def check_cryptographic_suitability(a, b):
    """Check if two numbers are suitable for cryptographic key generation."""
    gcd = gcd_euclidean(a, b)
    coprime = gcd == 1
    
    print(f"The GCD of {a} and {b} is: {gcd}")
    
    if coprime:
        print(f"{a} and {b} are co-prime.")
        print("These numbers are suitable for use in cryptographic key generation.")
    else:
        print(f"{a} and {b} are not co-prime.")
        print("These numbers are not suitable for use in cryptographic key generation.")

# Get input from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Check suitability for cryptographic key generation
check_cryptographic_suitability(num1, num2)