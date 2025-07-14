
def length_of_last_word(s):
    words = s.strip().split()
    print(words)
    return len(words[-1]) if words else 0

s = "   fly me   to   the moon  "
s = "luffy is still joyboy"
result = length_of_last_word(s)
print(f"The length of the last word is: {result}")