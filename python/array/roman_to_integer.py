
def roman_to_integer(roman):
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer_value = 0
    prev_value = 0

    for i in reversed(roman):
        print(i)
        if roman_map[i] < prev_value:
            integer_value -= roman_map[i]
        else:
            integer_value += roman_map[i]

        prev_value = roman_map[i]
    return integer_value

roman_numeral = "XIV"
integer_value = roman_to_integer(roman_numeral)
print(f"The integer value of {roman_numeral} is {integer_value}.")


# s="XIV"
# d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
# summ = 0
# n = len(s)
# i = 0
# while i < n:
#     if i < n - 1 and d[s[i]] < d[s[i+1]]:
#         summ += d[s[i+1]] - d[s[i]]
#         i += 2
#     else:
#         summ += d[s[i]]
#         i +=1    

# print(summ)    