def columnar_transposition_encrypt(message, key):
    # Remove spaces and convert to uppercase
    message = ''.join(message.split()).upper()
    key = ''.join(key.split()).upper()
    
    # Calculate number of rows needed
    num_rows = -(-len(message) // len(key))  # Ceiling division
    
    # Pad the message if necessary
    message += 'X' * (num_rows * len(key) - len(message))
    
    # Create the grid
    grid = [[''] * len(key) for _ in range(num_rows)]
    
    # Fill the grid with the message
    index = 0
    for row in range(num_rows):
        for col in range(len(key)):
            grid[row][col] = message[index]
            index += 1
    
    # Sort the columns based on the key
    sorted_columns = sorted(range(len(key)), key=lambda k: key[k])
    
    # Read off the columns to get the ciphertext
    ciphertext = ''
    for col in sorted_columns:
        ciphertext += ''.join(grid[row][col] for row in range(num_rows))
    
    return ciphertext

# Example usage
message = input("Enter the message to encrypt: ")
key = input("Enter the encryption key: ")

encrypted_message = columnar_transposition_encrypt(message, key)
print(f"Encrypted message: {encrypted_message}")