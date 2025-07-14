def longest_common_prefix(strings):
    if not strings:
        return ""

    prefix = strings[0]
    print("init_prefix",prefix)
    for string in strings[1:]:
        print(string)
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            print("while_prefix",prefix)
            if not prefix:
                return ""
    
    return prefix

strings = ["flower", "flow", "flight"]
result = longest_common_prefix(strings)
print(f"The longest common prefix is: '{result}'")