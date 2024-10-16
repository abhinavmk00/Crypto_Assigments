def columnar_transposition(message, keyword):
    # Remove spaces and convert to uppercase
    message = ''.join(message.split()).upper()
    keyword = ''.join(keyword.split()).upper()
    
    # Create the column order based on the keyword
    column_order = sorted(range(len(keyword)), key=lambda k: keyword[k])
    
    # Calculate number of rows needed
    num_rows = -(-len(message) // len(keyword))  # Ceiling division
    
    # Pad the message if necessary
    message += 'X' * (num_rows * len(keyword) - len(message))
    
    # Create the grid
    grid = [[''] * len(keyword) for _ in range(num_rows)]
    
    # Fill the grid with the message
    index = 0
    for row in range(num_rows):
        for col in range(len(keyword)):
            grid[row][col] = message[index]
            index += 1
    
    # Read off the columns according to the keyword order
    ciphertext = ''
    for col in column_order:
        ciphertext += ''.join(grid[row][col] for row in range(num_rows))
    
    return ciphertext

def double_columnar_transposition_encrypt(message, keyword1, keyword2):
    # First transposition
    first_encryption = columnar_transposition(message, keyword1)
    
    # Second transposition
    second_encryption = columnar_transposition(first_encryption, keyword2)
    
    return second_encryption

# Example usage
message = input("Enter the message to encrypt: ")
keyword1 = input("Enter the first keyword for encryption: ")
keyword2 = input("Enter the second keyword for encryption: ")

encrypted_message = double_columnar_transposition_encrypt(message, keyword1, keyword2)
print(f"Encrypted message: {encrypted_message}")