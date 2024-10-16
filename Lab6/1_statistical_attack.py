# not working
cipher = "XLILSYWIMWRSAJSVWEPIJSVJSYVQMPPMSRHSPPEVWMXMWASVX-LQSVILYVVCFIJSVIXLIWIPPIVVIGIMZIWQSVISJJIVW" 


frequency = {}
for char in cipher:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

frequency = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))

english_frequency = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

replacement_mapping = {}
for i, char in enumerate(frequency):
    replacement_mapping[char] = english_frequency[i]

plain_text = "".join(replacement_mapping.get(char, char) for char in cipher)

print(frequency)
print(replacement_mapping)
print(cipher)
print(plain_text)