def str_str(haystack, needle):
    if not needle:
        return 0
    
    return haystack.find(needle)

# Example Usage
haystack = "butsad"
needle = "sad"
result = str_str(haystack, needle)
print(f"The index of the first occurrence of '{needle}' in '{haystack}' is: {result}")