def vigenere_encrypt(plaintext, keyword):
    ciphertext = ""
    keyword = keyword.upper()
    keyword_length = len(keyword)
    keyword_as_int = [ord(i) - ord('A') for i in keyword]
    
    for i, char in enumerate(plaintext.upper()):
        if char.isalpha():
            # Convert letter to number (A=0, B=1, ..., Z=25)
            char_num = ord(char) - ord('A')
            # Get the corresponding keyword letter
            keyword_num = keyword_as_int[i % keyword_length]
            # Apply Vigenère encryption formula
            encrypted_num = (char_num + keyword_num) % 26
            # Convert back to letter
            encrypted_char = chr(encrypted_num + ord('A'))
            ciphertext += encrypted_char
        else:
            ciphertext += char
    
    return ciphertext

# Message and keyword
message = "She is listening"
keyword = "PASCAL"

# Encrypt the message
encrypted_message = vigenere_encrypt(message, keyword)

print(f"Original message: {message}")
print(f"Keyword: {keyword}")
print(f"Encrypted message: {encrypted_message}")