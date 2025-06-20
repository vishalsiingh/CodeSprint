def decode_parentheses(s: str) -> str:
    result = []
    balance = 0
    start = 0  

    for i, char in enumerate(s):
        if char == '(':
            balance += 1
        else:
            balance -= 1
        
        
        if balance == 0:
            
            result.append(s[start + 1:i])
            start = i + 1

    return ''.join(result)


if __name__ == "__main__":
    s = input("Enter a valid parentheses string: ")
    output = decode_parentheses(s)
    print("Decoded message:", output)
