def decodeString(s):
    stack = []
    curr_str = ""
    num = 0

    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == '[':
            stack.append((curr_str, num))
            curr_str, num = "", 0
        elif ch == ']':
            last_str, repeat = stack.pop()
            curr_str = last_str + curr_str * repeat
        else:
            curr_str += ch

    return curr_str


s = input("Enter the encoded string: ")
print("Decoded string:", decodeString(s))
