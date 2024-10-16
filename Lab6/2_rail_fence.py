def rail_fence_encrypt(message, key):
    # Create the rail fence matrix
    fence = [[' ' for _ in range(len(message))] for _ in range(3)]
    
    # Fill the rail fence
    row, direction = 0, 1
    for i, char in enumerate(message):
        fence[row][i] = char
        row += direction
        if row == 0 or row == 2:
            direction *= -1
    
    # Read off the fence
    cipher = ''
    for i, letter in enumerate(key):
        for j in range(len(message)):
            if fence[i][j] != ' ':
                cipher += fence[i][j]
    
    return cipher

# Example usage
message = input("Enter the message to encrypt: ")
key = "ONE"

encrypted_message = rail_fence_encrypt(message, key)
print(f"Encrypted message: {encrypted_message}")