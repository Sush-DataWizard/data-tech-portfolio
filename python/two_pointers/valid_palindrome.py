
def valid_palindrome():
    s = "A man, a plan, a canal: Panama"
    cleaned = ''.join(char.lower() for char in s if char.isalnum())

    return cleaned == cleaned[::-1]

print(valid_palindrome())



# char.isalpha()   ---->   To check if string is ALPHABET
# char.isalnum()   ---->   To check if string is ALPHA-NUMERIC
# char.isdigit()   ---->   To check if string is DIGIT