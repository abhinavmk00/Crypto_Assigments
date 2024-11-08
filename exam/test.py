import random

def mod(a, m):
    return ((a % m) + m) % m

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_first_n_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def get_random_numbers(n, start=1, end=100):
    return [random.randint(start, end) for _ in range(n)]

def encrypt_shift(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine the case and base ASCII value
            ascii_base = ord('A') if char.isupper() else ord('a')
            # Apply shift and wrap around using modulo
            shifted = mod(ord(char) - ascii_base + shift, 26)
            result += chr(ascii_base + shifted)
        else:
            result += char
    return result

def decrypt_shift(text, shift):
    return encrypt_shift(text, -shift)

if __name__ == "__main__":
    print("\n=== Modular Arithmetic ===")
    print(f"mod(-5, 3) = {mod(-5, 3)}")
    print(f"mod(17, 5) = {mod(17, 5)}")

    print("\n=== Prime Numbers ===")
    print(f"\nFirst 10 prime numbers: {get_first_n_primes(10)}")
    
    print("\n=== IV. Shift Cipher ===")
 
    messages = ["Hello, World!", "Python Programming 101", "UPPERCASE lower123"]
    shift_value = 3
    
    for msg in messages:
        encrypted = encrypt_shift(msg, shift_value)
        decrypted = decrypt_shift(encrypted, shift_value)
        print(f"\nOriginal: {msg}")
        print(f"Encrypted (shift={shift_value}): {encrypted}")
        print(f"Decrypted: {decrypted}")
        print(f"Successful roundtrip: {msg == decrypted}")

